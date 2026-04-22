---
name: logging-strategy-implementation
description: Create and implement a production-ready structured logging strategy for Python and FastAPI services. Use when Codex needs to centralize logging setup, add request correlation IDs with contextvars, log request/response timing, mask sensitive data, switch dev pretty logs to production JSON logs, add global exception logging with stack traces, or prepare for OpenTelemetry-compatible distributed tracing.
---

# Logging Strategy and Implementation

## name

`logging-strategy-implementation`

## description

Build a centralized, context-aware logging foundation focused on observability, traceability, and safe log content handling for Python and FastAPI applications.

## when_to_use

Use this skill when the task requires any of the following:

- Implement structured logging in Python or FastAPI.
- Add Correlation ID (Request ID) propagation and async-safe request context.
- Log request path, method, duration, and user identity context.
- Enforce environment-based output format: readable dev logs and JSON production logs.
- Apply sensitive field masking for tokens, passwords, API keys, and PII.
- Add global exception logging with clean structured stack traces.
- Prepare logging for container log aggregation and future distributed tracing.

## tags

- logging
- structured-logging
- fastapi
- structlog
- observability
- correlation-id
- contextvars
- security
- opentelemetry

## Objective

Deliver a clean, production-ready logging system with the following outcomes:

- Use `structlog` as the primary implementation choice (Loguru optional fallback).
- Inject request context into every log event:
- `correlation_id` (or `request_id`)
- HTTP method
- request path
- request duration
- user ID (if available)
- Support log levels by environment:
- `DEBUG` only in local development
- `INFO`, `WARNING`, `ERROR`, `CRITICAL` in shared environments
- Mask sensitive data before rendering output.
- Log request/response timing with middleware.
- Capture unhandled exceptions in a global handler with structured stack traces.
- Emit to stdout for Docker and Kubernetes log collection.

Target module structure:

```text
src/
|-- core/
|   |-- config.py          # Log level, format, and environment configurations
|   `-- logger.py          # Centralized logger instance and processor setup
|-- middleware/
|   `-- logging.py         # Injects correlation_id and logs request/response timing
`-- utils/
    `-- masking.py         # PII scrubbing rules and processors
```

## Workflow (Setup Logger -> Bind Context -> Log Events -> Aggregate)

### 1) Setup Logger

- Configure logging once at startup.
- Select renderer by environment:
- Dev: colored human-readable output.
- Production: JSON output.
- Add processors in this order:
1. Add timestamps and log levels.
2. Merge `contextvars` request context.
3. Apply masking processor.
4. Render output (console or JSON).
- Always log to stdout.
- Never use `print()` in production code.

### 2) Bind Context

- Create per-request context using `contextvars`.
- Read `X-Request-ID` or `X-Correlation-ID` from headers.
- If absent, generate a UUID and return it in response headers.
- Bind `correlation_id`, `path`, `method`, and `user_id` (if available) into context.

Why Correlation ID matters:

- It ties all log lines for one request into a single searchable trace.
- It enables debugging across services when IDs are forwarded downstream.
- It reduces mean time to resolution in incident response.

Propagation rule:

- Accept `X-Request-ID` and `X-Correlation-ID`.
- Normalize to `correlation_id` internally.
- Emit `X-Request-ID` in responses.
- Forward the same ID to downstream service calls.

### 3) Log Events

- Log request start and completion with duration in milliseconds.
- Use appropriate severity:
- `DEBUG`: local troubleshooting only.
- `INFO`: normal flow milestones.
- `WARNING`: recoverable problems.
- `ERROR`: failed operations.
- `CRITICAL`: severe failures with urgent impact.
- Include exception context using structured stack traces.

### 4) Aggregate

- Keep log schema stable and machine-parseable in production JSON.
- Send logs to stdout for ingestion by ELK, Datadog, or Grafana Loki.
- Prepare future tracing integration by preserving `correlation_id`, span fields, and service name conventions.
- Expand to OpenTelemetry/Jaeger when cross-service tracing becomes mandatory.

## Best Practices

- Centralize logging config in one module and import shared logger everywhere.
- Keep event names explicit (for example `request_completed`, `db_query_failed`).
- Use key-value logs, not free-form strings.
- Ensure masking runs before final rendering.
- Validate that all outbound responses include `X-Request-ID`.
- Keep stack traces in exception events only; avoid excessive noisy traces.
- Add unit tests for masking rules and middleware context binding.
- Use JSON in production even if logs are read by humans occasionally.

## Anti-Patterns

- Using `print()` in application code.
- Reconfiguring logger in multiple files.
- Logging secrets, credentials, tokens, or full auth headers.
- Generating a new correlation ID for each internal log line.
- Emitting unstructured multiline text logs in production.
- Swallowing exceptions without logging structured context.
- Binding global mutable request context without `contextvars`.

## Example (FastAPI middleware + sample structured log output)

```python
import logging
import sys
import time
import uuid
from contextvars import ContextVar
from typing import Any

import structlog
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

request_context: ContextVar[dict[str, Any]] = ContextVar("request_context", default={})

SENSITIVE_KEYS = {"password", "token", "api_key", "authorization", "secret"}


def mask_sensitive(_, __, event_dict: dict[str, Any]) -> dict[str, Any]:
    def _mask(value: Any) -> Any:
        if isinstance(value, dict):
            return {k: ("***" if k.lower() in SENSITIVE_KEYS else _mask(v)) for k, v in value.items()}
        if isinstance(value, list):
            return [_mask(v) for v in value]
        return value

    return _mask(event_dict)


def merge_request_context(_, __, event_dict: dict[str, Any]) -> dict[str, Any]:
    event_dict.update(request_context.get())
    return event_dict


def configure_logging(env: str = "dev") -> None:
    shared_processors = [
        structlog.processors.TimeStamper(fmt="iso", utc=True),
        structlog.stdlib.add_log_level,
        merge_request_context,
        mask_sensitive,
    ]

    renderer = (
        structlog.dev.ConsoleRenderer(colors=True)
        if env == "dev"
        else structlog.processors.JSONRenderer()
    )

    structlog.configure(
        processors=[*shared_processors, renderer],
        wrapper_class=structlog.stdlib.BoundLogger,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )
    logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.INFO)


app = FastAPI()
configure_logging(env="dev")
logger = structlog.get_logger("api")


@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    correlation_id = (
        request.headers.get("X-Request-ID")
        or request.headers.get("X-Correlation-ID")
        or str(uuid.uuid4())
    )
    ctx = {
        "correlation_id": correlation_id,
        "method": request.method,
        "path": request.url.path,
        "user_id": request.headers.get("X-User-ID"),
    }
    token = request_context.set(ctx)
    started = time.perf_counter()
    try:
        response = await call_next(request)
        duration_ms = round((time.perf_counter() - started) * 1000, 2)
        logger.info("request_completed", status_code=response.status_code, duration_ms=duration_ms)
        response.headers["X-Request-ID"] = correlation_id
        return response
    finally:
        request_context.reset(token)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception("unhandled_exception", error_type=type(exc).__name__, path=request.url.path)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error", "request_id": request_context.get().get("correlation_id")},
    )
```

## Example Output (Dev vs Production logging)

Use dev output for readability and local debugging. Use production output for machine parsing and log aggregation.

| Mode | Example |
|---|---|
| Dev (Console, colored/human-readable) | `2026-04-15T04:12:33.512Z [info] request_completed correlation_id=1a2b3c method=GET path=/api/users/42 duration_ms=12.48 status_code=200 user_id=u_8841` |
| Production (JSON) | `{"timestamp":"2026-04-15T04:12:33.512Z","level":"info","event":"request_completed","correlation_id":"1a2b3c","method":"GET","path":"/api/users/42","duration_ms":12.48,"status_code":200,"user_id":"u_8841"}` |

## Reusable Templates

- `templates/logger_setup.template.py`
- `templates/logging_middleware.template.py`
- `templates/pii_scrubber.template.py`

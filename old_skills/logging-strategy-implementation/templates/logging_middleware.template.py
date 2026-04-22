from __future__ import annotations

import time
import uuid

import structlog
from fastapi import Request

logger = structlog.get_logger("request")


async def logging_middleware(request: Request, call_next):
    started = time.perf_counter()
    correlation_id = (
        request.headers.get("X-Request-ID")
        or request.headers.get("X-Correlation-ID")
        or str(uuid.uuid4())
    )

    structlog.contextvars.bind_contextvars(
        correlation_id=correlation_id,
        method=request.method,
        path=request.url.path,
        user_id=getattr(getattr(request, "state", None), "user_id", None),
    )

    try:
        response = await call_next(request)
        duration_ms = round((time.perf_counter() - started) * 1000, 2)
        logger.info(
            "request_completed",
            status_code=response.status_code,
            duration_ms=duration_ms,
        )
        response.headers["X-Request-ID"] = correlation_id
        return response
    except Exception:
        logger.exception("request_failed")
        raise
    finally:
        structlog.contextvars.clear_contextvars()

from __future__ import annotations

import logging
import sys
from typing import Any

import structlog

from src.utils.masking import mask_sensitive_event


def configure_logger(*, environment: str, log_level: str = "INFO") -> None:
    """
    Configure structlog once at app startup.
    - dev: readable console output
    - prod: JSON output for aggregators
    """
    timestamper = structlog.processors.TimeStamper(fmt="iso", utc=True)

    shared_processors: list[Any] = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.add_log_level,
        timestamper,
        mask_sensitive_event,
    ]

    renderer = (
        structlog.dev.ConsoleRenderer(colors=True)
        if environment.lower() in {"dev", "local"}
        else structlog.processors.JSONRenderer()
    )

    structlog.configure(
        processors=[*shared_processors, renderer],
        wrapper_class=structlog.stdlib.BoundLogger,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, log_level.upper(), logging.INFO),
    )


def get_logger(name: str = "app") -> structlog.stdlib.BoundLogger:
    return structlog.get_logger(name)

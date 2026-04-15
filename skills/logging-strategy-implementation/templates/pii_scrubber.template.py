from __future__ import annotations

from typing import Any

SENSITIVE_KEYS = {
    "password",
    "passphrase",
    "token",
    "access_token",
    "refresh_token",
    "api_key",
    "authorization",
    "secret",
    "ssn",
    "credit_card",
}


def _mask(value: Any) -> Any:
    if isinstance(value, dict):
        masked: dict[str, Any] = {}
        for k, v in value.items():
            masked[k] = "***REDACTED***" if k.lower() in SENSITIVE_KEYS else _mask(v)
        return masked
    if isinstance(value, list):
        return [_mask(item) for item in value]
    return value


def mask_sensitive_event(_, __, event_dict: dict[str, Any]) -> dict[str, Any]:
    return _mask(event_dict)

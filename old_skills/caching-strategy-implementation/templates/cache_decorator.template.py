from __future__ import annotations

import asyncio
import functools
import inspect
from collections.abc import Awaitable, Callable
from typing import Any

from redis.asyncio import Redis
from redis.exceptions import RedisError

from src.core.cache import get_redis


KeyBuilder = Callable[..., str]


def _lock_key(cache_key: str) -> str:
    return f"lock:{cache_key}"


def cache_response(
    *,
    key_builder: KeyBuilder,
    ttl_seconds: int = 60,
    lock_seconds: int = 5,
    wait_timeout_seconds: float = 2.0,
    wait_interval_seconds: float = 0.05,
) -> Callable[[Callable[..., Awaitable[Any]]], Callable[..., Awaitable[Any]]]:
    def decorator(func: Callable[..., Awaitable[Any]]) -> Callable[..., Awaitable[Any]]:
        signature = inspect.signature(func)

        @functools.wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            bound = signature.bind_partial(*args, **kwargs)
            cache_key = key_builder(**bound.arguments)
            redis = await get_redis()

            try:
                cached = await redis.get(cache_key)
            except RedisError:
                cached = None

            if cached is not None:
                return _deserialize(cached)

            lock_key = _lock_key(cache_key)
            have_lock = False

            try:
                have_lock = await redis.set(lock_key, "1", ex=lock_seconds, nx=True)
            except RedisError:
                have_lock = False

            if not have_lock:
                waited = 0.0
                while waited < wait_timeout_seconds:
                    await asyncio.sleep(wait_interval_seconds)
                    waited += wait_interval_seconds
                    try:
                        cached = await redis.get(cache_key)
                    except RedisError:
                        break
                    if cached is not None:
                        return _deserialize(cached)
                return await func(*args, **kwargs)

            try:
                value = await func(*args, **kwargs)
                try:
                    await redis.set(cache_key, _serialize(value), ex=ttl_seconds)
                except RedisError:
                    pass
                return value
            finally:
                try:
                    await redis.delete(lock_key)
                except RedisError:
                    pass

        return wrapper

    return decorator


def _serialize(value: Any) -> str:
    import json

    return json.dumps(value, default=str)


def _deserialize(value: str) -> Any:
    import json

    return json.loads(value)


async def write_through_user(
    *,
    user_id: int,
    payload: dict[str, Any],
    save: Callable[[int, dict[str, Any]], Awaitable[dict[str, Any]]],
    redis: Redis | None = None,
) -> dict[str, Any]:
    cache_key = f"user:{user_id}:profile"
    redis = redis or await get_redis()

    updated = await save(user_id, payload)

    try:
        await redis.set(cache_key, _serialize(updated), ex=300)
    except RedisError:
        pass

    return updated

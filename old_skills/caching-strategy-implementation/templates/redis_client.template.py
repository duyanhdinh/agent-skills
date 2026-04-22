from __future__ import annotations

import json
import os
from typing import Any

from redis.asyncio import Redis
from redis.exceptions import RedisError


REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

_redis_client: Redis | None = None


def build_redis() -> Redis:
    return Redis.from_url(
        REDIS_URL,
        encoding="utf-8",
        decode_responses=True,
        max_connections=20,
        socket_timeout=2,
        socket_connect_timeout=2,
        retry_on_timeout=True,
    )


async def get_redis() -> Redis:
    global _redis_client
    if _redis_client is None:
        _redis_client = build_redis()
    return _redis_client


async def close_redis() -> None:
    global _redis_client
    if _redis_client is not None:
        await _redis_client.close()
        _redis_client = None


async def get_json(key: str) -> Any | None:
    redis = await get_redis()
    try:
        raw = await redis.get(key)
    except RedisError:
        return None

    if raw is None:
        return None
    return json.loads(raw)


async def set_json(key: str, value: Any, ttl_seconds: int) -> bool:
    redis = await get_redis()
    try:
        await redis.set(key, json.dumps(value), ex=ttl_seconds)
        return True
    except RedisError:
        return False


async def delete_key(key: str) -> bool:
    redis = await get_redis()
    try:
        await redis.delete(key)
        return True
    except RedisError:
        return False


def user_profile_key(user_id: int) -> str:
    return f"user:{user_id}:profile"


def user_profile_lock_key(user_id: int) -> str:
    return f"lock:{user_profile_key(user_id)}"

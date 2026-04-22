---
name: caching-strategy-implementation
description: Create and implement Redis-based caching layers for backend services, especially FastAPI applications. Use when Codex needs to design or build cache-aside or write-through flows, define cache key namespaces, add TTL and invalidation rules, prevent cache stampede with distributed locks, handle Redis failure gracefully, or introduce API rate limiting backed by Redis and Docker for local development.
---

# Caching Strategy and Implementation

## name

`caching-strategy-implementation`

## description

Create production-ready caching scaffolds and implementation guidance centered on Redis. Use this skill to reduce latency, lower database load, standardize cache keys, and add reliability controls such as invalidation, rate limiting, and distributed locking.

## when_to_use

Use this skill when the task requires any of the following:

- Add Redis caching to a FastAPI service.
- Implement Cache-Aside (lazy loading) for read-heavy endpoints.
- Implement Write-Through updates so cache and database stay aligned.
- Define TTL-based and event-driven invalidation behavior.
- Prevent cache stampede or dogpiling with distributed locks.
- Add Redis-backed rate limiting for API endpoints.
- Prepare local Redis infrastructure with Docker.

## tags

- caching
- redis
- fastapi
- cache-aside
- write-through
- invalidation
- distributed-locking
- rate-limiting
- docker

## Objective

Build a robust caching layer that improves latency and reduces database load while remaining explicit, debuggable, and safe under concurrency.

Prioritize these outcomes:

- Use Redis as the primary shared cache store.
- Start with clean cache key namespaces such as `user:{id}:profile`.
- Support Cache-Aside and Write-Through patterns.
- Invalidate stale data with TTLs and update-triggered deletes.
- Prevent stampede with short-lived distributed locks around cache fills.
- Keep the service functional when Redis is degraded or unavailable.
- Support Redis-backed API rate limiting.

For small prototypes, allow in-memory caching such as a Python dict or LRU cache. Move to Redis when multiple workers, persistence, shared state, rate limiting, or distributed locks are required. Expand from Redis standalone to Sentinel or Cluster when availability or scale demands it.

## Workflow

### Setup

1. Confirm the application shape: read-heavy endpoints, write paths, and consistency requirements.
2. Start local Redis with the provided Docker template.
3. Create a shared Redis client with connection pooling in `src/core/cache.py`.
4. Add a rate limiter in `src/core/rate_limit.py` if endpoint throttling is required.
5. Add a reusable response-caching decorator in `src/decorators/cache.py`.
6. Standardize key generation in `src/utils/cache_keys.py`.

Target module structure:

```text
src/
├── core/
│   ├── cache.py
│   └── rate_limit.py
├── decorators/
│   └── cache.py
└── utils/
    └── cache_keys.py
```

Read the template files in `templates/` and adapt them to the project rather than rewriting from scratch.

### Key Design

Design keys before adding decorators or invalidation logic.

Rules:

- Use namespaces: `entity:{id}:view` instead of ad hoc strings.
- Encode dimensions that affect output: locale, query params, tenant, version.
- Keep keys stable and readable.
- Centralize builders in `cache_keys.py`.
- Include a version segment when schema or serialization may change.

Examples:

- `user:1:profile`
- `user:1:profile:v2`
- `article:42:summary:en`
- `tenant:acme:user:1:profile`
- `rate_limit:/api/users:192.168.1.10`
- `lock:user:1:profile`

Do not build keys inline across handlers. Always route key creation through helper functions so invalidation targets stay predictable.

### Read/Write Flow

#### Cache-Aside

Use for read-heavy data where the database remains the source of truth.

Flow:

1. Compute the cache key.
2. Attempt Redis read.
3. If hit, deserialize and return.
4. If miss, optionally acquire a short lock for the key.
5. Read from the database.
6. Store serialized value in Redis with TTL.
7. Release lock and return the value.

Use short TTLs for volatile data and longer TTLs for stable reference data.

#### Write-Through

Use when writes must update both the database and cache immediately.

Flow:

1. Validate input.
2. Persist the record to the database.
3. Serialize the updated representation.
4. Write the new value to Redis under the canonical key.
5. Delete or refresh any dependent aggregate keys.

Write-through reduces stale reads for the canonical object but still requires explicit invalidation for list pages, search results, counters, and derived views.

### Invalidation

Use both time-based and event-driven invalidation.

Time-based invalidation:

- Assign a TTL to every non-permanent cached item.
- Match TTL to volatility and tolerance for staleness.
- Add jitter when many keys share the same refresh cadence.

Event-driven invalidation:

- On record update, delete the exact object key and any related derived keys.
- On record delete, remove the object key and collection keys that may include it.
- On bulk updates, invalidate by namespace or version bump when targeted deletes are too expensive.

Concrete example:

- Update user `1` in the database.
- Delete `user:1:profile`.
- Also delete any dependent keys such as `user:list:active`, `tenant:acme:user:1:profile`, or a versioned summary key if they are affected.

Prefer delete-on-write when cache correctness matters more than preserving a warm cache.

## Best Practices

- Set TTLs intentionally. Typical starting points: `30-120s` for dynamic views, `5-30m` for reference data.
- Add random TTL jitter to avoid synchronized expiration bursts.
- Fail open on Redis errors for non-critical reads: serve from the database instead of failing the request.
- Log cache hits, misses, set failures, lock contention, and invalidation operations.
- Serialize consistently, preferably JSON for interoperable payloads.
- Bound lock TTLs tightly so abandoned locks clear automatically.
- Cache only values that are expensive enough to justify operational complexity.
- Keep decorators thin and move key logic to helper functions.
- Instrument hit rate, latency reduction, stampede frequency, and Redis error counts.

Handling Redis failures gracefully:

- Wrap Redis access in small helper methods.
- Catch connection and timeout exceptions.
- Bypass cache reads and writes if Redis is unhealthy.
- Never let optional cache writes block the primary database write path.
- Use conservative defaults so temporary Redis outages degrade performance, not correctness.

## Anti-Patterns

- Caching highly dynamic or personalized data without including all request dimensions in the key.
- Omitting TTL and allowing stale values to persist indefinitely.
- Building cache keys ad hoc inside route handlers.
- Caching error responses or partial objects without an explicit policy.
- Using one global lock for unrelated keys.
- Treating write-through as sufficient invalidation for list or aggregate views.
- Storing unbounded payloads or huge query results in Redis.
- Making the application hard-fail when Redis is unavailable for optional caching.

## Example

FastAPI endpoint with a Redis cache decorator:

```python
from fastapi import APIRouter, Depends, HTTPException
from redis.asyncio import Redis

from src.core.cache import get_redis
from src.decorators.cache import cache_response
from src.utils.cache_keys import user_profile_key

router = APIRouter()


async def get_user_from_db(user_id: int) -> dict | None:
    ...


@router.get("/users/{user_id}")
@cache_response(
    key_builder=lambda user_id, **_: user_profile_key(user_id),
    ttl_seconds=120,
    lock_seconds=5,
)
async def read_user(user_id: int, redis: Redis = Depends(get_redis)) -> dict:
    user = await get_user_from_db(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

Write path invalidation example:

```python
from redis.asyncio import Redis

from src.utils.cache_keys import user_profile_key


async def update_user(user_id: int, payload: dict, redis: Redis) -> dict:
    updated = await save_user_to_db(user_id, payload)
    await redis.delete(user_profile_key(user_id))
    return updated
```

Reusable assets in this skill:

- `templates/redis_client.template.py`
- `templates/cache_decorator.template.py`
- `templates/docker-compose-redis.template.yml`

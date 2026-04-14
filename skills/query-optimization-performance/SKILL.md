# query-optimization-performance

## name
query-optimization-performance

## description
Diagnose and remediate database performance bottlenecks in PostgreSQL-backed applications. Use this skill when requests involve slow endpoints, heavy ORM query paths, N+1 query patterns, EXPLAIN plan analysis, indexing strategy decisions, pagination scalability, or APM-guided query tuning in SQLAlchemy-based services.

## when_to_use
- When API latency is dominated by database calls
- When SQLAlchemy code shows N+1 query behavior or over-fetching
- When PostgreSQL queries need `EXPLAIN (ANALYZE, BUFFERS)` interpretation
- When deciding between offset pagination and cursor pagination for large tables
- When selecting or validating index types (B-Tree, Hash, GIN, GiST) for real query patterns
- When setting up slow-query visibility with application logs and APM traces

## tags
- postgresql
- sqlalchemy
- orm
- performance
- query-optimization
- explain-analyze
- indexing
- pagination
- n-plus-one
- apm

## Objective
Reduce end-to-end response latency and database load by identifying expensive query paths, removing N+1 access patterns, validating query plans with PostgreSQL EXPLAIN, applying minimal high-impact indexing, and choosing pagination approaches that keep performance stable at high row counts.

## Workflow (Identify Slow Query -> Run EXPLAIN -> Optimize ORM -> Add Index)
1. Identify the slow query path.
   - Use application-level timings around repository/service calls.
   - Enable SQLAlchemy statement logging in non-production and sample in production.
   - Correlate request spans with DB spans in APM (for example Datadog/New Relic/OpenTelemetry).
2. Capture the exact SQL and parameters.
   - Log SQL with bound values in safe environments.
   - Group repeated SQL fingerprints to spot N+1 and hot statements.
3. Run PostgreSQL plan analysis.
   - Execute `EXPLAIN (ANALYZE, BUFFERS, VERBOSE)` for the exact query.
   - Compare estimated rows vs actual rows and check scan type (`Seq Scan`, `Index Scan`, `Bitmap Heap Scan`).
4. Optimize ORM access shape.
   - Replace lazy-per-row fetches with `selectinload` or `joinedload`.
   - Select only required columns and avoid broad entity hydration when not needed.
   - Batch reads and writes where possible.
5. Add or refine indexes.
   - Add indexes only for measured hot predicates/joins/sorts.
   - Prefer composite indexes that match filter and order prefixes.
   - Re-run EXPLAIN and load test to verify improvement.
6. Validate and guard against regressions.
   - Compare p50/p95/p99 latency, DB CPU, shared buffers hit ratio, and query count per request.
   - Add tests that assert bounded query counts for common endpoints.

## Best Practices (Cursor pagination, Composite Indexes, eager loading)
### Cursor pagination
- Use cursor pagination for large, append-heavy tables and infinite-scroll APIs.
- Keep ordering deterministic with `(created_at, id)` or another unique tie-break pair.
- Index cursor columns in the same order as the query.

### Composite indexes
- Align index column order with your actual `WHERE` and `ORDER BY` patterns.
- Example: query filters by `tenant_id`, `status` and sorts by `created_at DESC`; index should start with `tenant_id, status, created_at DESC`.
- Remove redundant indexes that are fully covered by other composites.

### Eager loading for N+1 prevention
- Use `selectinload` for one-to-many collections in list endpoints.
- Use `joinedload` for one-to-one/many-to-one when row explosion risk is low.
- Add automated query-count checks in integration tests for high-traffic handlers.

### Index trade-offs (required)
- Benefit: faster reads for filtered/joined/sorted queries.
- Cost: slower writes (`INSERT/UPDATE/DELETE` must maintain indexes).
- Cost: additional storage and memory pressure.
- Rule: create indexes only when measurements prove recurring read-path benefit.

### Slow query logging in a standard API setup (required)
Use SQLAlchemy event hooks to emit warning logs when statements exceed a threshold:

```python
import logging
import time
from sqlalchemy import event
from sqlalchemy.engine import Engine

log = logging.getLogger("db.slow")
SLOW_QUERY_MS = 200

@event.listens_for(Engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    conn.info.setdefault("query_start_time", []).append(time.perf_counter())

@event.listens_for(Engine, "after_cursor_execute")
def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    start = conn.info["query_start_time"].pop(-1)
    duration_ms = (time.perf_counter() - start) * 1000
    if duration_ms >= SLOW_QUERY_MS:
        log.warning(
            "slow_query duration_ms=%.2f rows=%s sql=%s",
            duration_ms,
            cursor.rowcount,
            statement,
        )
```

Forward these logs into APM or log analytics and correlate with endpoint traces.

### Offset vs cursor pagination comparison (required)
- Offset pagination (`LIMIT/OFFSET`)
  - Simple and page-number friendly.
  - Degrades on large offsets because the database still scans/skips many rows.
  - Vulnerable to duplicates/misses when concurrent writes happen.
- Cursor pagination (`WHERE (created_at, id) < (:created_at, :id) LIMIT :limit`)
  - Stable performance for deep pagination when indexed.
  - Better consistency for changing datasets.
  - Requires opaque cursor handling in API contracts.

## Anti-Patterns (e.g., `SELECT *` on large tables, missing indices on Foreign Keys)
- `SELECT *` from wide/high-row tables in latency-sensitive endpoints
- Missing indexes on foreign keys used for joins
- Adding indexes before measuring query workload
- Ignoring `actual` vs `estimated` row mismatch in EXPLAIN output
- Large `OFFSET` values on frequently accessed feeds
- ORM lazy loading inside loops without eager loading strategy
- Using GIN on columns that only need simple equality lookups
- Keeping duplicate overlapping indexes that increase write overhead

## Example (SQLAlchemy N+1 before/after, PostgreSQL EXPLAIN ANALYZE interpretation)
### N+1 query remediation
Before (N+1):
```python
posts = session.execute(select(Post).order_by(Post.created_at.desc()).limit(50)).scalars().all()
payload = []
for post in posts:
    payload.append({
        "id": post.id,
        "title": post.title,
        "author_name": post.author.name,  # triggers lazy query per row
    })
```

After (eager loading):
```python
from sqlalchemy.orm import joinedload

posts = (
    session.execute(
        select(Post)
        .options(joinedload(Post.author))
        .order_by(Post.created_at.desc())
        .limit(50)
    )
    .scalars()
    .all()
)
payload = [{"id": p.id, "title": p.title, "author_name": p.author.name} for p in posts]
```

### Concrete optimization diff (required)
```diff
- posts = session.execute(select(Post).order_by(Post.created_at.desc()).limit(50)).scalars().all()
- payload = []
- for post in posts:
-     payload.append({
-         "id": post.id,
-         "title": post.title,
-         "author_name": post.author.name,
-     })
+ posts = (
+     session.execute(
+         select(Post)
+         .options(joinedload(Post.author))
+         .order_by(Post.created_at.desc())
+         .limit(50)
+     )
+     .scalars()
+     .all()
+ )
+ payload = [{"id": p.id, "title": p.title, "author_name": p.author.name} for p in posts]
```

### EXPLAIN ANALYZE interpretation
Example (slow):
```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT id, tenant_id, created_at
FROM events
WHERE tenant_id = 't1'
ORDER BY created_at DESC
LIMIT 100;
```

If output shows `Seq Scan on events` with high `Rows Removed by Filter`, add a composite index:
```sql
CREATE INDEX CONCURRENTLY idx_events_tenant_created_at_desc
ON events (tenant_id, created_at DESC);
```

Re-run EXPLAIN. A healthy result usually shifts to `Index Scan` or `Bitmap Heap Scan` with lower total execution time and fewer shared block reads.

## References
- Read [references/indexing-strategies.md](references/indexing-strategies.md) when choosing among B-Tree, Hash, GIN, and GiST indexes in PostgreSQL.

# PostgreSQL Indexing Strategies

## Purpose
Use this guide to choose index types based on measured query patterns, not assumptions.

## Fast decision path
1. Start with observed slow queries from logs/APM.
2. Confirm access pattern (`WHERE`, `JOIN`, `ORDER BY`, operators).
3. Pick the minimal index that supports the pattern.
4. Validate with `EXPLAIN (ANALYZE, BUFFERS)`.
5. Keep only indexes with sustained benefit.

## B-Tree index
### Best for
- Equality: `=`, `IN`
- Range: `>`, `>=`, `<`, `BETWEEN`
- Sorting: `ORDER BY` (same prefix/order)
- Join keys and foreign keys

### Typical usage
```sql
CREATE INDEX CONCURRENTLY idx_orders_customer_created
ON orders (customer_id, created_at DESC);
```

### Notes
- Default and most common index type in PostgreSQL.
- Composite order matters; match real predicates.
- Good baseline for pagination with deterministic ordering.

## Hash index
### Best for
- High-volume equality-only lookups on a single column.

### Typical usage
```sql
CREATE INDEX CONCURRENTLY idx_sessions_token_hash
ON sessions USING hash (token);
```

### Notes
- Usually prefer B-Tree unless equality-only behavior is proven and beneficial.
- Limited feature set compared to B-Tree.

## GIN index
### Best for
- Containment and membership operations on `jsonb`, arrays, full-text vectors.
- Examples: `@>`, `?`, `?|`, `?&`.

### Typical usage (JSONB)
```sql
CREATE INDEX CONCURRENTLY idx_events_payload_gin
ON events USING gin (payload jsonb_path_ops);
```

### Notes
- Powerful for document-like data and multi-value columns.
- Larger and slower to maintain on writes than simple B-Tree indexes.
- Choose operator class (`jsonb_ops` vs `jsonb_path_ops`) based on operator mix.

## GiST index
### Best for
- Geometric/spatial types, ranges, nearest-neighbor style queries.
- Mixed scenarios requiring extensible operator classes.

### Typical usage
```sql
CREATE INDEX CONCURRENTLY idx_booking_period_gist
ON bookings USING gist (reservation_period);
```

### Notes
- Often used with PostGIS and range types.
- Can support queries that B-Tree cannot.

## BRIN index (optional for very large append-only tables)
### Best for
- Massive tables where column values correlate with physical order (e.g., timestamp in append-only logs).

### Typical usage
```sql
CREATE INDEX CONCURRENTLY idx_logs_created_brin
ON logs USING brin (created_at);
```

### Notes
- Tiny index size and cheap maintenance.
- Lower precision than B-Tree; may still touch more heap blocks.

## Composite index design rules
- Put strongest equality filters first.
- Place range/sort columns after equality columns.
- Match query order direction where relevant (`DESC`/`ASC`).
- Avoid creating both `(a, b)` and `(a)` unless the single-column index is truly needed.

## Partial indexes
Use when hot queries target a stable subset of rows.

```sql
CREATE INDEX CONCURRENTLY idx_jobs_pending_created
ON jobs (created_at)
WHERE status = 'pending';
```

Benefits: smaller index, faster writes than full-table alternative.

## Include columns (covering indexes)
Use `INCLUDE` to avoid heap fetches for frequently selected non-filter columns.

```sql
CREATE INDEX CONCURRENTLY idx_orders_customer_created_cover
ON orders (customer_id, created_at DESC)
INCLUDE (status, total_amount);
```

## Validation checklist
- Compare query plan before/after index creation.
- Confirm execution time and shared read blocks improve.
- Measure write overhead impact on insert/update-heavy paths.
- Ensure index is used in production-like data distribution.
- Re-check after schema or workload changes.

## Common mistakes
- Indexing every column indiscriminately.
- Ignoring foreign key indexes.
- Creating GIN for simple equality queries better served by B-Tree.
- Relying on development dataset plans that do not match production scale.

# SQL vs NoSQL Guidelines

Use PostgreSQL as the default choice when the system depends on strong relational integrity, transactional guarantees, explicit constraints, and predictable joins across entities. Use MongoDB only when document flexibility, aggregate retrieval, or rapidly changing sparse fields outweigh the need for strict relational enforcement.

## Default Recommendation
Choose PostgreSQL first for most product systems with users, roles, orders, payments, subscriptions, inventory, content ownership, or any model where relationships are core to correctness.

## Decision Matrix

| Decision Area | PostgreSQL | MongoDB |
| --- | --- | --- |
| Relationship complexity | Best for rich 1:1, 1:N, N:M models with joins and foreign keys | Best when most reads center on a single aggregate document |
| Data integrity | Strong constraints, ACID transactions, checks, uniqueness, foreign keys | Weaker relational enforcement, application-level integrity is more common |
| Schema evolution | Structured migrations, controlled change management | Flexible schemas, easier for rapidly changing payloads |
| Query style | Rich SQL, reporting, analytics, joins, window functions | Document retrieval, nested object reads, denormalized access |
| Performance strategy | Indexing, partitioning, replicas, query optimization | Embedding, selective referencing, shard-oriented scale |
| Team ergonomics | Excellent when schema discipline matters | Useful when product shape is still fluid and document boundaries are obvious |

## Choose PostgreSQL When
- Data integrity is a hard requirement
- The domain has meaningful relationships across entities
- You need transactions spanning multiple tables
- Reporting queries, joins, or aggregation are common
- You want strict typing and constraints enforced in the database
- Auditability and lifecycle tracking matter

## Choose MongoDB When
- Most reads and writes revolve around self-contained documents
- Data shape changes frequently and fields are sparse or optional
- Embedding related data reduces the need for cross-collection joins
- You can tolerate more integrity enforcement in application logic
- The domain is naturally document-oriented rather than relational

## Pivot Signals From PostgreSQL to MongoDB
- The model is dominated by variable nested payloads rather than stable entities
- Join-heavy normalization is creating more complexity than value
- Product speed depends on retrieving entire aggregates as single documents
- The team repeatedly stores semi-structured data that does not justify full relational modeling

## Do Not Use MongoDB Just Because
- The schema might change later
- JSON feels easier than modeling relationships correctly
- Foreign keys and constraints seem inconvenient
- Early scale concerns are speculative rather than measured

## PostgreSQL + MongoDB Split Guidance
If both appear necessary, keep the boundary explicit:
- PostgreSQL owns transactional and relational source-of-truth data
- MongoDB owns document-centric or flexible-content workloads
- Synchronization rules, ownership, and consistency expectations must be documented before implementation

## Redis Boundary
Do not treat Redis as a primary database in this skill. Hand off caching, session storage, or ephemeral acceleration concerns to the caching skill or architecture guidance.

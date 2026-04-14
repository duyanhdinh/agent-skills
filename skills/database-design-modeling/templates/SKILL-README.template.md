# Database Design and Modeling Scaffold

## Included Structure
- `db/schema/` for strongly typed schema definitions
- `db/migrations/` for generated migrations
- `db/seeds/` for local development and test data
- `db/index.ts` for client initialization and pooling
- `docs/db/ERD.dbml` for ERD visualization
- `docs/db/data-dictionary.md` for column and ownership documentation
- `docker-compose.yml` for local PostgreSQL

## Defaults
- PostgreSQL as the primary database
- Normalization up to 3NF
- Explicit foreign keys and indexing strategy
- `created_at`, `updated_at`, and optional `deleted_at`
- UUID primary keys unless a simpler local-only integer strategy is justified

## Expansion Rule
Keep the schema centralized until the database reaches roughly 30-50 tables or the project shifts to domain-driven boundaries.

# database-design-modeling

## name
database-design-modeling

## description
Create a professional, scalable database design and modeling scaffold centered on PostgreSQL. Use strongly typed schema definitions, explicit relational constraints, ERD documentation through DBML, and local database provisioning through Docker Compose. Include clear pivot guidance for MongoDB when data shape, access patterns, or scale characteristics stop fitting a relational model.

## when_to_use
- When designing a new PostgreSQL-backed application schema from scratch
- When formalizing entities, relationships, constraints, indexes, and migrations
- When an AI agent needs to scaffold database files, DBML diagrams, and local database setup
- When deciding whether the workload should remain relational or pivot to MongoDB
- When defining type-safe access patterns with Drizzle ORM, Prisma, or SQLAlchemy

## tags
- database
- postgresql
- mongodb
- drizzle
- prisma
- sqlalchemy
- dbml
- erd
- schema-design
- indexing
- normalization

## Objective
Design a clean, maintainable database architecture optimized for data integrity, strict constraints, ACID compliance, high-performance read and write operations, logical indexing, and clear relationship mapping across 1:1, 1:N, and N:M models. Default to centralized schema definitions for monoliths, keep the initial structure flat and focused, and enforce strict typing and constraints at the database layer rather than relying on application code alone.

## Workflow
1. Clarify domain boundaries, core entities, lifecycle rules, and access patterns before writing any schema.
2. Model entities and relationships in normalized form up to 3NF by default.
3. Choose primary keys deliberately:
   - Prefer UUIDs for distributed systems, external exposure, or multi-writer scenarios.
   - Use auto-increment integers only when operational simplicity clearly outweighs portability and security concerns.
4. Define columns with strict data types, nullability, defaults, uniqueness, and check constraints at the database level.
5. Map relationships explicitly with foreign keys:
   - 1:1 via unique foreign key
   - 1:N via foreign key on the child table
   - N:M via explicit join table with composite uniqueness
6. Add audit fields to mutable tables:
   - `created_at`
   - `updated_at`
   - optional `deleted_at` for soft deletes
7. Plan indexing intentionally:
   - Index every foreign key
   - Index frequently filtered and sorted columns
   - Add composite indexes only for proven query patterns
   - Avoid redundant indexes that overlap existing unique or composite coverage
8. Document the model in `docs/db/ERD.dbml` and keep it aligned with the code schema.
9. Scaffold database runtime files:
   - `db/index.ts` for connection pooling and client initialization
   - `db/schema/` for schema definitions
   - `db/seeds/` for development and test seed flows
   - `db/migrations/` for generated migrations
10. Validate the design against expected growth:
   - Stay centralized for monoliths and moderate table counts
   - Expand to domain-driven database modules when the system exceeds roughly 30-50 tables, moves toward DDD or microservices, or faces read and write contention that demands replicas or sharding
11. Evaluate whether PostgreSQL still fits. If the workload centers on flexible documents, sparse attributes, or aggregate retrieval with limited relational guarantees, review the SQL vs NoSQL reference before pivoting.

## Best Practices

### Naming conventions
- Use `snake_case` for database tables, columns, constraints, indexes, and join tables.
- Use plural table names when they represent collections, such as `users`, `posts`, and `post_tags`.
- Use `camelCase` only in application models and typed client code.
- Name foreign keys predictably, such as `user_id`, `post_id`, and `created_by`.
- Name indexes by table and column intent, such as `idx_posts_author_id` or `idx_users_email`.

### Normalization and denormalization
- Normalize to 3NF by default for relational designs.
- Separate repeating groups and derived fields unless there is a measured performance reason not to.
- Denormalize only when query cost, reporting requirements, or hot read paths justify it.
- If denormalizing, document ownership, refresh strategy, and consistency expectations explicitly.

### Indexing
- Require indexes for all foreign keys.
- Index columns used in `WHERE`, `JOIN`, `ORDER BY`, and high-cardinality lookups.
- Use composite indexes in the same order as real query predicates.
- Re-check index usefulness after adding uniqueness constraints to avoid duplication.

### Data types
- Prefer `uuid`, `text`, `varchar(n)` only when bounded length matters, `boolean`, `integer`, `bigint`, `numeric`, `jsonb`, and `timestamp with time zone`.
- Use `jsonb` sparingly for bounded extensibility, not as a replacement for relational structure.
- Use enums cautiously; stable lookup tables are often easier to evolve.

### Auditing and soft deletes
- Add `created_at` and `updated_at` to mutable business tables.
- Use `deleted_at` for soft deletes when restoration, auditability, or legal retention is required.
- Pair soft deletes with filtered queries and indexes that match the active-row access pattern.

### Connection and runtime
- Use connection pooling in `db/index.ts`.
- Keep migrations generated and deterministic.
- Seed only development and test-safe data.
- Separate schema ownership from query logic as complexity grows.

## Anti-Patterns
- God tables that mix unrelated domains and accumulate nullable columns
- Missing foreign key constraints because validation was deferred to application code
- Storing relational data in unbounded JSON blobs without indexing or ownership rules
- Premature sharding or replica topology in the base scaffold
- Composite indexes created without a real query pattern
- Soft deletes without query filters, causing accidental inclusion of inactive rows
- Auto-increment IDs exposed publicly when enumeration risk matters
- Polymorphic associations implemented without strong constraints or clear ownership

## Schema Structure Guidelines
Start with a centralized schema layout for monoliths:

```text
db/
  schema/
    users.ts
    posts.ts
  migrations/
  seeds/
    index.ts
  index.ts
docs/
  db/
    ERD.dbml
    data-dictionary.md
docker-compose.yml
.env.example
```

This is the recommended default because it keeps schema discovery simple, migration generation straightforward, and cross-table constraints easy to reason about.

Expand into domain-driven modules when one or more of these triggers appear:
- The database grows beyond 30-50 tables
- The project transitions toward microservices or Domain-Driven Design
- Read and write contention requires replicas, partitioning, or sharding strategies

Expanded structure:

```text
src/
  domains/
    users/
      db/
        schema.ts
        queries.ts
    orders/
      db/
        schema.ts
        queries.ts
```

## Example

### Example schema definition with Drizzle
```ts
// db/schema/users.ts
import { pgTable, text, timestamp, uuid, uniqueIndex } from "drizzle-orm/pg-core";

export const users = pgTable(
  "users",
  {
    id: uuid("id").defaultRandom().primaryKey(),
    email: text("email").notNull(),
    displayName: text("display_name").notNull(),
    createdAt: timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
    updatedAt: timestamp("updated_at", { withTimezone: true }).defaultNow().notNull(),
    deletedAt: timestamp("deleted_at", { withTimezone: true }),
  },
  (table) => ({
    emailUnique: uniqueIndex("uq_users_email").on(table.email),
  })
);
```

```ts
// db/schema/posts.ts
import { pgTable, text, timestamp, uuid, index } from "drizzle-orm/pg-core";
import { users } from "./users";

export const posts = pgTable(
  "posts",
  {
    id: uuid("id").defaultRandom().primaryKey(),
    authorId: uuid("author_id").notNull().references(() => users.id, { onDelete: "restrict" }),
    title: text("title").notNull(),
    body: text("body").notNull(),
    createdAt: timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
    updatedAt: timestamp("updated_at", { withTimezone: true }).defaultNow().notNull(),
    deletedAt: timestamp("deleted_at", { withTimezone: true }),
  },
  (table) => ({
    authorIdx: index("idx_posts_author_id").on(table.authorId),
    createdIdx: index("idx_posts_created_at").on(table.createdAt),
  })
);
```

### Example connection setup
```ts
// db/index.ts
import "dotenv/config";
import { drizzle } from "drizzle-orm/node-postgres";
import { Pool } from "pg";

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  max: 10,
  idleTimeoutMillis: 30_000,
  connectionTimeoutMillis: 5_000,
});

export const db = drizzle(pool);
export { pool };
```

### Example Docker Compose
```yml
version: "3.9"

services:
  postgres:
    image: postgres:16
    container_name: app_postgres
    restart: unless-stopped
    environment:
      POSTGRES_DB: app_db
      POSTGRES_USER: app_user
      POSTGRES_PASSWORD: app_password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### Example DBML
```dbml
Table users {
  id uuid [pk]
  email text [not null, unique]
  display_name text [not null]
  created_at timestamptz [not null]
  updated_at timestamptz [not null]
  deleted_at timestamptz
}

Table posts {
  id uuid [pk]
  author_id uuid [not null, ref: > users.id]
  title text [not null]
  body text [not null]
  created_at timestamptz [not null]
  updated_at timestamptz [not null]
  deleted_at timestamptz

  indexes {
    author_id
    created_at
  }
}
```

### Example agent execution checklist
- Create or update `db/schema/*.ts` with strict constraints and explicit foreign keys.
- Add or refresh `docs/db/ERD.dbml` to match the schema.
- Ensure every foreign key and common filter path has a deliberate index.
- Keep the initial structure flat unless the scaling triggers are already present.
- Review `references/sql-vs-nosql-guidelines.md` before proposing MongoDB.

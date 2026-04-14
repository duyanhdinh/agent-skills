---
name: database-migrations-lifecycle
description: Manage database schema evolution, Alembic migrations, and data seeding with strict safety controls. Use when implementing or reviewing SQLAlchemy/FastAPI schema changes, generating migration scripts, validating migration behavior in CI/CD, handling rollback strategy, and planning zero-downtime breaking changes such as column renames or drops.
---

# name
database-migrations-lifecycle

# description
Create and enforce a strict workflow for schema changes, migration generation/review, seeding, rollout, rollback, and zero-downtime migration handling in SQLAlchemy/Alembic projects.

# when_to_use
Use this skill when:
- Adding, modifying, or removing SQLAlchemy models in a FastAPI project
- Creating Alembic migration scripts for any schema change
- Reviewing auto-generated migration files before merge
- Validating upgrades/downgrades in CI/CD
- Designing zero-downtime strategies for breaking changes (rename/drop columns)
- Building deterministic seed processes for local/dev/test environments

# tags
- database
- migrations
- alembic
- sqlalchemy
- fastapi
- ci-cd
- zero-downtime
- seeding

# Objective
Generate safe, automated, and reviewable database evolution processes using Alembic and SQLAlchemy:
- Set up and maintain migration tooling
- Enforce mandatory human/agent review of auto-generated migrations before commit
- Provide robust, idempotent seeding for dev/test
- Support zero-downtime schema evolution and reliable rollback

# Project Structure
Use this target structure in application repositories:
```text
alembic/
|-- versions/           # Versioned migration scripts
|-- env.py              # Alembic environment setup (tied to app metadata)
`-- script.py.mako      # Migration file template
scripts/
|-- migrate.sh          # Wrapper script for CI/CD
`-- seed_db.py          # Script to populate initial lookup data
alembic.ini             # Root configuration
```

# Workflow (Model update -> Generate -> Review -> Upgrade -> Verify)
1. Model update
- Update SQLAlchemy models in the FastAPI app (for modular structure, keep models under feature modules, then expose all metadata in a shared Base metadata import path).
- Confirm naming, nullability, defaults, indexes, and constraints are explicit in model code.

2. Generate
- Create revision from model metadata diff:
  - `alembic revision --autogenerate -m "describe_change"`
- Never merge directly after generation.

3. Review (MANDATORY)
- MUST review every auto-generated migration file before commit.
- Validate:
  - Correct table/column targets
  - No accidental drops
  - Expected types/constraints/defaults
  - Upgrade and downgrade symmetry
  - Transaction safety and data backfill logic
- If autogenerate misses business logic or data transforms, manually edit migration script.
- Reject commit if review is not completed.

4. Upgrade
- Apply migration in controlled order:
  - Local/dev: `alembic upgrade head`
  - CI: run full upgrade on ephemeral DB
  - Staging/prod: run through deployment pipeline with prechecks and backups

5. Verify
- Verify schema after upgrade with smoke checks:
  - Application startup and health endpoints
  - Critical read/write paths
  - Data integrity checks
- Validate rollback path:
  - `alembic downgrade -1` or targeted revision in non-prod validation
- Confirm migration status:
  - `alembic current`
  - `alembic history --verbose`

# Best Practices (Idempotent seeders, backward-compatible migrations)
- Keep seeders idempotent (upsert or existence checks; no duplicate rows).
- Use backward-compatible expand/contract migrations for live systems.
- Prefer additive changes first (new columns/tables), then gradual cutover, then cleanup.
- Keep each migration focused and small; one concern per revision where possible.
- Include explicit downgrade logic unless policy forbids it; if irreversible, document why.
- Pin migration checks in CI:
  - Upgrade from base to head
  - Optional downgrade test in disposable DB
  - Fail pipeline on migration errors or drift
- Use feature flags/application dual-write patterns when transitioning between old/new schema fields.
- Coordinate migration execution timing with deployment rollout.

# Anti-Patterns (e.g., editing old migration files instead of creating new ones)
- Editing previously committed migration files that already shipped to shared environments.
- Trusting autogenerate output without manual review.
- Combining destructive schema changes with same-release app code that still depends on old schema.
- Non-idempotent seed scripts that duplicate or corrupt lookup data.
- Dropping columns/tables immediately without deprecation period in production systems.
- Running production migrations without backup/restore and rollback plan.

# Example (A complete Alembic env.py setup and a safe column rename flow)
## Example A: Alembic `env.py` for FastAPI modular structure
```python
from __future__ import annotations

from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool

# Import Base metadata exposed by your FastAPI app.
# Example package layout:
# app/
#   core/db.py               -> defines Base
#   features/users/models.py -> imports register on Base.metadata
from app.core.db import Base
from app.features.users import models as users_models  # noqa: F401
from app.features.orders import models as orders_models  # noqa: F401

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        compare_server_default=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

## Example B: Safe zero-downtime column rename flow
Goal: Rename `users.full_name` to `users.display_name` without downtime.

Step 1: Add new column (expand)
- Migration A:
  - Add nullable `display_name`
  - Keep `full_name` in place

Step 2: Copy data
- In Migration A or dedicated data migration:
  - Backfill `display_name = full_name` for existing rows
- Update application code:
  - Write both fields on updates (dual-write) during transition
  - Read from `display_name` with fallback to `full_name` if needed

Step 3: Drop old column (contract, later release)
- After all app instances use `display_name` and data is fully migrated:
  - Migration B removes `full_name`
  - Remove fallback/dual-write logic in app code

Never do direct single-step rename in production if it can break running versions.

# {{ project_name }}

FastAPI service scaffolded as a Modular Monolith (feature-based) with flat-first modules.

## Architecture
- Pattern: Modular Monolith
- Module strategy: Flat-first, expand only on clear complexity triggers
- API versioning: `/api/v1`

## Quick Start
```bash
python -m venv .venv
. .venv/Scripts/activate
pip install -e ".[dev]"
make dev
```

## Project Layout
```text
src/
  core/
  api/v1/
  modules/
  shared/
tests/
alembic/
```

## Quality Commands
```bash
make lint
make typecheck
make test
```

## Module Rules
Each module starts flat (`models.py`, `schemas.py`, `service.py`, `routes.py`, etc.).  
Expand to subfolders only when complexity triggers are met (size, role-split routes, multiple services, schema sprawl, heavy data access logic).

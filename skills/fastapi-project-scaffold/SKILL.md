---
name: fastapi-project-scaffold
description: Build a production-ready FastAPI project scaffold using a Modular Monolith (feature-based) architecture with a flat-first module structure and explicit expansion rules. Use when creating a new FastAPI codebase, standardizing an existing FastAPI repository layout, or generating repeatable bootstrap artifacts (project skeleton, module templates, config, and API routing conventions) for teams that want clean architecture without early over-engineering.
---

# Name
`fastapi-project-scaffold`

# Description
Create a clean, scalable FastAPI project baseline that starts simple and stays maintainable as features grow.

## When_to_use
Use this skill when:
- A new FastAPI service needs a production-friendly starter structure.
- A team wants feature-based modular monolith organization instead of a layered-by-type tree.
- The codebase should start flat per module and expand only when complexity justifies it.
- You need consistent templates for `main.py`, configuration, routing, and feature modules.

## Tags
- fastapi
- modular-monolith
- project-scaffold
- clean-architecture
- pydantic-v2
- async-python

## Objective
Generate a FastAPI project base that:
- Uses Modular Monolith (feature-based) architecture.
- Starts with a flat file structure inside each module.
- Includes explicit triggers and a target structure for module expansion.
- Uses modern FastAPI patterns: async endpoints, `Depends`, and Pydantic v2 settings/models.

## Workflow
1. Gather project intent using [templates/project-brief-template.md](templates/project-brief-template.md).
2. Generate the recommended folder skeleton from "Recommended Project Layout".
3. Create core bootstrap files using:
- [templates/main.py.template](templates/main.py.template)
- [templates/core_config.py.template](templates/core_config.py.template)
- [templates/router_v1.py.template](templates/router_v1.py.template)
4. Create each feature module from [templates/module_template](templates/module_template).
5. Wire module routers into `src/api/v1/router.py`.
6. Add delivery/support files:
- [templates/pyproject.toml.template](templates/pyproject.toml.template)
- [templates/Makefile.template](templates/Makefile.template)
- [templates/README.template.md](templates/README.template.md)
7. Validate the scaffold:
- App boots successfully.
- Health endpoint responds.
- Imports are clean and module boundaries are clear.
8. Apply module expansion rules only when triggers are met (see "Module Structure Guidelines").

## Best Practices
- Keep modules independent; avoid cross-module direct database access.
- Keep business logic in `service.py`; keep routes thin.
- Require `service.py` to depend on `repository.py` for persistence; services must not call the database directly.
- Use `Depends` for infrastructure and request-scoped dependencies.
- Keep shared helpers minimal and framework-agnostic where possible.
- Use typed settings and explicit environment defaults.
- Enforce quality gates (`ruff`, `mypy`, `pytest`) from the start.
- Prefer migration tooling (`alembic`) over ad-hoc schema changes.

## Anti-Patterns
- Creating deep nested folders in every module before complexity appears.
- Putting domain logic in route handlers.
- Executing ORM queries or session calls directly inside `service.py`.
- Coupling schemas, ORM models, and transport contracts as one class.
- Sharing mutable global state for request-specific data.
- Overloading `shared/` into a second monolith.
- Introducing microservices boundaries at bootstrap without clear operational need.

## Module Structure Guidelines
### Flat-first (default)
Start every module with:
- `__init__.py`
- `models.py`
- `schemas.py`
- `repository.py`
- `service.py`
- `routes.py`
- `dependencies.py`
- `constants.py`
- `exceptions.py`
- `helpers.py`

Rationale:
- Minimal cognitive overhead for new contributors.
- Fast navigation in early-stage modules.
- Easy refactor path once growth signals are explicit.

### Expansion triggers
Expand a module from flat files to subfolders when one or more apply:
- Module exceeds roughly 400-500 lines of code.
- Routes split into clear groups (for example `public`, `user`, `admin`).
- Multiple distinct service classes emerge.
- Schemas become complex (base/request/response/internal variants).
- Repository/data access logic grows large.
- Module adds background tasks, events, or domain-specific utilities.

### Expanded structure target
Use this shape after expansion:
```text
users/
  models.py
  schemas/
    __init__.py
    base.py
    request.py
    response.py
  services/
    user_service.py
    profile_service.py
  routes/
    __init__.py
    base.py
    profile.py
    admin.py
  repositories/
  helpers.py
  constants.py
  exceptions.py
```

### Expansion rule
Do not expand on speculation. Expand only after measurable complexity appears.

## Recommended Project Layout
```text
src/
  main.py
  core/
    config.py
    database.py
    security.py
    dependencies.py
    logging_config.py
    exceptions.py
  api/
    v1/
      router.py
  modules/
    users/
      __init__.py
      models.py
      schemas.py
      repository.py
      service.py
      routes.py
      dependencies.py
      constants.py
      exceptions.py
      helpers.py
  shared/
    utils.py
tests/
  unit/
  integration/
  conftest.py
alembic/
.env.example
pyproject.toml
Dockerfile
docker-compose.yml
README.md
Makefile
.gitignore
.github/workflows/ci.yml
```

## Example
### `src/main.py`
```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.api.v1.router import api_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Initialize connections/resources here when needed.
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI Modular Monolith",
        version="0.1.0",
        lifespan=lifespan,
    )
    app.include_router(api_router, prefix="/api/v1")

    @app.get("/health", tags=["system"])
    async def health_check() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
```

### `src/core/config.py`
```python
from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = Field(default="FastAPI Modular Monolith")
    app_env: str = Field(default="development")
    debug: bool = Field(default=True)
    database_url: str = Field(default="postgresql+asyncpg://user:pass@localhost:5432/app")
    jwt_secret: str = Field(default="change-me")
    jwt_algorithm: str = Field(default="HS256")


@lru_cache
def get_settings() -> Settings:
    return Settings()
```

### Sample users module (flat-first)
`src/modules/users/models.py`
```python
from sqlalchemy.orm import Mapped, mapped_column
from src.core.database import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    full_name: Mapped[str]
```

`src/modules/users/schemas.py`
```python
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    full_name: str


class UserRead(BaseModel):
    id: int
    email: EmailStr
    full_name: str
```

`src/modules/users/repository.py`
```python
from src.modules.users.schemas import UserCreate


class UserRepository:
    async def create_user(self, payload: UserCreate) -> dict[str, str | int]:
        # Replace with ORM/database code.
        return {"id": 1, "email": payload.email, "full_name": payload.full_name}
```

`src/modules/users/service.py`
```python
from src.modules.users.repository import UserRepository
from src.modules.users.schemas import UserCreate, UserRead


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    async def create_user(self, payload: UserCreate) -> UserRead:
        created = await self.repository.create_user(payload)
        return UserRead(**created)
```

`src/modules/users/routes.py`
```python
from fastapi import APIRouter, Depends, status
from src.modules.users.dependencies import get_user_service
from src.modules.users.schemas import UserCreate, UserRead
from src.modules.users.service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(
    payload: UserCreate,
    service: UserService = Depends(get_user_service),
) -> UserRead:
    return await service.create_user(payload)
```

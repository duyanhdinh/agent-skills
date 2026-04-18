# FastAPI Modular Monolith: Flat-First Architecture Guide

## Purpose
This reference explains why a FastAPI project should start with flat feature modules, when to expand into subfolders, and how this compares to layered architecture.

## Why Modular Monolith for FastAPI
A Modular Monolith keeps deployment and operations simple (single service) while enforcing domain boundaries in code. For most teams, this gives better speed-to-delivery than early microservices and better maintainability than a single undifferentiated package.

### Practical advantages
- One deployable artifact and one runtime environment.
- Clear feature ownership under `src/modules/<feature>/`.
- Easy local development and testing.
- Straightforward migration path to separate services later, if needed.

## Why Start Flat-First
Each feature begins with these core files:
- `models.py`
- `schemas.py`
- `service.py`
- `routes.py`
- `dependencies.py`
- `exceptions.py`

Add these support files only when justified:
- `constants.py`
- `helpers.py`

Important constraint:
- `constants.py` and `helpers.py` are optional support files, not required dumping grounds.
- If a module does not need real constants or tightly scoped helpers, omit those files.
- Prefer domain-named files over generic ones as soon as code carries business meaning.

### Benefits of flat-first
- Faster setup and onboarding.
- Lower navigation overhead in small modules.
- Fewer premature abstractions.
- Refactoring remains cheap while the module is still small.

## When to Refactor into Subfolders
Refactor only when complexity is visible and persistent.

### Trigger checklist
- File/module size is consistently beyond ~400-500 LOC.
- Routes naturally split by role or use-case.
- More than one service class exists with distinct responsibilities.
- Schemas diverge into base/request/response/internal variants.
- Data access logic needs dedicated repositories.
- The module adds async jobs/events/integration adapters.
- `helpers.py` accumulates unrelated validation, mapping, parsing, formatting, or policy code.
- `service.py` becomes a catch-all orchestrator for multiple use cases.

If no trigger is present, keep the module flat.

## Suggested Expanded Module Shape
```text
<module>/
  models.py
  schemas/
    __init__.py
    base.py
    request.py
    response.py
  services/
    <feature>_service.py
  routes/
    __init__.py
    base.py
    admin.py
  repositories/
    <feature>_repository.py
  validators.py
  mappers.py
  constants.py
  exceptions.py
```

## Modular Monolith vs Layered-By-Type
| Criterion | Modular Monolith (Feature-based) | Layered-by-Type (global folders) |
|---|---|---|
| Feature cohesion | High: related files live together | Lower: feature files spread across folders |
| Onboarding speed | Faster per feature | Slower due to cross-folder tracing |
| Refactor safety | Better local impact | Higher cross-cutting ripple |
| Team ownership | Clear per module | Shared/global ownership ambiguity |
| Bootstrap complexity | Low with flat-first | Moderate, often over-abstracted early |

## Clean Architecture Without Over-Engineering
Use clean boundaries, not excessive layers:
- Keep `routes.py` for transport and validation concerns.
- Keep business rules in `service.py` (or `services/` after expansion).
- Keep persistence details in repository logic only when needed.
- Keep shared utilities minimal and generic.
- Do not let generic filenames absorb domain behavior just because they already exist.

This preserves architecture quality while keeping the bootstrap stage lightweight.

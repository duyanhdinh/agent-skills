---
name: backend-development
description: Implement robust backend services including APIs, domain logic, persistence, async workflows, and operational controls.
when_to_use: Use when building or modifying server-side features, APIs, integrations, or database-backed business logic.
tags:
  - backend
  - api
  - services
  - database
---

# Objective

Deliver backend features that are correct, observable, secure, and maintainable in production.

# Workflow

1. Define contract first: request/response, validation, and errors.
2. Implement domain logic independent from transport concerns.
3. Add data access behind repositories with clear transaction boundaries.
4. Add telemetry, retries, idempotency, and timeouts where needed.
5. Validate with unit, integration, and contract tests.

# Required

- Services own business rules and orchestration only.
- Any database access from application code must go through a repository or equivalent persistence abstraction.
- Do not execute ORM queries, raw SQL, session operations, or database client calls directly inside service classes.
- Keep transaction scope explicit at the repository or unit-of-work boundary.

# Best Practices

- Keep handlers thin; keep business logic testable.
- Inject repositories into services so domain logic stays persistence-aware without being persistence-coupled.
- Version API contracts intentionally.
- Prefer explicit error models over ad-hoc exceptions.
- Instrument critical paths with traces and metrics.

# Anti-Patterns

- Leaking persistence models directly to API consumers.
- Calling the database directly from services instead of a repository boundary.
- Silent retries without bounded backoff.
- Mixing validation and side effects.

# Resources

- Read `references/api-design-checklist.md` before implementing endpoints.

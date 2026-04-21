---
name: backend-development
description: Implement robust backend services including APIs, domain logic, persistence, async workflows, operational controls, server-side features, integrations, and database-backed business logic.
---

# Objective

Deliver backend features that are correct, observable, secure, and maintainable in production.

# Workflow

1. Define contract first: request/response, validation, and errors.
2. Run the placement check before implementation and name the owning layer.
3. Implement domain logic independent from transport and persistence concerns.
4. Add data access behind repositories with clear transaction boundaries.
5. Add telemetry, retries, idempotency, and timeouts where needed.
6. Validate with unit, integration, and contract tests.

# Required

- Services own business rules and orchestration only.
- Any database access from application code must go through a repository or equivalent persistence abstraction.
- Do not execute ORM queries, raw SQL, session operations, or database client calls directly inside service classes.
- Keep transaction scope explicit at the repository or unit-of-work boundary.
- Place new behavior in the layer that owns its reason to change, not in the nearest convenient file.
- Keep dependency direction one-way: transport -> application/service -> domain -> persistence interfaces; infrastructure implements interfaces and must not own business decisions.
- Do not put orchestration, workflow decisions, policy checks, notifications, external API calls, or other business side effects inside data mappers, query helpers, repositories, model files, constants, or generic utilities.

# Layer Ownership

- Transport handlers own protocol concerns: routing, authentication handoff, request parsing, response shaping, status codes, and transport-specific validation.
- Application services own use-case orchestration: sequencing, authorization decisions, idempotency decisions, transaction coordination, domain service calls, repository calls, and business side effects.
- Domain modules own business rules, invariants, policies, calculations, and state transitions that should be testable without framework or database dependencies.
- Repositories own persistence access: queries, commands, entity hydration, data mapping, and storage-specific error translation.
- Integration adapters own calls to external systems behind explicit interfaces; application services decide when those calls happen.
- Shared utilities own only framework-agnostic, low-level helpers with no domain policy, orchestration, persistence, or external side effects.

# Side-Effect Placement

- Put persistence side effects in repositories or units of work.
- Put external system side effects in integration adapters, triggered by application services.
- Put business side-effect decisions in application services or domain policies, not in persistence helpers.
- Put telemetry side effects near the operation being measured without changing dependency direction.
- Keep pure mapping, parsing, formatting, and constants free of writes, network calls, queues, emails, event publication, and workflow decisions.

# Dependency Direction Invariants

- Higher-level policy may depend on abstractions, not concrete infrastructure.
- Domain code must not import transport frameworks, ORM sessions, database clients, job queues, or HTTP clients.
- Repositories must not call services, publish business events, invoke workflows, or decide user-visible behavior.
- Transport handlers must not bypass services to call repositories for use cases with business rules.
- Generic helpers must not import feature services, repositories, models with persistence behavior, or integration clients.
- When a change requires reverse dependency, introduce an interface, event, callback boundary, or move the behavior to the owning layer.

# Placement Check

Before implementation, answer these checks in the plan or working notes:

- What behavior is being added or changed?
- Which layer owns the primary reason this behavior changes?
- Does the target file already own that responsibility by name and existing code?
- What side effects can occur, and which layer should trigger each one?
- What dependencies will the code import, and do they follow the allowed direction?
- Would this still be the right location if the storage, transport, or external provider changed?
- If the answer is unclear, create or reuse a dedicated domain-named module instead of adding to a generic helper.

# PR/Self-Review Gate

Before finishing, reject the change or revise placement if any answer is "yes":

- Did orchestration or business side-effect decisions land in persistence, mapper, model, constants, helper, or utility code?
- Did a lower layer import or call a higher layer?
- Did a handler bypass the service/application layer for a business use case?
- Did a generic file become the default home for feature-specific behavior?
- Did a repository do more than persistence access, mapping, storage errors, or transaction participation?
- Are tests forced to mock unrelated infrastructure because logic is in the wrong layer?

# Best Practices

- Keep handlers thin; keep business logic testable.
- Inject repositories into services so domain logic stays persistence-aware without being persistence-coupled.
- Version API contracts intentionally.
- Prefer explicit error models over ad-hoc exceptions.
- Instrument critical paths with traces and metrics.

# Anti-Patterns

- Leaking persistence models directly to API consumers.
- Calling the database directly from services instead of a repository boundary.
- Triggering workflow, notification, authorization, or integration side effects from query helpers or repositories.
- Adding feature behavior to a file because it is already imported nearby.
- Silent retries without bounded backoff.
- Mixing validation and side effects.

# Resources

- Read `references/api-design-checklist.md` before implementing endpoints.

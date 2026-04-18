---
name: common-coding-standards
description: Enforce consistent coding standards for readability, maintainability, testability, and long-term code health across teams.
when_to_use: Use when creating team conventions, reviewing style quality, or standardizing project-level engineering practices.
tags:
  - coding-standards
  - maintainability
  - quality
  - conventions
---

# Objective

Keep codebases coherent and easy to evolve by applying clear engineering standards.

# Workflow

1. Define naming, structure, and formatting conventions.
2. Define error handling and logging expectations.
3. Define testing and documentation requirements.
4. Automate checks in lint, format, and CI.
5. Review deviations and tighten standards iteratively.

# Required

- Do not create god objects, god functions, or god files.
- Each class, function, and file must have a narrow, explicit responsibility.
- Split code when a unit starts accumulating unrelated responsibilities, branching by many concerns, or becoming the default place for new logic.
- Prefer cohesive modules with clear boundaries over central utility blobs or catch-all managers.
- Do not default to `constants`, `helpers`, `utils`, or similarly generic files for feature logic.
- Create a dedicated file when logic has a stable domain role such as validation, mapping, policy, parsing, formatting, orchestration, or integration.
- Treat generic catch-all files as a last resort for truly cross-cutting, low-complexity, framework-agnostic code only.
- If a generic file starts mixing unrelated concerns, split it immediately into domain-named files.
- Reject implementations that hide business rules inside `constants.py`, `helpers.py`, `utils.py`, `service.py`, or other ambiguous filenames.
- Prefer names that reveal responsibility, for example `user_policy.py`, `invoice_formatter.py`, `payload_validator.py`, or `token_parser.py`.

# File Boundary Rules

- `constants.*` may contain only immutable values, enums, and configuration-like declarations for one bounded concern.
- `helpers.*` is not a default destination for leftover code; use it only for a very small set of closely related, non-domain-specific helpers.
- `utils.*` must not contain feature behavior, orchestration, persistence, validation policy, or branching business rules.
- When code answers different reasons to change, split by reason to change instead of grouping by convenience.
- When a file name would require a broad explanation such as "misc", "common", or "helper", rename and split it.

# Best Practices

- Favor explicitness over cleverness.
- Keep functions focused and side effects clear.
- Keep files small enough to remain scannable and safe to change.
- Align abstractions with domain language.
- Document non-obvious decisions in code comments or ADRs.

# Anti-Patterns

- Creating catch-all files such as `utils.py`, `helpers.py`, or `service.py` that absorb unrelated logic.
- Building large functions that mix orchestration, validation, persistence, transformation, and side effects.
- Using style rules with no enforcement automation.
- Allowing widespread exceptions to standards.
- Prioritizing micro-optimizations over readability.

# Resources

- Read `references/style-and-quality-checklist.md`.

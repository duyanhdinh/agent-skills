---
name: oop-design-principles
description: Apply SOLID, DRY, and GoF design patterns to improve code structure, extensibility, and maintainability.
when_to_use: Use when refactoring tangled code, designing new modules, reviewing architecture quality, or selecting object-oriented design patterns.
tags:
  - solid
  - dry
  - gof
  - design-patterns
  - maintainability
---

# Objective

Produce code that is easier to change safely by applying practical OOP design principles and pattern choices with explicit trade-offs.

# Workflow

1. Identify current pain points: rigidity, duplication, high coupling, unclear responsibilities.
2. Map each issue to principle-level fixes (SOLID/DRY) before introducing patterns.
3. Choose the smallest fitting GoF pattern only when it removes a real constraint.
4. Implement incrementally with behavior-preserving refactors and tests.
5. Validate design quality through coupling/cohesion checks and change-scenario review.

# Best Practices

- Prefer composition over inheritance when evolution paths are uncertain.
- Apply DRY to behavior and business rules; avoid over-abstracting trivial duplication.
- Use interfaces/abstractions only where substitution is needed.
- Document why a pattern is chosen and what simpler options were rejected.

# Anti-Patterns

- Introducing patterns without concrete forces (premature abstraction).
- Treating SOLID as rigid rules instead of trade-off heuristics.
- Using inheritance trees to share unrelated behavior.
- Copy-pasting logic across services instead of extracting stable policies.

# Resources

- Read `references/solid-dry-gof-playbook.md`.
- For GoF catalog and examples, use `https://refactoring.guru/design-patterns/catalog`.

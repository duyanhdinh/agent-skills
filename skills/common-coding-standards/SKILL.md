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

# Best Practices

- Favor explicitness over cleverness.
- Keep functions focused and side effects clear.
- Align abstractions with domain language.
- Document non-obvious decisions in code comments or ADRs.

# Anti-Patterns

- Using style rules with no enforcement automation.
- Allowing widespread exceptions to standards.
- Prioritizing micro-optimizations over readability.

# Resources

- Read `references/style-and-quality-checklist.md`.

---
name: testing-strategy
description: Design and operationalize pragmatic testing strategies across unit, integration, contract, and end-to-end levels.
when_to_use: Use when defining test plans, improving confidence before releases, or fixing weak coverage in critical paths.
tags:
  - testing
  - quality
  - reliability
  - strategy
---

# Objective

Create a balanced test portfolio that catches defects early and protects business-critical behavior.

# Workflow

1. Map critical user and system flows.
2. Choose test levels per risk and feedback speed.
3. Define deterministic fixtures, mocks, and test data strategy.
4. Add CI gates, flake controls, and failure triage workflow.
5. Track coverage of behavior, not just lines.

# Best Practices

- Test contracts at service boundaries.
- Keep end-to-end tests focused and stable.
- Enforce fast unit tests as the default.
- Add non-functional tests for performance and reliability.

# Anti-Patterns

- Depending only on end-to-end tests.
- Treating coverage percentage as the only metric.
- Keeping flaky tests as optional warnings.

# Resources

- Read `references/test-pyramid-and-honeycomb.md` for model selection.
- Use `templates/test-plan-template.md` to produce test plans.
- Run `scripts/generate-test-matrix.py` to build scenario matrices.

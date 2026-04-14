---
name: frontend-development
description: Build accessible, responsive, and performant user interfaces with maintainable state management and reliable UX behavior.
when_to_use: Use when creating or refactoring web UI features, interaction flows, or frontend architecture.
tags:
  - frontend
  - ui
  - accessibility
  - performance
---

# Objective

Ship user-facing features that are usable, fast, accessible, and resilient to edge cases.

# Workflow

1. Define user journey, states, and acceptance criteria.
2. Build semantic UI structure and accessible interactions.
3. Implement state flow and data fetching boundaries.
4. Handle loading, empty, error, and retry states.
5. Validate with UI tests, accessibility checks, and performance budgets.

# Best Practices

- Build components around behaviors, not visuals alone.
- Keep design tokens centralized.
- Use progressive enhancement where possible.
- Set measurable performance goals early.

# Anti-Patterns

- Shipping inaccessible controls or missing keyboard support.
- Coupling view components to API shapes directly.
- Ignoring mobile and low-bandwidth scenarios.

# Resources

- Read `references/ui-performance-checklist.md` during implementation and review.

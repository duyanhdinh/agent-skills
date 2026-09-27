---
name: design-mode
description: Use when choosing an approach, architecture, component boundary, interface, or user flow before implementation.
---

# Design Mode

- You MUST define the decision, desired outcome, and constraints. You MUST separate established requirements from choices still open.
- You MUST inspect existing code, interfaces, and user flows. You SHOULD prefer an incremental approach that fits the repository; you MUST justify any new boundary or pattern with a current need.
- You MUST compare alternatives when more than one viable option exists. If constraints leave only one, you MUST explain why without inventing a second option.
- You MUST evaluate relevant trade-offs such as complexity, coupling, usability, accessibility, failure handling, migration cost, and reversibility.
- For UI decisions, you MUST describe affected interactions and states using existing components and design conventions where suitable. You MUST NOT prescribe a frontend framework or backend layering scheme by default.
- You MUST identify compatibility risks and any irreversible step; you MUST provide mitigation when needed. You MUST scale the detail to the impact of the decision.
- You MUST recommend a concrete approach and how to verify it. You MUST move to implementation only when authorized by the request; you MUST ask about unresolved choices that materially change the outcome.

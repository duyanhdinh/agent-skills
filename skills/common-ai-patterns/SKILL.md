---
name: common-ai-patterns
description: Apply reusable AI solution patterns for classification, extraction, generation, retrieval, routing, and agentic workflows.
when_to_use: Use when choosing implementation patterns for AI features and avoiding one-off, fragile designs.
tags:
  - ai-patterns
  - architecture
  - reuse
  - design
---

# Objective

Accelerate delivery by selecting proven AI patterns that fit problem constraints.

# Workflow

1. Classify problem type and quality requirements.
2. Select matching pattern and define acceptance metrics.
3. Implement minimal vertical slice.
4. Add evaluation and observability loops.
5. Harden for production with scaling and safety controls.

# Best Practices

- Start from simplest pattern that can work.
- Keep pattern decisions explicit and testable.
- Combine patterns only when one pattern cannot satisfy constraints.
- Revisit pattern choice as data and usage evolve.

# Anti-Patterns

- Jumping to agents for simple extraction tasks.
- Combining many model stages without observability.
- Ignoring fallback paths for uncertain outputs.

# Resources

- Read `references/pattern-catalog.md`.

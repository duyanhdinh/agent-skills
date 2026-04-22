---
name: architecture-system-design
description: Design scalable, reliable system architectures with clear component boundaries, data flow, and operational trade-offs.
when_to_use: Use when planning a new platform, redesigning core systems, or making architecture decisions with long-term impact.
tags:
  - architecture
  - system-design
  - scalability
  - reliability
---

# Objective

Produce architecture decisions that balance simplicity, scale, resilience, and delivery speed.

# Workflow

1. Capture requirements, constraints, and quality attributes.
2. Define context, containers, components, and interfaces.
3. Evaluate trade-offs with explicit decision records.
4. Plan observability, failure modes, and recovery paths.
5. Validate design with load, reliability, and cost assumptions.

# Best Practices

- State assumptions and unknowns explicitly.
- Separate synchronous and asynchronous paths clearly.
- Treat data ownership and schema evolution as first-class concerns.
- Use ADRs for non-trivial decisions.

# Anti-Patterns

- Designing from tools before requirements.
- Ignoring failure scenarios and backpressure.
- Centralizing all logic in one service.

# Resources

- Use `templates/system-design-doc-template.md` for design artifacts.

---
name: ai-agent-design
description: Design AI agents with clear control loops, tool orchestration, state boundaries, and safety guardrails.
when_to_use: Use when implementing autonomous or semi-autonomous AI workflows with planning, tool use, and iterative execution.
tags:
  - agents
  - orchestration
  - tools
  - autonomy
---

# Objective

Create predictable, inspectable agents that complete tasks safely and efficiently.

# Workflow

1. Define goal, constraints, and success criteria.
2. Design the control loop (plan, act, observe, reflect).
3. Specify tool contracts, permissions, and failure handling.
4. Define memory scope and retention policy.
5. Add human-in-the-loop checkpoints for risky actions.

# Best Practices

- Keep agent loops shallow and bounded.
- Prefer deterministic tool outputs over free text.
- Log reasoning summaries and action traces.
- Add stop conditions for run-away loops.

# Anti-Patterns

- Giving unrestricted tool access by default.
- Persisting sensitive context longer than needed.
- Allowing unbounded recursive planning.

# Resources

- Read `references/agent-loop-pattern.md` for orchestration patterns.

# Prompt Patterns

## Direct Instruction Pattern

Use for deterministic transformations.

Template:

- Task
- Constraints
- Output schema

## Few-Shot Pattern

Use when formatting or reasoning style needs examples.

Rules:

- Keep examples short.
- Cover edge cases.
- Avoid contradictory examples.

## Tool-Use Pattern

Use when model must call tools.

Rules:

- Specify when to call each tool.
- Define strict output contract for tool arguments.
- Add retry and fallback behavior.

## Guardrail Pattern

Use for sensitive or policy-constrained tasks.

Rules:

- Define refusal boundaries.
- Define uncertainty responses.
- Require citation from provided context when needed.

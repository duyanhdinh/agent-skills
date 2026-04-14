# Agent Loop Pattern

## Standard Loop

1. Plan: decompose objective into bounded tasks.
2. Act: execute the next action or tool call.
3. Observe: parse outputs and environment signals.
4. Reflect: check progress, risks, and stop conditions.
5. Repeat or stop.

## Guardrails

- Max step budget.
- Max retry budget per tool.
- Sensitive action confirmation.
- Explicit exit when confidence is low.

## Telemetry

- Task ID
- Step number
- Tool name
- Outcome
- Error class

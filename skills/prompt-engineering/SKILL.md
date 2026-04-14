---
name: prompt-engineering
description: Design reliable prompts, instruction hierarchies, and structured outputs for LLM-powered applications and automation.
when_to_use: Use when creating or improving prompts, reducing hallucination risk, or building repeatable LLM workflows.
tags:
  - prompts
  - llm
  - reliability
  - structured-output
---

# Objective

Produce prompts that are robust, testable, and aligned with clear output contracts.

# Workflow

1. Define task objective, constraints, and output schema.
2. Choose prompt pattern (role, few-shot, chain-of-thought policy, tool-use).
3. Add grounding context and explicit refusal boundaries.
4. Evaluate with representative and adversarial cases.
5. Iterate with versioning and regression checks.

# Best Practices

- Write deterministic output instructions.
- Separate system policy from task content.
- Keep examples short and diverse.
- Add explicit uncertainty behavior.

# Anti-Patterns

- Prompting with ambiguous goals.
- Overloading one prompt with multiple conflicting tasks.
- Shipping prompts without an evaluation suite.

# Resources

- Read `references/prompt-patterns.md`.
- Use `templates/prompt-spec-template.md`.
- Run `scripts/prompt-lint.py` for structural checks.

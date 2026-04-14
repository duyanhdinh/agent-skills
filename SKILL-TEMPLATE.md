---
name: skill-name
description: Clear summary of what this skill does.
when_to_use: Use when these exact triggers or contexts are present.
tags:
  - domain
  - workflow
  - tools
---

# Objective

State the concrete outcome this skill should produce.

# Workflow

1. Confirm scope, constraints, and acceptance criteria.
2. Select the minimal implementation path.
3. Execute with deterministic steps and checkpoints.
4. Validate with tests or measurable verification.
5. Report outputs, risks, and next actions.

# Best Practices

- Keep instructions specific and executable.
- Prefer reusable assets for repeated work.
- Include commands, snippets, or templates that reduce ambiguity.
- Define quality gates before implementation.

# Anti-Patterns

- Starting implementation before scope is clear.
- Mixing unrelated concerns in one workflow.
- Skipping validation or evidence collection.
- Writing generic guidance with no actionable steps.

# Resources

- `references/`: domain notes, checklists, decision criteria.
- `templates/`: reusable docs, forms, boilerplates.
- `scripts/`: deterministic automation helpers.

# Structure

```text
skill-name/
|-- SKILL.md
|-- references/        # optional
|-- templates/         # optional
`-- scripts/           # optional
```

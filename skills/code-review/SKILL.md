---
name: code-review
description: Perform high-signal code reviews for pull requests, risky changes, and production-readiness, focused on correctness, regressions, security, maintainability, architectural placement, and test adequacy.
---

# Objective

Identify and communicate defects, risks, and missing validations before code is merged.

# Workflow

1. Understand change intent and scope from diff plus context.
2. Assess correctness, edge cases, and regression risks.
3. Check architectural placement: layer ownership, side-effect location, and dependency direction.
4. Review tests for coverage depth and failure behavior.
5. Classify findings by severity and include evidence.
6. Propose concrete remediation and verification steps.

# Required

- Treat misplaced behavior as a correctness and maintainability risk, not only style feedback.
- Flag orchestration, workflow decisions, business side effects, or policy checks placed in persistence helpers, mappers, model files, constants, or generic utilities.
- Flag dependencies that point from lower-level modules to higher-level modules.
- Verify handlers, services, domain modules, repositories, adapters, and utilities each keep their expected responsibility.
- Ask whether the implementation would still be correctly placed if transport, storage, or an external provider changed.

# Best Practices

- Prioritize bugs and behavioral regressions over style.
- Anchor each finding to file and line.
- Include reasoning and expected impact.
- Call out missing tests explicitly.

# Anti-Patterns

- Approving based only on readability.
- Reporting vague concerns with no reproduction path.
- Mixing critical and cosmetic feedback without severity labels.

# Resources

- Use `references/severity-model.md` for issue classification.
- Use `references/review-checklist.md` for systematic review.
- Use `templates/review-report-template.md` for review output.
- Run `scripts/changed-files.ps1` to focus on touched files.

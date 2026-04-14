---
name: code-review
description: Perform high-signal code reviews focused on correctness, regressions, security, maintainability, and test adequacy.
when_to_use: Use when reviewing pull requests, auditing risky changes, or assessing production-readiness before merge.
tags:
  - review
  - quality
  - risk
  - governance
---

# Objective

Identify and communicate defects, risks, and missing validations before code is merged.

# Workflow

1. Understand change intent and scope from diff plus context.
2. Assess correctness, edge cases, and regression risks.
3. Review tests for coverage depth and failure behavior.
4. Classify findings by severity and include evidence.
5. Propose concrete remediation and verification steps.

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

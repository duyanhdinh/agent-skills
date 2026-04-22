---
name: git-workflow
description: Apply consistent Git practices for branching, commit hygiene, pull requests, release tags, and collaboration safety.
when_to_use: Use when defining team Git conventions, preparing pull requests, or managing release and hotfix flows.
tags:
  - git
  - collaboration
  - release
  - version-control
---

# Objective

Improve collaboration velocity and traceability while reducing merge risk and release friction.

# Workflow

1. Choose a branch strategy aligned to release cadence.
2. Enforce commit message conventions and atomic commits.
3. Use pull-request templates and required checks.
4. Tag releases and maintain changelog inputs.
5. Manage hotfix and rollback flows explicitly.

# Best Practices

- Keep commits focused on one concern.
- Rebase or merge predictably based on team policy.
- Require green CI before merge.
- Protect main branch with review gates.

# Anti-Patterns

- Large mixed commits with unrelated changes.
- Force pushes to shared stable branches.
- Merging without test and review evidence.

# Resources

- Read `references/commit-convention.md`.
- Use `templates/pull-request-template.md`.

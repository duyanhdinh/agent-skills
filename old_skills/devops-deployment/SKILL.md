---
name: devops-deployment
description: Build dependable CI/CD and deployment workflows with safety checks, observability, rollback, and incident readiness.
when_to_use: Use when creating or improving build pipelines, release automation, deployment runbooks, and operations controls.
tags:
  - devops
  - deployment
  - ci-cd
  - operations
---

# Objective

Ship changes safely and repeatedly with minimal downtime and fast recovery.

# Workflow

1. Define build, test, package, and deploy stages.
2. Add environment promotion and approval policies.
3. Add health checks, canary/blue-green options, and rollback.
4. Integrate logs, metrics, traces, and alerts.
5. Run release drills and post-deploy verification.

# Best Practices

- Keep deployment artifacts immutable.
- Separate config from code with secure secret management.
- Automate rollback criteria.
- Track deployment lead time and change failure rate.

# Anti-Patterns

- Manual hotfixes without audit trail.
- Sharing mutable runtime state across deploys.
- Deploying without observability baselines.

# Resources

- Follow `references/deployment-checklist.md`.
- Use `templates/release-runbook-template.md` for standardized releases.

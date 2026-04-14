---
name: project-scaffold
description: Create production-ready project foundations, repository layout, baseline tooling, and initial docs for new software projects.
when_to_use: Use when starting a new project, standardizing repository structure, or creating a repeatable foundation for teams.
tags:
  - scaffold
  - repository
  - bootstrap
  - standards
---

# Objective

Create a clean, reproducible project foundation that is easy to develop, test, review, and deploy.

# Workflow

1. Confirm runtime, framework, package manager, and deployment target.
2. Generate a minimal but complete folder layout.
3. Add quality gates: lint, format, test, and CI stubs.
4. Add developer documentation and contribution standards.
5. Verify bootstrap commands run successfully.

# Best Practices

- Keep the first scaffold small and composable.
- Separate source code, tests, configs, and docs clearly.
- Include environment examples, not real secrets.
- Add Makefile or scripts for common commands.

# Anti-Patterns

- Overengineering before first feature delivery.
- Committing environment-specific artifacts.
- Missing onboarding steps for new contributors.

# Resources

- Read `references/stack-selection.md` for decision criteria.
- Use `templates/project-brief-template.md` to lock scope early.
- Use `templates/README.template.md` as initial README.
- Run `scripts/init_project.ps1` for deterministic setup.

---
name: security-best-practices
description: Integrate secure-by-default engineering practices including threat modeling, input validation, secret management, and dependency hygiene.
when_to_use: Use when implementing features that handle user input, authentication, data access, or any sensitive workflows.
tags:
  - security
  - secure-coding
  - threat-modeling
  - compliance
---

# Objective

Reduce exploitability and security regressions through systematic secure engineering controls.

# Workflow

1. Model trust boundaries and threat scenarios.
2. Validate and sanitize all external inputs.
3. Enforce authentication, authorization, and least privilege.
4. Manage secrets, encryption, and key rotation safely.
5. Run security scans and review findings before release.

# Best Practices

- Default-deny where possible.
- Use parameterized queries and safe serializers.
- Track and patch vulnerable dependencies quickly.
- Log security events with tamper-aware retention.

# Anti-Patterns

- Hardcoding secrets in code or CI config.
- Relying on client-side validation alone.
- Skipping authorization checks on internal endpoints.

# Resources

- Use `references/threat-modeling-checklist.md` for design and review.

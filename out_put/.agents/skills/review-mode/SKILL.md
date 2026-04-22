---
name: review-mode
description: Use when reviewing code, pull requests, diffs, or implementation plans for correctness, security, data loss, regressions, operational risk, and test coverage.
---

# Review Mode

- You MUST report findings only when they create correctness, security, data loss, regression, or operational risk.
- You MUST rank every finding by severity before discussing secondary concerns.
- You MUST cite the exact location, failure scenario, user impact, and remediation for each finding.
- You MUST NOT include style-only, preference-only, or speculative comments as findings.
- You MUST verify whether tests cover the risky path before treating coverage as adequate.
- You MUST call out any critical path you could not inspect as residual risk.
- You MUST distinguish confirmed defects from questions that need author clarification.
- Findings MUST include severity, location, impact, and concrete remediation.
- Severity MUST use only Critical, High, Medium, or Low.
- Findings MUST prioritize correctness, security, data loss, regressions, and operational risk over style preferences.
- You MUST NOT report style-only review comments as findings unless they create a concrete maintainability or correctness risk.

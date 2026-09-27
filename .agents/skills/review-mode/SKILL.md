---
name: review-mode
description: Use when reviewing code, changes, or implementation plans for concrete defects, regressions, and verification gaps.
---

# Review Mode

- You MUST establish the review scope and intended behavior. You MUST inspect relevant callers, consumers, and repository conventions before judging a change.
- You MUST report evidence-backed defects or risks affecting correctness, security, data integrity, compatibility, usability, accessibility, or operation. You MUST exclude personal style preferences and unsupported scenarios.
- For UI changes, you MUST consider interactions, state transitions, responsive layout, and accessibility where affected. You MUST distinguish a functional or specified visual regression from a subjective design preference.
- You MUST rank findings as Critical, High, Medium, or Low based on impact and likelihood. You MUST include the exact location, triggering condition, user impact, and a concrete correction for each finding.
- You MUST check whether tests or other validation exercise the risky behavior. You MUST identify concrete gaps without claiming that passing checks prove untested paths.
- You MUST separate confirmed findings from questions requiring clarification. You MUST state any material paths you could not inspect or verify.
- You MUST present findings first, then a brief verification summary and residual risks. If no findings are supported, you MUST say so without implying the change is risk-free. You MUST NOT apply fixes unless requested.

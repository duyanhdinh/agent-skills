---
name: evaluation-and-testing-ai
description: Build rigorous evaluation frameworks for AI systems including offline tests, online metrics, and regression gating.
when_to_use: Use when validating AI quality, comparing model or prompt variants, or enforcing release gates for AI behavior.
tags:
  - evaluation
  - ai-testing
  - metrics
  - regression
---

# Objective

Create repeatable AI evaluation that detects quality regressions before production impact.

# Workflow

1. Define task taxonomy and failure classes.
2. Build benchmark datasets with gold labels or rubric criteria.
3. Select metrics for quality, safety, latency, and cost.
4. Run baseline and candidate comparisons.
5. Set pass/fail thresholds and release policies.

# Best Practices

- Separate evaluation by use case segment.
- Track both aggregate and tail failure behavior.
- Include red-team and adversarial cases.
- Record exact model, prompt, and dataset versions.

# Anti-Patterns

- Relying on anecdotal spot checks only.
- Changing benchmarks without version control.
- Optimizing one metric while regressing safety.

# Resources

- Read `references/llm-eval-metrics.md`.
- Use `templates/eval-plan-template.md`.
- Run `scripts/score_eval_results.py` for basic score summaries.

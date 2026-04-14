---
name: mlops-deployment
description: Operationalize machine learning systems with reproducible training, model registry, deployment pipelines, and monitoring.
when_to_use: Use when moving ML models from experimentation to reliable production serving.
tags:
  - mlops
  - model-serving
  - monitoring
  - lifecycle
---

# Objective

Deliver ML models with traceability, reproducibility, and controlled production risk.

# Workflow

1. Standardize datasets, feature definitions, and training configs.
2. Version models, metadata, and evaluation artifacts.
3. Build CI/CD for training and serving paths.
4. Deploy with staged rollout and rollback triggers.
5. Monitor accuracy, drift, latency, and cost.

# Best Practices

- Separate offline metrics from online business KPIs.
- Keep feature engineering consistent across train and serve.
- Automate lineage capture for compliance.
- Define retraining policy by drift thresholds.

# Anti-Patterns

- Promoting models without reproducible training runs.
- Ignoring data drift until incidents occur.
- Coupling model and feature pipelines too tightly.

# Resources

- Use `references/model-release-checklist.md`.

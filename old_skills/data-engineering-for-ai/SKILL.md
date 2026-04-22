---
name: data-engineering-for-ai
description: Build reliable data pipelines for AI workloads with ingestion, transformation, quality enforcement, and governance controls.
when_to_use: Use when preparing training, evaluation, or retrieval datasets from heterogeneous sources.
tags:
  - data-engineering
  - pipelines
  - data-quality
  - governance
---

# Objective

Deliver trustworthy, well-modeled data products that support AI systems at scale.

# Workflow

1. Define source contracts and ingestion cadence.
2. Build transformations with schema and lineage tracking.
3. Enforce quality checks, anomaly detection, and SLAs.
4. Partition and optimize storage for downstream consumers.
5. Monitor freshness, completeness, and cost.

# Best Practices

- Treat datasets as versioned products.
- Add data contracts between producers and consumers.
- Use idempotent jobs and replay support.
- Track PII and policy tags through pipeline stages.

# Anti-Patterns

- Silent schema changes in source systems.
- Mixing raw and curated layers.
- Unbounded backfills without resource controls.

# Resources

- Read `references/data-quality-slos.md`.

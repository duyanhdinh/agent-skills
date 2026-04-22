---
name: vector-database
description: Design and operate vector database systems for semantic search, filtering, hybrid retrieval, and embedding lifecycle management.
when_to_use: Use when implementing or optimizing embedding storage and retrieval layers in AI applications.
tags:
  - vector-db
  - embeddings
  - retrieval
  - indexing
---

# Objective

Provide fast, accurate, and cost-efficient semantic retrieval for AI products.

# Workflow

1. Define retrieval tasks and relevance criteria.
2. Select index type, distance metric, and metadata model.
3. Implement ingestion, upsert, and re-embedding strategy.
4. Tune recall/latency trade-offs with benchmarks.
5. Add multi-tenant isolation and lifecycle retention policies.

# Best Practices

- Keep embedding model version with every vector.
- Use hybrid search for ambiguous queries.
- Filter aggressively before reranking.
- Rebuild indexes with controlled cutovers.

# Anti-Patterns

- Mixing embeddings from incompatible models.
- Ignoring stale vectors after content updates.
- Querying without metadata constraints in shared environments.

# Resources

- Read `references/indexing-and-retrieval.md`.

---
name: rag-implementation
description: Implement retrieval-augmented generation pipelines with robust ingestion, chunking, retrieval, and grounded answer generation.
when_to_use: Use when building AI systems that must answer using external knowledge bases or enterprise documents.
tags:
  - rag
  - retrieval
  - llm
  - knowledge-base
---

# Objective

Build a high-precision retrieval pipeline that improves factuality and traceability of model outputs.

# Workflow

1. Define document sources and freshness requirements.
2. Build ingestion and chunking strategy with metadata.
3. Select embedding model and indexing approach.
4. Tune retrieval (k, rerank, filters, hybrid search).
5. Implement answer grounding with citations and fallback behavior.

# Best Practices

- Keep chunk size aligned to query intent.
- Store source metadata for attribution and filtering.
- Evaluate retrieval and answer quality separately.
- Monitor drift in corpus and embeddings.

# Anti-Patterns

- Treating vector search score as truth.
- Skipping metadata filters for multi-tenant data.
- Mixing unrelated corpora in one undifferentiated index.

# Resources

- Read `references/rag-architecture-patterns.md`.
- Use `templates/rag-evaluation-template.md`.

# RAG Architecture Patterns

## Pattern 1: Single-Stage Retrieval

Embed query, retrieve top-k chunks, generate with citations.

Use when corpus is small to medium and latency target is strict.

## Pattern 2: Hybrid Retrieval + Rerank

Combine keyword + vector retrieval, then rerank before generation.

Use when precision is critical and corpus vocabulary is mixed.

## Pattern 3: Multi-Hop Retrieval

Retrieve iteratively across sources to answer compositional queries.

Use when user queries require cross-document reasoning.

## Baseline Controls

- Source attribution in final response.
- Metadata filters for tenant, time, and permissions.
- Fallback behavior for low-confidence retrieval.

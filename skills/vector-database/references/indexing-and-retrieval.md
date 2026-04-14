# Indexing and Retrieval Notes

## Index Choice

- HNSW: strong recall/latency balance for many workloads.
- IVF variants: useful for very large datasets with tuned probes.
- Flat index: best for small datasets or exact search requirements.

## Retrieval Tuning

- Start with conservative `k`, then tune with evaluation.
- Add metadata filters before vector search when possible.
- Use reranking for precision-sensitive tasks.

## Lifecycle

- Track embedding model versions.
- Re-embed changed or stale content on schedule.
- Archive or delete vectors by retention policy.

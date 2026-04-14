# API Design Checklist

- Endpoint purpose is single-responsibility.
- Request schema has strict validation rules.
- Response schema is versioned and documented.
- Error model is explicit with machine-readable codes.
- Idempotency strategy exists for mutation endpoints.
- Pagination and filtering are consistent.
- Authentication and authorization are defined.
- Rate limits and abuse controls are specified.
- Observability fields (request ID, latency, error class) are present.

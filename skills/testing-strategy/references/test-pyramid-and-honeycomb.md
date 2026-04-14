# Test Pyramid and Honeycomb Guidance

Use a blended model:

- Unit tests: fast checks for pure logic and component behavior.
- Integration tests: verify module boundaries and data contracts.
- Contract tests: ensure service-to-service compatibility.
- End-to-end tests: validate critical user journeys.
- Non-functional tests: performance, resiliency, and security behavior.

Prefer many deterministic lower-level tests and fewer high-value end-to-end tests.

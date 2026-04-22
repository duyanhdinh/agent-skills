# Scope Control

- You MUST define the task boundary from the user's request before changing files.
- You MUST modify only files required to satisfy the accepted task boundary.
- You MUST keep generated artifacts limited to the requested structure and count.
- You MUST treat behavior preservation as part of scope: new behavior MUST NOT silently alter existing flows, defaults, permissions, outputs, or integrations.
- You MUST ask for approval before expanding scope to new features, migrations, redesigns, or broad rewrites.
- You MUST treat unrelated cleanup, optimization, modernization, and style fixes as out of scope unless requested.
- Do NOT add convenience features that were not requested.
- Do NOT make silent improvements outside the task boundary, even when they appear low-risk.
- Do NOT change formatting, naming, or architecture outside the touched requirement.
- Do NOT replace working implementations when a targeted fix is sufficient.
- Do NOT perform destructive operations unless explicitly requested or approved.
- Do NOT combine application behavior changes with schema, data, configuration, or deployment changes unless the task requires the combined release.
- You MUST report any out-of-scope issue separately without fixing it automatically.
- You MUST keep configuration, secrets, and environment-specific values separate from code changes and committed defaults.
- You MUST identify rollback or mitigation for release-impacting changes, including how to disable the change or restore the previous version.
- You MUST include a health check, smoke test, or equivalent verification step for deployment-impacting changes.
- You MUST treat schema and data migrations as high-risk scope changes that require backward compatibility, reversible rollout planning, and data preservation checks.
- You MUST include rollback or mitigation steps for high-risk changes.

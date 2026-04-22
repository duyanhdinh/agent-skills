# Scope Control

- You MUST define the task boundary from the user's request before changing files.
- You MUST modify only files required to satisfy the accepted task boundary.
- You MUST keep generated artifacts limited to the requested structure and count.
- You MUST ask for approval before expanding scope to new features, migrations, redesigns, or broad rewrites.
- You MUST treat unrelated cleanup, optimization, modernization, and style fixes as out of scope unless requested.
- Do NOT add convenience features that were not requested.
- Do NOT make silent improvements outside the task boundary, even when they appear low-risk.
- Do NOT change formatting, naming, or architecture outside the touched requirement.
- Do NOT replace working implementations when a targeted fix is sufficient.
- Do NOT perform destructive operations unless explicitly requested or approved.
- You MUST report any out-of-scope issue separately without fixing it automatically.
- You MUST include rollback or mitigation steps for high-risk changes.

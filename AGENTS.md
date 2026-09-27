# AGENTS.md

These rules apply across languages and project types, including backend services, frontend applications, libraries, and command-line tools. You MUST follow the repository's actual architecture and conventions.

`MUST` and `MUST NOT` are mandatory. A conditional requirement is mandatory whenever its condition applies. `SHOULD` is a recommendation; departures require a task-specific reason. `MAY` grants an option within the authorized scope. Missing tools or evidence do not waive a requirement: report the limitation and do not claim unverified completion.

## Understand the Task

- You MUST identify the requested outcome, scope, and constraints; you MUST briefly restate them when the task has multiple requirements.
- You MUST inspect relevant files and available evidence before deciding. You MUST NOT invent requirements, APIs, behavior, or verification results.
- You MUST look for missing information in the repository first. You MUST ask when an unresolved choice materially affects correctness, user-visible behavior, scope, or an irreversible action. You MUST continue independent work while waiting.
- For minor, reversible choices, you MUST follow established conventions. You MUST state consequential assumptions and unresolved uncertainty; you MUST verify time-sensitive claims before relying on them.
- You MUST keep planning proportional to the task. For substantial changes, you MUST identify the affected components and how success will be checked before editing.
- You MUST report conflicting requirements and pause only the affected work when they cannot be reconciled under the instruction hierarchy.

## Keep Changes Focused

- You MUST make the smallest complete change that satisfies the request. You MUST preserve behavior, contracts, and user experience outside the requested change.
- You MUST leave unrelated user changes intact. You MUST NOT add unrelated cleanup, features, dependencies, or infrastructure; you MUST report separate issues without fixing them automatically.
- You MUST ask before expanding beyond the authorized scope. Existing authorization remains valid; you MUST NOT request it again for routine steps within that scope.
- You MUST NOT perform destructive operations without explicit authorization. For migrations or other high-risk changes, you MUST plan compatibility, data preservation, and rollback or mitigation before execution.

## Work with the Repository

- You MUST read applicable instructions and existing code before editing. You MUST follow local naming, dependencies, tools, and framework idioms.
- You MUST place behavior in the component or module responsible for it. You MUST respect existing boundaries and dependency direction; you MUST NOT impose a fixed layering scheme or move behavior into generic helpers because ownership is unclear.
- You MUST reuse suitable code and UI components. You MUST introduce abstractions or dependencies only when a current requirement justifies them, not for hypothetical future use.
- For frontend work, you MUST follow the existing design system and state-management conventions. You MUST preserve unaffected interactions, navigation, and visual behavior.
- You MUST handle reachable failure states. For UI changes, you MUST include loading, empty, error, and success states where the changed flow needs them.
- You MUST validate untrusted input at trust boundaries and use safe APIs for queries, commands, paths, and rendered content. You MUST enforce protected operations at a trusted boundary; client-side checks alone are not authorization.
- You MUST keep secrets and environment-specific configuration out of committed code, client bundles, logs, and error output. You MUST NOT expose sensitive data in diagnostics.
- You MUST use existing logging and error-reporting mechanisms when the change needs diagnostics. You MUST preserve output contracts and avoid adding logging infrastructure by default.

## Verify and Report

- You MUST run the most relevant available checks for the change. You MUST add or update tests for changed logic and regression risks where the repository has a suitable test setup; otherwise you MUST use a focused alternative and report its limits.
- For UI changes, you MUST check affected interactions, relevant viewport sizes, and accessibility such as keyboard use, focus, and labels. You MUST use available browser or visual checks when needed; a successful build alone does not verify appearance or interaction.
- For deployment-impacting changes, you MUST include a smoke or health check and a rollback or mitigation path.
- You MUST check the final diff against the request. You MUST NOT treat passing one check as evidence for behavior it does not cover.
- You MUST report completed changes, relevant file paths, verification results, and remaining risks concisely. You MUST distinguish evidence from assumptions and state any skipped, failed, or unavailable checks.
- You MUST follow the requested output format, including full file contents when requested. You MUST NOT claim completion while required work remains unresolved.

## Skills

You MUST use the mode that matches the current phase. You MUST read its `SKILL.md` before applying it; you MUST prioritize explicitly requested skills in selection.

- `debug-mode`: Diagnose bugs, failures, or regressions before fixing them. Path: `.agents/skills/debug-mode/SKILL.md`.
- `design-mode`: Decide an approach, structure, or user flow before implementation. Path: `.agents/skills/design-mode/SKILL.md`.
- `implement-mode`: Implement an agreed change within its scope. Path: `.agents/skills/implement-mode/SKILL.md`.
- `review-mode`: Assess code or a plan for concrete defects and risks. Path: `.agents/skills/review-mode/SKILL.md`.

You MUST use one mode at a time unless the user requests a combination. You MUST switch modes as the task progresses, such as debug to implement after identifying the cause; switching within the authorized scope does not require renewed approval. You MUST NOT implement changes for a review-only or design-only request.

You MUST apply skills alongside these rules and the target repository's instructions; you MUST NOT treat skills as a replacement for them.

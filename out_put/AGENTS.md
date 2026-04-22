# AGENTS.md

## Core Rules

- You MUST restate explicit requirements before acting when the task has multiple constraints.
- You MUST treat unspecified information as unknown.
- You MUST ask for missing required data before making a decision that depends on it.
- You MUST NOT proceed with implementation when required inputs, acceptance criteria, or constraints are incomplete.
- You MAY ONLY infer from evidence available in the request, repository, tools, or verified sources.
- You MUST label every inference that affects implementation, review, or recommendation.
- You MUST NOT invent files, APIs, dependencies, behavior, dates, metrics, or user intent.
- You MUST NOT ignore any explicit constraint unless it conflicts with a higher-priority instruction.
- You MUST stop and report the conflict when requirements cannot all be satisfied.
- You MUST verify claims that can change over time before relying on them.
- You MUST distinguish facts, assumptions, risks, and completed work in final communication.

## Reasoning Rules

- You MUST identify the goal, constraints, inputs, and expected output before choosing an approach.
- You MUST map each explicit requirement to a planned action or validation before implementation.
- You MUST break multi-step work into ordered actions before executing irreversible or broad changes.
- You MUST use structured reasoning for non-trivial tasks before editing, running migrations, deploying, or changing behavior.
- You MUST decide which file, module, and layer owns the change before editing code.
- You MUST verify that the planned location already has responsibility for the behavior or document why ownership must move.
- You MUST validate each major decision against the stated requirements.
- You MUST use direct evidence from code, files, tests, logs, or source material when diagnosing issues.
- You MUST compare alternatives by observable trade-offs when more than one viable approach exists.
- You MUST NOT place behavior in generic helpers, utils, common modules, or constants merely because the correct owner is unclear.
- You MUST NOT skip from symptom to fix without identifying the mechanism that causes the symptom.
- You MUST NOT treat successful execution of one command as proof of unrelated behavior.
- You MUST record unresolved uncertainty when evidence is incomplete.
- You MUST revise the approach when new evidence contradicts the current plan.
- You MAY ONLY mark work complete after checking it against the original acceptance criteria.

## Scope Control

- You MUST define the task boundary from the user's request before changing files.
- You MUST modify only files required to satisfy the accepted task boundary.
- You MUST keep generated artifacts limited to the requested structure and count.
- You MUST treat behavior preservation as part of scope: new behavior MUST NOT silently alter existing flows, defaults, permissions, outputs, or integrations.
- You MUST ask for approval before expanding scope to new features, migrations, redesigns, or broad rewrites.
- You MUST treat unrelated cleanup, optimization, modernization, and style fixes as out of scope unless requested.
- You MUST NOT add convenience features that were not requested.
- You MUST NOT make silent improvements outside the task boundary, even when they appear low-risk.
- You MUST NOT change formatting, naming, or architecture outside the touched requirement.
- You MUST NOT replace working implementations when a targeted fix is sufficient.
- You MUST NOT perform destructive operations unless explicitly requested or approved.
- You MUST NOT combine application behavior changes with schema, data, configuration, or deployment changes unless the task requires the combined release.
- You MUST report any out-of-scope issue separately without fixing it automatically.
- You MUST keep configuration, secrets, and environment-specific values separate from code changes and committed defaults.
- You MUST identify rollback or mitigation for release-impacting changes, including how to disable the change or restore the previous version.
- You MUST include a health check, smoke test, or equivalent verification step for deployment-impacting changes.
- You MUST treat schema and data migrations as high-risk scope changes that require backward compatibility, reversible rollout planning, and data preservation checks.
- You MUST include rollback or mitigation steps for high-risk changes.

## Coding Rules

- You MUST inspect existing structure, naming, dependencies, and conventions before editing code.
- You MUST make the smallest change that satisfies the requirement without weakening existing behavior.
- You MUST preserve existing behavior, API contracts, data shapes, and error semantics when adding features unless the task explicitly requires a breaking change.
- You MUST implement only behavior required by the accepted task, not anticipated future variants.
- You MUST preserve public interfaces unless the task explicitly requires changing them.
- You MUST keep business logic, validation, data access, and presentation concerns separated according to existing architecture.
- You MUST keep behavior in its owning layer: transport handles protocol concerns, domain handles business rules, repositories handle persistence, and presentation handles UI formatting.
- You MUST keep dependencies pointing inward or downward according to the existing architecture; lower-level modules MUST NOT depend on higher-level transport, UI, or application orchestration modules.
- You MUST place new code in the narrowest existing module that owns the behavior.
- You MUST NOT create god files or catch-all modules; generic files such as utils, helpers, constants, or common MUST NOT contain domain workflow, persistence, authorization, or presentation logic.
- You MUST add or update tests when behavior changes or a regression risk is introduced.
- You MUST run the most relevant available validation for changed code.
- You MUST NOT refactor unrelated code.
- You MUST NOT introduce speculative abstractions, configuration, extension points, or generalization without a current requirement.
- You MUST NOT add dependencies unless the task cannot be completed with existing project tools.
- You MUST NOT duplicate logic when an existing local abstraction already covers the behavior.
- You MUST handle error paths that are reachable from the changed code.
- You MUST validate untrusted input at trust boundaries before using it in domain logic, persistence, commands, file paths, or outbound requests.
- You MUST enforce authentication and authorization at the boundary where protected behavior is invoked.
- You MUST use parameterized queries or the project's safe query builder for database access.
- You MUST NOT construct executable queries from unchecked string concatenation.
- You MUST emit structured logs for meaningful state changes, failures, and externally visible operations introduced by the change.
- You MUST avoid logging, exposing, or hardcoding secrets and sensitive data.
- You MUST exclude credentials, tokens, personal data, and sensitive payloads from logs, errors, metrics, and traces.
- You MUST leave unrelated user changes intact.

## Output Format

- You MUST answer in the format requested by the user.
- You MUST include full file contents when the user explicitly requests full file contents.
- You MUST make the required output directly usable without requiring the user to infer missing steps, files, or decisions.
- You MUST prioritize completed changes, verification evidence, and remaining risks.
- You MUST cite file paths for created, modified, or reviewed files.
- You MUST keep responses concise unless the user requests detail or the task requires it.
- You MUST NOT provide partial, placeholder, or ambiguous output unless explicitly requested or blocked.
- You MUST NOT include process narration that does not affect user decisions.
- You MUST NOT include hidden reasoning, private scratch work, or speculative alternatives as final output.
- You MUST NOT claim success for validation that was not run.
- You MUST state when validation was skipped, failed, or could not be performed.
- You MUST separate required output from optional notes when both are present.

## Skills

Skills are stored under `.agents/skills/<skill-name>/SKILL.md`.
Before starting work, you MUST check whether the task matches one of these skills:

Available skills:
- debug-mode: Use when diagnosing bugs, failures, regressions, unexpected behavior, logs, errors, or production symptoms before proposing or applying fixes.
  Path: .agents/skills/debug-mode/SKILL.md
- design-mode: Use when proposing architecture, flow, ownership, persistence, interface, deployment, or system boundary decisions before implementation.
  Path: .agents/skills/design-mode/SKILL.md
- implement-mode: Use when implementing requested behavior, modifying code paths, or extending existing functionality while preserving current behavior and scope.
  Path: .agents/skills/implement-mode/SKILL.md
- review-mode: Use when reviewing code, pull requests, diffs, or implementation plans for correctness, security, data loss, regressions, operational risk, and test coverage.
  Path: .agents/skills/review-mode/SKILL.md

If the user explicitly names a skill, you MUST use that skill.
If the task clearly matches a skill description, you MUST open that skill’s `SKILL.md` and follow it.
You MUST NOT apply multiple mode skills at once unless the user explicitly requests it.
Skills provide supplemental workflow instructions. You MUST still read and follow the current repository context, code, and constraints.

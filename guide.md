# Agent Skills Routing Guide

Use this folder as a skill registry for AI coding assistants. Start by matching the user request to one or more skills, then load only the required `SKILL.md` and supporting files.

## Routing Rules

1. Detect intent from the user request (build, design, review, test, deploy, secure, optimize, evaluate).
2. Pick the minimum skill set that covers the task.
3. Prefer one primary skill plus optional secondary skills.
4. Load extra files from `references/`, `templates/`, or `scripts/` only when needed.
5. Keep outputs actionable: decisions, commands, code changes, and verification.

## Skill Selection Map

- `project-scaffold`: Bootstrap a new codebase, repository structure, and baseline automation.
- `architecture-system-design`: Define high-level architecture, trade-offs, ADRs, and service boundaries.
- `backend-development`: Build APIs, data access, domain services, and reliability controls.
- `frontend-development`: Implement UX/UI features, state flows, accessibility, and web performance.
- `code-review`: Perform risk-first review with severity, evidence, and concrete remediation.
- `testing-strategy`: Design test plans across unit, integration, contract, and end-to-end levels.
- `devops-deployment`: Design CI/CD pipelines, release steps, rollback, and operational readiness.
- `git-workflow`: Standardize branches, commits, pull requests, and release tagging.
- `security-best-practices`: Apply secure coding, secrets handling, and threat-aware implementation.
- `prompt-engineering`: Write, test, and improve prompts, policies, and structured LLM interactions.
- `rag-implementation`: Build retrieval pipelines, chunking/indexing, and grounded generation behavior.
- `ai-agent-design`: Design multi-step agent loops, tools, memory boundaries, and guardrails.
- `mlops-deployment`: Operationalize model training, versioning, serving, and monitoring.
- `evaluation-and-testing-ai`: Define AI evaluation suites, metrics, baselines, and regression gates.
- `data-engineering-for-ai`: Build ingestion, transformation, quality controls, and AI-ready datasets.
- `vector-database`: Model embeddings, indexing, filtering, retrieval tuning, and lifecycle management.
- `ai-security-ethics`: Address misuse, privacy, bias, and policy compliance for AI systems.
- `common-ai-patterns`: Reuse proven AI architecture patterns and implementation blueprints.
- `common-coding-standards`: Enforce readability, maintainability, and consistency across repositories.

## Multi-Skill Composition

- New AI product: `project-scaffold` + `architecture-system-design` + `common-coding-standards`.
- Production AI app: `rag-implementation` + `ai-agent-design` + `evaluation-and-testing-ai` + `ai-security-ethics`.
- Release hardening: `code-review` + `testing-strategy` + `devops-deployment` + `security-best-practices`.

## Execution Standard

- Always define assumptions explicitly.
- Always produce test or validation evidence.
- Always include rollback or mitigation for high-risk changes.
- Always keep artifacts reusable for future tasks.


=== ./skills/ai-agent-design/references/agent-loop-pattern.md ===
# Agent Loop Pattern

## Standard Loop

1. Plan: decompose objective into bounded tasks.
2. Act: execute the next action or tool call.
3. Observe: parse outputs and environment signals.
4. Reflect: check progress, risks, and stop conditions.
5. Repeat or stop.

## Guardrails

- Max step budget.
- Max retry budget per tool.
- Sensitive action confirmation.
- Explicit exit when confidence is low.

## Telemetry

- Task ID
- Step number
- Tool name
- Outcome
- Error class

=== ./skills/ai-agent-design/SKILL.md ===
---
name: ai-agent-design
description: Design AI agents with clear control loops, tool orchestration, state boundaries, and safety guardrails.
when_to_use: Use when implementing autonomous or semi-autonomous AI workflows with planning, tool use, and iterative execution.
tags:
  - agents
  - orchestration
  - tools
  - autonomy
---

# Objective

Create predictable, inspectable agents that complete tasks safely and efficiently.

# Workflow

1. Define goal, constraints, and success criteria.
2. Design the control loop (plan, act, observe, reflect).
3. Specify tool contracts, permissions, and failure handling.
4. Define memory scope and retention policy.
5. Add human-in-the-loop checkpoints for risky actions.

# Best Practices

- Keep agent loops shallow and bounded.
- Prefer deterministic tool outputs over free text.
- Log reasoning summaries and action traces.
- Add stop conditions for run-away loops.

# Anti-Patterns

- Giving unrestricted tool access by default.
- Persisting sensitive context longer than needed.
- Allowing unbounded recursive planning.

# Resources

- Read `references/agent-loop-pattern.md` for orchestration patterns.

=== ./skills/ai-security-ethics/references/safety-risk-taxonomy.md ===
# Safety Risk Taxonomy

## Misuse Risks

- Malicious task enablement
- Policy circumvention
- Automated abuse at scale

## User Harm Risks

- Dangerous advice
- Harassment or hate amplification
- High-stakes misinformation

## Fairness Risks

- Disparate quality across groups
- Biased ranking or refusal behavior

## Privacy Risks

- Sensitive data leakage
- Re-identification or memorization exposure

For each risk, define prevention, detection, response, and ownership.

=== ./skills/ai-security-ethics/SKILL.md ===
---
name: ai-security-ethics
description: Apply AI security and ethics controls including misuse prevention, privacy protection, fairness checks, and policy-aligned governance.
when_to_use: Use when designing, reviewing, or deploying AI features that may impact users, organizations, or regulated data.
tags:
  - ai-safety
  - ethics
  - privacy
  - governance
---

# Objective

Reduce harmful outcomes and policy violations in AI systems across design, implementation, and operations.

# Workflow

1. Identify risk scenarios: misuse, bias, privacy, and abuse vectors.
2. Define policy constraints and refusal behavior.
3. Implement technical controls and audit mechanisms.
4. Evaluate impact across user segments and edge cases.
5. Monitor incidents and improve mitigations continuously.

# Best Practices

- Treat safety requirements as release-blocking.
- Provide transparent user-facing behavior where appropriate.
- Keep escalation and incident response procedures explicit.
- Review high-impact changes with multidisciplinary input.

# Anti-Patterns

- Framing ethics as optional documentation only.
- Deploying high-risk features without abuse monitoring.
- Collecting sensitive data without minimization or purpose control.

# Resources

- Use `references/safety-risk-taxonomy.md`.

=== ./skills/architecture-system-design/SKILL.md ===
---
name: architecture-system-design
description: Design scalable, reliable system architectures with clear component boundaries, data flow, and operational trade-offs.
when_to_use: Use when planning a new platform, redesigning core systems, or making architecture decisions with long-term impact.
tags:
  - architecture
  - system-design
  - scalability
  - reliability
---

# Objective

Produce architecture decisions that balance simplicity, scale, resilience, and delivery speed.

# Workflow

1. Capture requirements, constraints, and quality attributes.
2. Define context, containers, components, and interfaces.
3. Evaluate trade-offs with explicit decision records.
4. Plan observability, failure modes, and recovery paths.
5. Validate design with load, reliability, and cost assumptions.

# Best Practices

- State assumptions and unknowns explicitly.
- Separate synchronous and asynchronous paths clearly.
- Treat data ownership and schema evolution as first-class concerns.
- Use ADRs for non-trivial decisions.

# Anti-Patterns

- Designing from tools before requirements.
- Ignoring failure scenarios and backpressure.
- Centralizing all logic in one service.

# Resources

- Use `templates/system-design-doc-template.md` for design artifacts.

=== ./skills/architecture-system-design/templates/system-design-doc-template.md ===
# System Design Document

## 1. Context

- Problem statement:
- Stakeholders:
- Non-goals:

## 2. Requirements

- Functional requirements:
- Non-functional requirements:

## 3. Architecture

- Context diagram:
- Components:
- Data flow:

## 4. Trade-offs

- Option A:
- Option B:
- Decision and rationale:

## 5. Risks and Mitigations

- Risk:
- Detection:
- Mitigation:

## 6. Rollout Plan

- Milestones:
- Backward compatibility:
- Rollback plan:

=== ./skills/backend-development/references/api-design-checklist.md ===
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

=== ./skills/backend-development/SKILL.md ===
---
name: backend-development
description: Implement robust backend services including APIs, domain logic, persistence, async workflows, and operational controls.
when_to_use: Use when building or modifying server-side features, APIs, integrations, or database-backed business logic.
tags:
  - backend
  - api
  - services
  - database
---

# Objective

Deliver backend features that are correct, observable, secure, and maintainable in production.

# Workflow

1. Define contract first: request/response, validation, and errors.
2. Implement domain logic independent from transport concerns.
3. Add data access with migrations and transaction boundaries.
4. Add telemetry, retries, idempotency, and timeouts where needed.
5. Validate with unit, integration, and contract tests.

# Best Practices

- Keep handlers thin; keep business logic testable.
- Version API contracts intentionally.
- Prefer explicit error models over ad-hoc exceptions.
- Instrument critical paths with traces and metrics.

# Anti-Patterns

- Leaking persistence models directly to API consumers.
- Silent retries without bounded backoff.
- Mixing validation and side effects.

# Resources

- Read `references/api-design-checklist.md` before implementing endpoints.

=== ./skills/code-review/references/review-checklist.md ===
# Review Checklist

- Intent of change is clear from title and description.
- Business logic changes are correct for edge cases.
- Backward compatibility impact is considered.
- Error handling and retry behavior are safe.
- Security checks exist at trust boundaries.
- Tests cover changed behavior, not only happy paths.
- Logging and telemetry are sufficient for diagnosis.
- Migration and rollout steps are safe and reversible.

=== ./skills/code-review/references/severity-model.md ===
# Severity Model

## Critical

Production outage, data loss, privilege escalation, or exploitable vulnerability.

## High

Functional failure on core path, severe regression risk, or broken data integrity.

## Medium

Non-critical behavior bugs, maintainability hazards, or incomplete resilience controls.

## Low

Minor correctness concerns, readability issues, or optional improvements.

## Rule

Assign the highest defensible severity based on user impact and likelihood.

=== ./skills/code-review/scripts/changed-files.ps1 ===
param(
    [string]$BaseRef = "origin/main"
)

$files = git diff --name-only $BaseRef...HEAD
if (-not $files) {
    Write-Output "No changed files detected."
    exit 0
}

$files | ForEach-Object { Write-Output $_ }

=== ./skills/code-review/SKILL.md ===
---
name: code-review
description: Perform high-signal code reviews focused on correctness, regressions, security, maintainability, and test adequacy.
when_to_use: Use when reviewing pull requests, auditing risky changes, or assessing production-readiness before merge.
tags:
  - review
  - quality
  - risk
  - governance
---

# Objective

Identify and communicate defects, risks, and missing validations before code is merged.

# Workflow

1. Understand change intent and scope from diff plus context.
2. Assess correctness, edge cases, and regression risks.
3. Review tests for coverage depth and failure behavior.
4. Classify findings by severity and include evidence.
5. Propose concrete remediation and verification steps.

# Best Practices

- Prioritize bugs and behavioral regressions over style.
- Anchor each finding to file and line.
- Include reasoning and expected impact.
- Call out missing tests explicitly.

# Anti-Patterns

- Approving based only on readability.
- Reporting vague concerns with no reproduction path.
- Mixing critical and cosmetic feedback without severity labels.

# Resources

- Use `references/severity-model.md` for issue classification.
- Use `references/review-checklist.md` for systematic review.
- Use `templates/review-report-template.md` for review output.
- Run `scripts/changed-files.ps1` to focus on touched files.

=== ./skills/code-review/templates/review-report-template.md ===
# Review Report

## Summary

Short assessment of merge readiness.

## Findings

| Severity | File | Issue | Recommendation |
|---|---|---|---|
| High | path/file.ext | Description | Concrete fix |

## Test Assessment

- Existing tests reviewed:
- Missing tests:
- Suggested test cases:

## Final Recommendation

- Merge:
- Blockers:

=== ./skills/common-ai-patterns/references/pattern-catalog.md ===
# AI Pattern Catalog

## 1) Classify Then Act

Classify intent or risk tier, then route to specialized handlers.

## 2) Retrieve Then Generate

Retrieve grounded context, then generate response with citations.

## 3) Draft Then Critique

Produce candidate output, then run a critic pass before finalizing.

## 4) Tool-Orchestrated Completion

Use model to plan and call deterministic tools for execution.

## 5) Human Approval Gate

Require human confirmation for high-impact or irreversible actions.

=== ./skills/common-ai-patterns/SKILL.md ===
---
name: common-ai-patterns
description: Apply reusable AI solution patterns for classification, extraction, generation, retrieval, routing, and agentic workflows.
when_to_use: Use when choosing implementation patterns for AI features and avoiding one-off, fragile designs.
tags:
  - ai-patterns
  - architecture
  - reuse
  - design
---

# Objective

Accelerate delivery by selecting proven AI patterns that fit problem constraints.

# Workflow

1. Classify problem type and quality requirements.
2. Select matching pattern and define acceptance metrics.
3. Implement minimal vertical slice.
4. Add evaluation and observability loops.
5. Harden for production with scaling and safety controls.

# Best Practices

- Start from simplest pattern that can work.
- Keep pattern decisions explicit and testable.
- Combine patterns only when one pattern cannot satisfy constraints.
- Revisit pattern choice as data and usage evolve.

# Anti-Patterns

- Jumping to agents for simple extraction tasks.
- Combining many model stages without observability.
- Ignoring fallback paths for uncertain outputs.

# Resources

- Read `references/pattern-catalog.md`.

=== ./skills/common-coding-standards/references/style-and-quality-checklist.md ===
# Style and Quality Checklist

- Naming is domain-meaningful and consistent.
- Functions and classes have single clear responsibility.
- Error handling is explicit and actionable.
- Logging is structured and avoids sensitive data.
- Tests are deterministic and cover behavior changes.
- Public interfaces are documented with examples.
- Dead code and unused dependencies are removed.
- CI enforces lint, format, and test gates.

=== ./skills/common-coding-standards/SKILL.md ===
---
name: common-coding-standards
description: Enforce consistent coding standards for readability, maintainability, testability, and long-term code health across teams.
when_to_use: Use when creating team conventions, reviewing style quality, or standardizing project-level engineering practices.
tags:
  - coding-standards
  - maintainability
  - quality
  - conventions
---

# Objective

Keep codebases coherent and easy to evolve by applying clear engineering standards.

# Workflow

1. Define naming, structure, and formatting conventions.
2. Define error handling and logging expectations.
3. Define testing and documentation requirements.
4. Automate checks in lint, format, and CI.
5. Review deviations and tighten standards iteratively.

# Best Practices

- Favor explicitness over cleverness.
- Keep functions focused and side effects clear.
- Align abstractions with domain language.
- Document non-obvious decisions in code comments or ADRs.

# Anti-Patterns

- Using style rules with no enforcement automation.
- Allowing widespread exceptions to standards.
- Prioritizing micro-optimizations over readability.

# Resources

- Read `references/style-and-quality-checklist.md`.

=== ./skills/data-engineering-for-ai/references/data-quality-slos.md ===
# Data Quality SLOs

Define service-level objectives for data products:

- Freshness: maximum tolerated delay from source to curated layer.
- Completeness: required percentage of expected records.
- Validity: required pass rate for schema and rule checks.
- Uniqueness: duplicate tolerance threshold.
- Consistency: cross-table integrity checks.

Attach alert thresholds and escalation owners for each SLO.

=== ./skills/data-engineering-for-ai/SKILL.md ===
---
name: data-engineering-for-ai
description: Build reliable data pipelines for AI workloads with ingestion, transformation, quality enforcement, and governance controls.
when_to_use: Use when preparing training, evaluation, or retrieval datasets from heterogeneous sources.
tags:
  - data-engineering
  - pipelines
  - data-quality
  - governance
---

# Objective

Deliver trustworthy, well-modeled data products that support AI systems at scale.

# Workflow

1. Define source contracts and ingestion cadence.
2. Build transformations with schema and lineage tracking.
3. Enforce quality checks, anomaly detection, and SLAs.
4. Partition and optimize storage for downstream consumers.
5. Monitor freshness, completeness, and cost.

# Best Practices

- Treat datasets as versioned products.
- Add data contracts between producers and consumers.
- Use idempotent jobs and replay support.
- Track PII and policy tags through pipeline stages.

# Anti-Patterns

- Silent schema changes in source systems.
- Mixing raw and curated layers.
- Unbounded backfills without resource controls.

# Resources

- Read `references/data-quality-slos.md`.

=== ./skills/devops-deployment/references/deployment-checklist.md ===
# Deployment Checklist

- Build is reproducible and artifact is immutable.
- Required tests and security checks are green.
- Config and secrets are environment-scoped.
- Database migrations are backward compatible.
- Rollout strategy (canary/blue-green) is selected.
- Rollback conditions and commands are documented.
- Post-deploy smoke checks are automated.
- Alert thresholds are verified before release.

=== ./skills/devops-deployment/SKILL.md ===
---
name: devops-deployment
description: Build dependable CI/CD and deployment workflows with safety checks, observability, rollback, and incident readiness.
when_to_use: Use when creating or improving build pipelines, release automation, deployment runbooks, and operations controls.
tags:
  - devops
  - deployment
  - ci-cd
  - operations
---

# Objective

Ship changes safely and repeatedly with minimal downtime and fast recovery.

# Workflow

1. Define build, test, package, and deploy stages.
2. Add environment promotion and approval policies.
3. Add health checks, canary/blue-green options, and rollback.
4. Integrate logs, metrics, traces, and alerts.
5. Run release drills and post-deploy verification.

# Best Practices

- Keep deployment artifacts immutable.
- Separate config from code with secure secret management.
- Automate rollback criteria.
- Track deployment lead time and change failure rate.

# Anti-Patterns

- Manual hotfixes without audit trail.
- Sharing mutable runtime state across deploys.
- Deploying without observability baselines.

# Resources

- Follow `references/deployment-checklist.md`.
- Use `templates/release-runbook-template.md` for standardized releases.

=== ./skills/devops-deployment/templates/release-runbook-template.md ===
# Release Runbook

## Release Metadata

- Version:
- Environment:
- Owner:
- Change window:

## Pre-Checks

- Build and tests:
- Migration readiness:
- Feature flags:

## Deployment Steps

1. Step
2. Step
3. Step

## Verification

- Health checks:
- Functional smoke tests:
- Metrics validation:

## Rollback

- Trigger criteria:
- Rollback command:
- Validation after rollback:

=== ./skills/evaluation-and-testing-ai/references/llm-eval-metrics.md ===
# LLM Evaluation Metrics

## Quality

- Accuracy or rubric score
- Task completion rate
- Groundedness / factual consistency

## Safety

- Policy violation rate
- Harmful output rate
- Refusal correctness

## Performance

- End-to-end latency
- Token usage
- Cost per successful task

## Stability

- Regression delta vs baseline
- Variance across reruns
- Tail failure rate (P95/P99)

=== ./skills/evaluation-and-testing-ai/scripts/score_eval_results.py ===
#!/usr/bin/env python3
import csv
import sys


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: score_eval_results.py <results.csv>")
        return 1

    path = sys.argv[1]
    total = 0
    passed = 0
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += 1
            if row.get("pass", "").strip().lower() in {"1", "true", "yes", "pass"}:
                passed += 1

    if total == 0:
        print("No rows found.")
        return 2

    rate = passed / total
    print(f"Passed: {passed}/{total} ({rate:.2%})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

=== ./skills/evaluation-and-testing-ai/SKILL.md ===
---
name: evaluation-and-testing-ai
description: Build rigorous evaluation frameworks for AI systems including offline tests, online metrics, and regression gating.
when_to_use: Use when validating AI quality, comparing model or prompt variants, or enforcing release gates for AI behavior.
tags:
  - evaluation
  - ai-testing
  - metrics
  - regression
---

# Objective

Create repeatable AI evaluation that detects quality regressions before production impact.

# Workflow

1. Define task taxonomy and failure classes.
2. Build benchmark datasets with gold labels or rubric criteria.
3. Select metrics for quality, safety, latency, and cost.
4. Run baseline and candidate comparisons.
5. Set pass/fail thresholds and release policies.

# Best Practices

- Separate evaluation by use case segment.
- Track both aggregate and tail failure behavior.
- Include red-team and adversarial cases.
- Record exact model, prompt, and dataset versions.

# Anti-Patterns

- Relying on anecdotal spot checks only.
- Changing benchmarks without version control.
- Optimizing one metric while regressing safety.

# Resources

- Read `references/llm-eval-metrics.md`.
- Use `templates/eval-plan-template.md`.
- Run `scripts/score_eval_results.py` for basic score summaries.

=== ./skills/evaluation-and-testing-ai/templates/eval-plan-template.md ===
# AI Evaluation Plan

## Goal

-

## Candidate Variants

- Baseline:
- Candidate A:
- Candidate B:

## Dataset

- Source:
- Size:
- Segments:

## Metrics and Thresholds

| Metric | Threshold | Blocking |
|---|---|---|
| Accuracy | >= 0.85 | yes |

## Execution

- Offline run:
- Online experiment:
- Decision owner:

=== ./skills/frontend-development/references/ui-performance-checklist.md ===
# UI Performance Checklist

- Largest contentful paint target is defined and measured.
- Critical rendering path is minimized.
- Images are optimized and responsive.
- Non-critical scripts are deferred or lazy-loaded.
- Lists use virtualization when large.
- State updates avoid unnecessary rerenders.
- Input responsiveness under load is tested.
- Bundle size budgets are enforced in CI.

=== ./skills/frontend-development/SKILL.md ===
---
name: frontend-development
description: Build accessible, responsive, and performant user interfaces with maintainable state management and reliable UX behavior.
when_to_use: Use when creating or refactoring web UI features, interaction flows, or frontend architecture.
tags:
  - frontend
  - ui
  - accessibility
  - performance
---

# Objective

Ship user-facing features that are usable, fast, accessible, and resilient to edge cases.

# Workflow

1. Define user journey, states, and acceptance criteria.
2. Build semantic UI structure and accessible interactions.
3. Implement state flow and data fetching boundaries.
4. Handle loading, empty, error, and retry states.
5. Validate with UI tests, accessibility checks, and performance budgets.

# Best Practices

- Build components around behaviors, not visuals alone.
- Keep design tokens centralized.
- Use progressive enhancement where possible.
- Set measurable performance goals early.

# Anti-Patterns

- Shipping inaccessible controls or missing keyboard support.
- Coupling view components to API shapes directly.
- Ignoring mobile and low-bandwidth scenarios.

# Resources

- Read `references/ui-performance-checklist.md` during implementation and review.

=== ./skills/git-workflow/references/commit-convention.md ===
# Commit Convention

Use structured commit messages:

`type(scope): short summary`

Suggested `type` values:

- `feat`: new behavior
- `fix`: bug fix
- `refactor`: structure improvement without behavior change
- `test`: tests only
- `docs`: documentation only
- `chore`: tooling or maintenance

Rules:

- Keep summary under 72 characters.
- Use imperative form.
- Reference issue IDs in body when applicable.

=== ./skills/git-workflow/SKILL.md ===
---
name: git-workflow
description: Apply consistent Git practices for branching, commit hygiene, pull requests, release tags, and collaboration safety.
when_to_use: Use when defining team Git conventions, preparing pull requests, or managing release and hotfix flows.
tags:
  - git
  - collaboration
  - release
  - version-control
---

# Objective

Improve collaboration velocity and traceability while reducing merge risk and release friction.

# Workflow

1. Choose a branch strategy aligned to release cadence.
2. Enforce commit message conventions and atomic commits.
3. Use pull-request templates and required checks.
4. Tag releases and maintain changelog inputs.
5. Manage hotfix and rollback flows explicitly.

# Best Practices

- Keep commits focused on one concern.
- Rebase or merge predictably based on team policy.
- Require green CI before merge.
- Protect main branch with review gates.

# Anti-Patterns

- Large mixed commits with unrelated changes.
- Force pushes to shared stable branches.
- Merging without test and review evidence.

# Resources

- Read `references/commit-convention.md`.
- Use `templates/pull-request-template.md`.

=== ./skills/git-workflow/templates/pull-request-template.md ===
# Pull Request

## Summary

Describe what changed and why.

## Changes

- Item 1
- Item 2

## Risk and Impact

- User impact:
- Operational impact:
- Rollback plan:

## Testing

- Automated tests:
- Manual checks:

## Checklist

- [ ] CI is green
- [ ] Migration impact reviewed
- [ ] Security impact reviewed

=== ./skills/mlops-deployment/references/model-release-checklist.md ===
# Model Release Checklist

- Training data snapshot is versioned.
- Features are consistent between training and serving.
- Offline evaluation meets threshold.
- Safety and bias checks pass.
- Serving latency and throughput targets pass load test.
- Rollback model version is available.
- Post-release monitoring dashboards are active.

=== ./skills/mlops-deployment/SKILL.md ===
---
name: mlops-deployment
description: Operationalize machine learning systems with reproducible training, model registry, deployment pipelines, and monitoring.
when_to_use: Use when moving ML models from experimentation to reliable production serving.
tags:
  - mlops
  - model-serving
  - monitoring
  - lifecycle
---

# Objective

Deliver ML models with traceability, reproducibility, and controlled production risk.

# Workflow

1. Standardize datasets, feature definitions, and training configs.
2. Version models, metadata, and evaluation artifacts.
3. Build CI/CD for training and serving paths.
4. Deploy with staged rollout and rollback triggers.
5. Monitor accuracy, drift, latency, and cost.

# Best Practices

- Separate offline metrics from online business KPIs.
- Keep feature engineering consistent across train and serve.
- Automate lineage capture for compliance.
- Define retraining policy by drift thresholds.

# Anti-Patterns

- Promoting models without reproducible training runs.
- Ignoring data drift until incidents occur.
- Coupling model and feature pipelines too tightly.

# Resources

- Use `references/model-release-checklist.md`.

=== ./skills/project-scaffold/references/stack-selection.md ===
# Stack Selection Checklist

Use this checklist before scaffolding:

- Runtime and language versions are explicitly pinned.
- Framework choice matches team expertise and hosting model.
- Package manager and lockfile strategy are defined.
- Test framework and CI runtime are chosen.
- Lint and formatting tooling are selected.
- Local developer workflow commands are standardized.
- Deployment target and environment model are known.
- Security baseline (secret storage, dependency scan) is decided.

=== ./skills/project-scaffold/scripts/init_project.ps1 ===
param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectRoot
)

$dirs = @(
    "src",
    "tests",
    "docs",
    ".github/workflows"
)

foreach ($dir in $dirs) {
    $path = Join-Path $ProjectRoot $dir
    New-Item -ItemType Directory -Force -Path $path | Out-Null
}

$gitkeepTargets = @(
    "src/.gitkeep",
    "tests/.gitkeep",
    "docs/.gitkeep"
)

foreach ($target in $gitkeepTargets) {
    $path = Join-Path $ProjectRoot $target
    if (-not (Test-Path $path)) {
        New-Item -ItemType File -Path $path | Out-Null
    }
}

Write-Output "Initialized scaffold at $ProjectRoot"

=== ./skills/project-scaffold/SKILL.md ===
---
name: project-scaffold
description: Create production-ready project foundations, repository layout, baseline tooling, and initial docs for new software projects.
when_to_use: Use when starting a new project, standardizing repository structure, or creating a repeatable foundation for teams.
tags:
  - scaffold
  - repository
  - bootstrap
  - standards
---

# Objective

Create a clean, reproducible project foundation that is easy to develop, test, review, and deploy.

# Workflow

1. Confirm runtime, framework, package manager, and deployment target.
2. Generate a minimal but complete folder layout.
3. Add quality gates: lint, format, test, and CI stubs.
4. Add developer documentation and contribution standards.
5. Verify bootstrap commands run successfully.

# Best Practices

- Keep the first scaffold small and composable.
- Separate source code, tests, configs, and docs clearly.
- Include environment examples, not real secrets.
- Add Makefile or scripts for common commands.

# Anti-Patterns

- Overengineering before first feature delivery.
- Committing environment-specific artifacts.
- Missing onboarding steps for new contributors.

# Resources

- Read `references/stack-selection.md` for decision criteria.
- Use `templates/project-brief-template.md` to lock scope early.
- Use `templates/README.template.md` as initial README.
- Run `scripts/init_project.ps1` for deterministic setup.

=== ./skills/project-scaffold/templates/project-brief-template.md ===
# Project Brief

## Problem

Describe the user or business problem.

## Scope

- In scope:
- Out of scope:

## Success Criteria

- Metric 1:
- Metric 2:

## Constraints

- Technical:
- Compliance:
- Timeline:

## Initial Milestones

1. Scaffold and baseline automation.
2. First end-to-end feature.
3. Release candidate.

=== ./skills/project-scaffold/templates/README.template.md ===
# {{PROJECT_NAME}}

## Overview

Short summary of purpose and scope.

## Prerequisites

- Runtime:
- Package manager:

## Quick Start

```bash
<install-command>
<test-command>
<run-command>
```

## Repository Structure

- `src/`: application code
- `tests/`: automated tests
- `docs/`: architecture and runbooks

## Quality Gates

- Lint:
- Tests:
- Security scan:

## Contributing

See contribution and pull request rules in repository policy files.

=== ./skills/prompt-engineering/references/prompt-patterns.md ===
# Prompt Patterns

## Direct Instruction Pattern

Use for deterministic transformations.

Template:

- Task
- Constraints
- Output schema

## Few-Shot Pattern

Use when formatting or reasoning style needs examples.

Rules:

- Keep examples short.
- Cover edge cases.
- Avoid contradictory examples.

## Tool-Use Pattern

Use when model must call tools.

Rules:

- Specify when to call each tool.
- Define strict output contract for tool arguments.
- Add retry and fallback behavior.

## Guardrail Pattern

Use for sensitive or policy-constrained tasks.

Rules:

- Define refusal boundaries.
- Define uncertainty responses.
- Require citation from provided context when needed.

=== ./skills/prompt-engineering/scripts/prompt-lint.py ===
#!/usr/bin/env python3
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "## Objective",
    "## Input Contract",
    "## Output Contract",
    "## Safety Rules",
]


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: prompt-lint.py <prompt-spec.md>")
        return 1

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        return 1

    content = path.read_text(encoding="utf-8")
    missing = [section for section in REQUIRED_SECTIONS if section not in content]
    if missing:
        print("Missing sections:")
        for section in missing:
            print(f"- {section}")
        return 2

    print("Prompt spec passed basic lint checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

=== ./skills/prompt-engineering/SKILL.md ===
---
name: prompt-engineering
description: Design reliable prompts, instruction hierarchies, and structured outputs for LLM-powered applications and automation.
when_to_use: Use when creating or improving prompts, reducing hallucination risk, or building repeatable LLM workflows.
tags:
  - prompts
  - llm
  - reliability
  - structured-output
---

# Objective

Produce prompts that are robust, testable, and aligned with clear output contracts.

# Workflow

1. Define task objective, constraints, and output schema.
2. Choose prompt pattern (role, few-shot, chain-of-thought policy, tool-use).
3. Add grounding context and explicit refusal boundaries.
4. Evaluate with representative and adversarial cases.
5. Iterate with versioning and regression checks.

# Best Practices

- Write deterministic output instructions.
- Separate system policy from task content.
- Keep examples short and diverse.
- Add explicit uncertainty behavior.

# Anti-Patterns

- Prompting with ambiguous goals.
- Overloading one prompt with multiple conflicting tasks.
- Shipping prompts without an evaluation suite.

# Resources

- Read `references/prompt-patterns.md`.
- Use `templates/prompt-spec-template.md`.
- Run `scripts/prompt-lint.py` for structural checks.

=== ./skills/prompt-engineering/templates/prompt-spec-template.md ===
# Prompt Specification

## Prompt Name

-

## Objective

-

## Input Contract

- Fields:
- Constraints:

## Output Contract

- Format:
- Required fields:
- Validation rules:

## Safety Rules

- Refusal criteria:
- Sensitive content handling:

## Examples

### Positive

Input:
Output:

### Negative

Input:
Expected refusal or safe response:

=== ./skills/rag-implementation/references/rag-architecture-patterns.md ===
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

=== ./skills/rag-implementation/SKILL.md ===
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

=== ./skills/rag-implementation/templates/rag-evaluation-template.md ===
# RAG Evaluation Sheet

## Dataset

- Domain:
- Query count:
- Source freshness:

## Retrieval Metrics

- Recall@k:
- MRR:
- NDCG:

## Generation Metrics

- Groundedness:
- Citation accuracy:
- Answer completeness:

## Failure Log

| Query | Failure Type | Root Cause | Fix |
|---|---|---|---|

=== ./skills/security-best-practices/references/threat-modeling-checklist.md ===
# Threat Modeling Checklist

- Assets and sensitive data are identified.
- Trust boundaries are mapped.
- Entry points and abuse paths are documented.
- Authentication and authorization risks are analyzed.
- Data exfiltration and integrity risks are assessed.
- Dependency and supply-chain risks are considered.
- Mitigations are linked to concrete controls.
- Residual risk and owners are documented.

=== ./skills/security-best-practices/SKILL.md ===
---
name: security-best-practices
description: Integrate secure-by-default engineering practices including threat modeling, input validation, secret management, and dependency hygiene.
when_to_use: Use when implementing features that handle user input, authentication, data access, or any sensitive workflows.
tags:
  - security
  - secure-coding
  - threat-modeling
  - compliance
---

# Objective

Reduce exploitability and security regressions through systematic secure engineering controls.

# Workflow

1. Model trust boundaries and threat scenarios.
2. Validate and sanitize all external inputs.
3. Enforce authentication, authorization, and least privilege.
4. Manage secrets, encryption, and key rotation safely.
5. Run security scans and review findings before release.

# Best Practices

- Default-deny where possible.
- Use parameterized queries and safe serializers.
- Track and patch vulnerable dependencies quickly.
- Log security events with tamper-aware retention.

# Anti-Patterns

- Hardcoding secrets in code or CI config.
- Relying on client-side validation alone.
- Skipping authorization checks on internal endpoints.

# Resources

- Use `references/threat-modeling-checklist.md` for design and review.

=== ./skills/testing-strategy/references/test-pyramid-and-honeycomb.md ===
# Test Pyramid and Honeycomb Guidance

Use a blended model:

- Unit tests: fast checks for pure logic and component behavior.
- Integration tests: verify module boundaries and data contracts.
- Contract tests: ensure service-to-service compatibility.
- End-to-end tests: validate critical user journeys.
- Non-functional tests: performance, resiliency, and security behavior.

Prefer many deterministic lower-level tests and fewer high-value end-to-end tests.

=== ./skills/testing-strategy/scripts/generate-test-matrix.py ===
#!/usr/bin/env python3
import csv
import sys


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: generate-test-matrix.py <input.csv> <output.md>")
        return 1

    input_csv = sys.argv[1]
    output_md = sys.argv[2]

    rows = []
    with open(input_csv, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    headers = ["feature", "risk", "test_level", "owner", "status"]
    with open(output_md, "w", encoding="utf-8") as f:
        f.write("| Feature | Risk | Test Level | Owner | Status |\n")
        f.write("|---|---|---|---|---|\n")
        for row in rows:
            f.write(
                "| {0} | {1} | {2} | {3} | {4} |\n".format(
                    row.get("feature", ""),
                    row.get("risk", ""),
                    row.get("test_level", ""),
                    row.get("owner", ""),
                    row.get("status", "planned"),
                )
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

=== ./skills/testing-strategy/SKILL.md ===
---
name: testing-strategy
description: Design and operationalize pragmatic testing strategies across unit, integration, contract, and end-to-end levels.
when_to_use: Use when defining test plans, improving confidence before releases, or fixing weak coverage in critical paths.
tags:
  - testing
  - quality
  - reliability
  - strategy
---

# Objective

Create a balanced test portfolio that catches defects early and protects business-critical behavior.

# Workflow

1. Map critical user and system flows.
2. Choose test levels per risk and feedback speed.
3. Define deterministic fixtures, mocks, and test data strategy.
4. Add CI gates, flake controls, and failure triage workflow.
5. Track coverage of behavior, not just lines.

# Best Practices

- Test contracts at service boundaries.
- Keep end-to-end tests focused and stable.
- Enforce fast unit tests as the default.
- Add non-functional tests for performance and reliability.

# Anti-Patterns

- Depending only on end-to-end tests.
- Treating coverage percentage as the only metric.
- Keeping flaky tests as optional warnings.

# Resources

- Read `references/test-pyramid-and-honeycomb.md` for model selection.
- Use `templates/test-plan-template.md` to produce test plans.
- Run `scripts/generate-test-matrix.py` to build scenario matrices.

=== ./skills/testing-strategy/templates/test-plan-template.md ===
# Test Plan

## Scope

- In scope:
- Out of scope:

## Risk Matrix

| Area | Risk | Test Level | Owner |
|---|---|---|---|
| Auth | High | Integration + E2E | Team A |

## Test Data Strategy

- Data sources:
- Fixtures:
- Sanitization:

## Automation and Gates

- Required CI checks:
- Flake policy:
- Release blocking criteria:

=== ./skills/vector-database/references/indexing-and-retrieval.md ===
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

=== ./skills/vector-database/SKILL.md ===
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

=== agent-skills/SKILL-TEMPLATE.md ===
---
name: skill-name
description: Clear summary of what this skill does.
when_to_use: Use when these exact triggers or contexts are present.
tags:
  - domain
  - workflow
  - tools
---

# Objective

State the concrete outcome this skill should produce.

# Workflow

1. Confirm scope, constraints, and acceptance criteria.
2. Select the minimal implementation path.
3. Execute with deterministic steps and checkpoints.
4. Validate with tests or measurable verification.
5. Report outputs, risks, and next actions.

# Best Practices

- Keep instructions specific and executable.
- Prefer reusable assets for repeated work.
- Include commands, snippets, or templates that reduce ambiguity.
- Define quality gates before implementation.

# Anti-Patterns

- Starting implementation before scope is clear.
- Mixing unrelated concerns in one workflow.
- Skipping validation or evidence collection.
- Writing generic guidance with no actionable steps.

# Resources

- `references/`: domain notes, checklists, decision criteria.
- `templates/`: reusable docs, forms, boilerplates.
- `scripts/`: deterministic automation helpers.

# Structure

```text
skill-name/
|-- SKILL.md
|-- references/        # optional
|-- templates/         # optional
`-- scripts/           # optional
```


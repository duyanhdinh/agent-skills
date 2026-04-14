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

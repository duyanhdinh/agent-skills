# Coding Rules

- You MUST inspect existing structure, naming, dependencies, and conventions before editing code.
- You MUST make the smallest change that satisfies the requirement without weakening existing behavior.
- You MUST implement only behavior required by the accepted task, not anticipated future variants.
- You MUST preserve public interfaces unless the task explicitly requires changing them.
- You MUST keep business logic, validation, data access, and presentation concerns separated according to existing architecture.
- You MUST add or update tests when behavior changes or a regression risk is introduced.
- You MUST run the most relevant available validation for changed code.
- Do NOT refactor unrelated code.
- Do NOT introduce speculative abstractions, configuration, extension points, or generalization without a current requirement.
- Do NOT add dependencies unless the task cannot be completed with existing project tools.
- Do NOT duplicate logic when an existing local abstraction already covers the behavior.
- You MUST handle error paths that are reachable from the changed code.
- You MUST avoid logging, exposing, or hardcoding secrets and sensitive data.
- You MUST leave unrelated user changes intact.

# Reasoning Rules

- You MUST identify the goal, constraints, inputs, and expected output before choosing an approach.
- You MUST map each explicit requirement to a planned action or validation before implementation.
- You MUST break multi-step work into ordered actions before executing irreversible or broad changes.
- You MUST use structured reasoning for non-trivial tasks before editing, running migrations, deploying, or changing behavior.
- You MUST decide which file, module, and layer owns the change before editing code.
- You MUST verify that the planned location already has responsibility for the behavior or document why ownership must move.
- You MUST validate each major decision against the stated requirements.
- You MUST use direct evidence from code, files, tests, logs, or source material when diagnosing issues.
- You MUST compare alternatives by observable trade-offs when more than one viable approach exists.
- Do NOT place behavior in generic helpers, utils, common modules, or constants merely because the correct owner is unclear.
- Do NOT skip from symptom to fix without identifying the mechanism that causes the symptom.
- Do NOT treat successful execution of one command as proof of unrelated behavior.
- You MUST record unresolved uncertainty when evidence is incomplete.
- You MUST revise the approach when new evidence contradicts the current plan.
- You MAY ONLY mark work complete after checking it against the original acceptance criteria.

# Design Mode

- You MUST state the decision boundary before proposing architecture or flow changes.
- You MUST compare at least two viable options when the choice affects persistence, interfaces, deployment, or ownership.
- You MUST evaluate trade-offs using concrete constraints: coupling, migration cost, operability, failure modes, and reversibility.
- You MUST NOT propose rewrites when an incremental design satisfies the same requirement.
- You MUST preserve existing system boundaries unless a named constraint proves they no longer fit.
- You MUST identify the first irreversible decision and define how to defer or mitigate it.
- You MUST reject generic patterns that do not solve a specific stated force in the problem.

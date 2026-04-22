# Debug Mode

- You MUST reproduce or localize the symptom before proposing a fix.
- You MUST identify the failing mechanism that connects the observed symptom to the suspected cause.
- You MUST keep competing hypotheses open until evidence eliminates them.
- You MUST NOT change code based only on log proximity, error wording, or intuition.
- You MUST inspect the last known good boundary: inputs, state transition, external dependency, or output.
- You MUST validate the fix against the original symptom and at least one adjacent failure path.
- You MUST record any unresolved uncertainty that could invalidate the diagnosis.

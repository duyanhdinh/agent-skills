---
name: debug-mode
description: Use when diagnosing bugs, failures, regressions, or unexpected behavior before proposing a fix.
---

# Debug Mode

- You MUST establish expected and actual behavior. You MUST reproduce the symptom or localize it with available evidence; you MUST state when reproduction is unavailable.
- You MUST trace the relevant inputs, state changes, and outputs to find where behavior first diverges. For UI bugs, you MUST include user actions, rendering, and network activity when relevant.
- You MUST test plausible causes with focused checks. You MUST NOT select a cause from error wording, nearby logs, or intuition alone.
- You MUST identify the mechanism connecting the cause to the symptom before proposing a fix. You MUST keep unresolved hypotheses explicit when evidence is incomplete.
- Once the cause is supported, you MUST move to implementation if fixing it is within the request; otherwise you MUST report the diagnosis and proposed correction.
- You MUST verify the correction against the original symptom and relevant neighboring behavior. You MUST add a regression test when a suitable test setup exists, or document the focused reproduction check.
- You MUST report what the evidence establishes and any remaining uncertainty that could invalidate the diagnosis.

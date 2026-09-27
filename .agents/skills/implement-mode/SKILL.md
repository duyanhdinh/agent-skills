---
name: implement-mode
description: Use when implementing or modifying requested functionality, interfaces, or presentation within an agreed scope.
---

# Implement Mode

- You MUST locate the code path or components responsible for the requested change and identify relevant checks before editing.
- You MUST implement the smallest complete solution using existing patterns. You MUST create a new module or abstraction only when the current change needs it; you MUST NOT use call-site counts as a universal rule.
- You MUST preserve unaffected contracts, defaults, side effects, and ordering. You MUST retain compatibility only where existing consumers require it, rather than adding speculative fallbacks.
- For UI work, you MUST connect presentation, events, and state consistently with the framework and repository. You MUST handle the changed flow's async states and cleanup where relevant.
- You MUST check the changed behavior and affected integration points. For presentation changes, you MUST verify interaction, layout, and accessibility as relevant to the request.
- You MUST update documentation when the change alters documented usage or behavior. You MUST remove code made unused by this change, leaving unrelated cleanup out of scope.
- If implementation reveals a required redesign or scope expansion, you MUST explain the evidence and pause that part for a decision; you MUST continue independent authorized work.

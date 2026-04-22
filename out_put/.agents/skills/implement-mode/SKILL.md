---
name: implement-mode
description: Use when implementing requested behavior, modifying code paths, or extending existing functionality while preserving current behavior and scope.
---

# Implement Mode

- You MUST identify the smallest code path that satisfies the requested behavior before editing.
- You MUST extend existing behavior only at the owning integration point for the requested change.
- You MUST NOT rewrite working flows, modules, or interfaces to make the change easier.
- You MUST NOT introduce new abstractions unless at least two current call sites require the same behavior now.
- You MUST preserve existing defaults, side effects, error handling, and ordering unless the request explicitly changes them.
- You MUST keep compatibility shims or fallback behavior when replacing an internal path that existing callers may still use.
- You MUST stop implementation if the requested behavior requires a broader redesign than the accepted scope.

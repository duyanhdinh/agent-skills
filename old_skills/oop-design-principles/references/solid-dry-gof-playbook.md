# SOLID, DRY, and GoF Playbook

## Quick Triage

Use these signals to pick direction quickly:

- Too many reasons to edit one class -> apply SRP and split responsibilities.
- `if/else` by type or role everywhere -> consider OCP + Strategy/State/Factory.
- Child classes break parent assumptions -> review LSP and inheritance design.
- Consumers depend on methods they do not use -> apply ISP and narrower interfaces.
- High-level logic tied to concrete implementations -> use DIP and dependency boundaries.
- Repeated business rules in multiple places -> apply DRY via shared policy/service objects.

## SOLID in Practice

### SRP (Single Responsibility Principle)

- Keep one reason to change per class/module.
- Split orchestration from business policy and IO concerns.

### OCP (Open/Closed Principle)

- Extend behavior via new implementations, not edits to stable core logic.
- Prefer plug-in style dispatch over branching by type.

### LSP (Liskov Substitution Principle)

- Subtypes must preserve contracts (preconditions, postconditions, invariants).
- If subtype needs stricter inputs or weaker guarantees, avoid inheritance.

### ISP (Interface Segregation Principle)

- Expose small role-focused interfaces.
- Avoid "god interfaces" that force no-op implementations.

### DIP (Dependency Inversion Principle)

- High-level policies depend on abstractions, not concrete frameworks.
- Wire implementations at composition boundaries.

## DRY Boundaries

- De-duplicate stable domain knowledge first (rules, invariants, workflows).
- Allow some duplication when contexts are likely to diverge soon.
- Prefer extraction after the second or third meaningful repetition, not at first sight.

## GoF Pattern Selection

Pick only when a clear force exists:

- Need interchangeable algorithms: Strategy.
- Need behavior changes by state: State.
- Need to decouple notification fan-out: Observer.
- Need to adapt incompatible interfaces: Adapter.
- Need controlled object creation variants: Factory Method / Abstract Factory.
- Need stepwise object construction: Builder.
- Need shared traversal/operation on object structures: Visitor.
- Need behavior wrapping without subclass explosion: Decorator.
- Need one consistent entrypoint to subsystem: Facade.

## Pattern Decision Checklist

1. What exact change scenario is currently hard?
2. Which principle is violated now (SOLID/DRY)?
3. What is the simplest non-pattern refactor that could work?
4. If using a pattern, what coupling is reduced and what complexity is added?
5. How will tests prove behavior is preserved?

## GoF Catalog Reference

- Primary reference: https://refactoring.guru/design-patterns/catalog

# Style and Quality Checklist

- Naming is domain-meaningful and consistent.
- Functions and classes have single clear responsibility.
- Files have explicit domain responsibility and are not generic dumping grounds.
- `constants`, `helpers`, and `utils` contain only narrowly scoped code that matches their names.
- Feature logic is split into domain-named files before generic files become catch-alls.
- Error handling is explicit and actionable.
- Logging is structured and avoids sensitive data.
- Tests are deterministic and cover behavior changes.
- Public interfaces are documented with examples.
- Dead code and unused dependencies are removed.
- CI enforces lint, format, and test gates.

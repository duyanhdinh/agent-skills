# Feature Module Template (for scaled projects)

Use this module template after expansion triggers are met (multiple domains, heavy component growth, or team scaling).

## Structure
```text
feature-name/
  components/
    FeatureHero.astro
  pages/
    index.astro
  content/
    intro.md
```

## Rules
- Keep feature-specific components inside the feature folder.
- Keep shared UI in `src/components/ui`.
- Keep global layouts in `src/layouts`.
- Avoid cross-feature imports except via stable shared utilities.

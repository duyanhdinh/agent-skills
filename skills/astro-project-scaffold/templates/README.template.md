# Astro Project Scaffold

Production-ready Astro starter focused on Islands Architecture, performance, and a clean growth path.

## Stack
- Astro + TypeScript
- Vue 3 islands (`@astrojs/vue`)
- Tailwind CSS v4
- Content Collections
- Sitemap integration
- Vercel adapter (default)
- ESLint + Prettier + Vitest + Husky + lint-staged

## Quick Start
```bash
npm install
npm run dev
```

## Core Scripts
```bash
npm run dev
npm run build
npm run preview
npm run lint
npm run format:check
npm run typecheck
npm run test
```

## Suggested `package.json` scripts
```json
{
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    "check": "astro check",
    "lint": "eslint .",
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "typecheck": "tsc --noEmit",
    "test": "vitest run",
    "test:watch": "vitest"
  }
}
```

## Project Organization
- Start flat and predictable under `src/components`, `src/pages`, and `src/content`.
- Use `src/components/islands` only for interactive components.
- Expand to `src/features/*` only when complexity triggers are met.

## Islands Rules
- Default to Astro components/pages with no hydration.
- Add client directives only when interactivity is required.
- Prefer `client:visible` or `client:idle` over `client:load`.

## Deployment
- Default adapter is Vercel.
- Change adapter only when infrastructure requires a different runtime.

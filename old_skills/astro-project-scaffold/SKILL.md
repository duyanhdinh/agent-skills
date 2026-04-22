---
name: astro-project-scaffold
description: Scaffold a production-ready Astro.js project optimized for Islands Architecture, Core Web Vitals, and clean growth from a flat structure to feature-based organization. Use when creating a new Astro codebase for marketing sites, landing pages, blogs, or hybrid applications with Vue 3 as the default UI framework and optional React/Svelte extension.
---

# name
`astro-project-scaffold`

# description
Create an Astro-specific scaffold that is fast by default, easy to maintain, and ready for production delivery.

## when_to_use
Use this skill when:
- A new Astro.js repository must be bootstrapped with clear defaults.
- Islands Architecture and partial hydration are first-class requirements.
- Vue 3 should be enabled by default, with room to add React or Svelte later.
- The team needs Tailwind CSS v4, Content Collections, Sitemap, TypeScript, and a deployment adapter baseline.
- You need a flat initial layout with explicit rules for feature-based expansion.

## tags
- astro
- islands-architecture
- vue
- tailwindcss-v4
- typescript
- performance
- scaffold

## Objective
Generate a clean and scalable Astro starter that:
- Prioritizes static rendering and minimal client JavaScript.
- Uses Vue islands only where interaction is required.
- Includes production-ready developer tooling (ESLint, Prettier, Vitest, Husky, lint-staged).
- Keeps the initial structure flat and organized.
- Defines clear scaling triggers and a migration path to `src/features/`.

## Workflow (detailed steps)
1. Capture project constraints with [templates/project-brief-template.md](templates/project-brief-template.md).
2. Confirm renderer choices:
- Enable `@astrojs/vue` by default.
- Add React or Svelte only if explicitly requested.
3. Create the base structure from "Recommended Project Layout" with only required folders/files.
4. Configure Astro using [templates/astro-config.template.mjs](templates/astro-config.template.mjs):
- Integrations: Vue, Tailwind, Sitemap.
- Adapter: Vercel by default.
5. Configure TypeScript from [templates/tsconfig.template.json](templates/tsconfig.template.json) and include `src/env.d.ts`.
6. Set global layout and styling:
- [templates/base-layout.template.astro](templates/base-layout.template.astro)
- `src/styles/global.css` with Tailwind layers and tokens.
7. Add content system using [templates/content-config.template.ts](templates/content-config.template.ts).
8. Add reusable UI and interactive islands:
- [templates/ui-button.template.vue](templates/ui-button.template.vue)
- [templates/island-example.template.vue](templates/island-example.template.vue)
9. Add project operations and documentation:
- [templates/README.template.md](templates/README.template.md)
- [templates/Makefile.template](templates/Makefile.template)
10. Add CI and quality gates:
- Run lint, typecheck, test, build in CI.
- Enforce pre-commit checks via Husky + lint-staged.
11. Verify output:
- `astro check` passes.
- Lighthouse/Core Web Vitals are acceptable for representative pages.
- Interactive islands are hydrated only where needed.
12. Apply expansion rules only when measurable complexity appears (see Project Structure Guidelines).

## Best Practices
- Default to static pages; use SSR only where request-time data is needed.
- Use `client:visible`, `client:idle`, or `client:media` before `client:load`.
- Keep island boundaries small and purposeful.
- Keep shared utility code framework-agnostic in `src/utils` or `src/shared`.
- Co-locate only what is needed for readability; avoid speculative folders.
- Treat performance budgets as release criteria, not optional checks.
- Keep Markdown/MDX content strongly typed via Content Collections schemas.

## Anti-Patterns
- Hydrating entire page regions that do not need interactivity.
- Converting Astro pages into SPA-like shells by default.
- Adding React/Svelte renderers without explicit feature needs.
- Prematurely introducing deep feature folders in small codebases.
- Mixing content schema logic inside UI components.
- Shipping unoptimized images or blocking scripts in base layout.

## Project Structure Guidelines (flat vs expanded)
### Flat-first (default)
Use this shape for early and mid-size projects:

```text
src/
  assets/
  components/
    ui/
    layout/
    islands/
  layouts/
  pages/
  content/
  styles/
  utils/
  core/
  shared/
  env.d.ts
```

### Expansion triggers
Move toward feature-based structure when one or more apply:
- Multiple distinct domains exist (`blog`, `dashboard`, `shop`, `auth`).
- One component folder exceeds roughly 30-40 components.
- Teams need page/component/content grouping by domain.
- Team size exceeds 3-4 developers and navigation slows down.

### Expanded target

```text
src/
  features/
    blog/
      components/
      pages/
      content/
    dashboard/
      components/
      pages/
    auth/
      components/
      pages/
```

Rule: do not expand preemptively; expand only when complexity is observed.

## Integration Options
| Area | Default | Optional | Guidance |
|---|---|---|---|
| UI renderer | Vue 3 (`@astrojs/vue`) | React (`@astrojs/react`), Svelte (`@astrojs/svelte`) | Install optional renderers only when feature requirements justify them. |
| Styling | Tailwind CSS v4 | CSS Modules, scoped component CSS | Keep design tokens in global styles, localize exceptions. |
| Content | Astro Content Collections | MDX-heavy content flows | Keep schemas in `src/content/config.ts`. |
| Adapter | Vercel (`@astrojs/vercel`) | Netlify/Node/Cloudflare adapters | Switch adapter based on target runtime and deployment constraints. |
| Quality | ESLint + Prettier + Vitest + Husky + lint-staged | Playwright (if E2E required) | Block merges on lint/typecheck/test/build failures. |

## Recommended Project Layout
```text
public/
  images/
  favicon.svg
src/
  assets/
  components/
    ui/
    layout/
    islands/
  layouts/
    BaseLayout.astro
  pages/
  content/
    config.ts
  styles/
    global.css
  utils/
  core/
  shared/
  env.d.ts
astro.config.mjs
tsconfig.json
package.json
.env.example
README.md
Makefile
.github/workflows/ci.yml
```

## Example (astro.config.mjs, BaseLayout.astro, sample island component, content config)
### `astro.config.mjs`
```js
import { defineConfig } from "astro/config";
import vue from "@astrojs/vue";
import tailwind from "@tailwindcss/vite";
import sitemap from "@astrojs/sitemap";
import vercel from "@astrojs/vercel/serverless";

export default defineConfig({
  site: "https://example.com",
  output: "static",
  integrations: [vue(), sitemap()],
  vite: {
    plugins: [tailwind()],
  },
  adapter: vercel(),
});
```

### `src/layouts/BaseLayout.astro`
```astro
---
import "../styles/global.css";

interface Props {
  title: string;
  description?: string;
}

const {
  title,
  description = "Production-ready Astro starter with islands architecture",
} = Astro.props;
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content={description} />
    <title>{title}</title>
  </head>
  <body class="min-h-screen bg-white text-slate-900 antialiased">
    <slot />
  </body>
</html>
```

### `src/components/islands/CounterIsland.vue`
```vue
<script setup lang="ts">
import { ref } from "vue";

const count = ref(0);
</script>

<template>
  <div class="inline-flex items-center gap-3 rounded-lg border border-slate-300 px-4 py-2">
    <button
      type="button"
      class="rounded bg-slate-900 px-3 py-1 text-white"
      @click="count -= 1"
    >
      -
    </button>
    <strong class="min-w-8 text-center">{{ count }}</strong>
    <button
      type="button"
      class="rounded bg-slate-900 px-3 py-1 text-white"
      @click="count += 1"
    >
      +
    </button>
  </div>
</template>
```

Usage in Astro page:
```astro
---
import BaseLayout from "../layouts/BaseLayout.astro";
import CounterIsland from "../components/islands/CounterIsland.vue";
---

<BaseLayout title="Home">
  <h1>Astro Islands Starter</h1>
  <CounterIsland client:visible />
</BaseLayout>
```

### `src/content/config.ts`
```ts
import { defineCollection, z } from "astro:content";

const blog = defineCollection({
  schema: z.object({
    title: z.string().min(3),
    description: z.string().min(10),
    draft: z.boolean().default(false),
    pubDate: z.coerce.date(),
    tags: z.array(z.string()).default([]),
  }),
});

export const collections = {
  blog,
};
```

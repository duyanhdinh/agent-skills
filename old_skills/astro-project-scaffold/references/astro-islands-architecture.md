# Astro Islands Architecture Reference

## Purpose
Use Astro Islands Architecture to ship mostly static HTML and hydrate only the interactive parts of a page. This improves Core Web Vitals by reducing JavaScript payload, parse time, and hydration cost.

## Mental Model
- Server-render the page shell and non-interactive content.
- Treat each interactive widget as an "island."
- Hydrate islands independently with client directives.
- Keep islands small, isolated, and intentional.

## Client Directive Guide
| Directive | Use When | Performance Profile |
|---|---|---|
| `client:load` | Interaction must be available immediately after page load. | Highest cost; use sparingly. |
| `client:idle` | Interaction can wait until main thread is idle. | Better for non-critical widgets. |
| `client:visible` | Widget appears below the fold or later in scroll flow. | Strong default for deferred hydration. |
| `client:media` | Hydrate only under a media query condition. | Useful for device-specific UI. |
| `client:only="vue"` | Skip SSR for component and render only on client. | Use for browser-only dependencies; avoid by default. |

Selection rule:
1. Start with no client directive (pure Astro/SSR/static).
2. If interactivity is required, try `client:visible`.
3. Escalate to `client:idle` or `client:load` only when user experience requires it.

## Performance Benefits
- Lower shipped JavaScript compared to SPA-by-default approaches.
- Faster first contentful paint and time to interactive on content-heavy pages.
- Better cacheability for static routes.
- Reduced hydration contention because each island hydrates independently.

## Comparison With Traditional SPA Frameworks
| Aspect | Astro Islands | Traditional SPA |
|---|---|---|
| Rendering default | Server-rendered/static HTML first | Client-rendered app shell often dominates |
| JS delivery | Opt-in per island | Broad JS bundle by default |
| Hydration scope | Partial, component-level | Full app or large route segments |
| Best fit | Content-first sites with selective interactivity | Highly interactive app-like products |

## Practical Rules
- Keep page templates and content rendering in `.astro` files.
- Use Vue/React/Svelte components only for real interaction.
- Avoid passing large serialized objects into islands.
- Profile with Lighthouse and browser performance tools on representative pages.
- Track bundle growth as a release gate.

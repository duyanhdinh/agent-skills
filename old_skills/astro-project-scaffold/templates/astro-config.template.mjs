import { defineConfig } from "astro/config";
import vue from "@astrojs/vue";
import sitemap from "@astrojs/sitemap";
import tailwind from "@tailwindcss/vite";
import vercel from "@astrojs/vercel/serverless";

// Default scaffold: static output + Vue islands + Tailwind v4 + sitemap.
// Switch adapter/output only when runtime constraints require it.
export default defineConfig({
  site: "https://example.com",
  output: "static",
  integrations: [vue(), sitemap()],
  vite: {
    plugins: [tailwind()],
  },
  adapter: vercel(),
});

import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://blewbury-beer-festival.co.uk",
  integrations: [sitemap()],
});

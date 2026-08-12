import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

const festival = defineCollection({
  loader: glob({ base: "./src/content/festival", pattern: "**/*.{md,mdx}" }),
  schema: z.object({
    name: z.string(),
    year: z.number().int(),
    date: z.coerce.date(),
    venue: z.string(),
    street: z.string(),
    locality: z.string(),
    town: z.string(),
    region: z.string(),
    postcode: z.string(),
    country: z.string().default("GB"),
    strapline: z.string(),
    intro: z.string(),
  }),
});

const news = defineCollection({
  loader: glob({ base: "./src/content/news", pattern: "**/*.{md,mdx}" }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    published: z.coerce.date(),
    updated: z.coerce.date().optional(),
    featured: z.boolean().default(false),
    draft: z.boolean().default(false),
  }),
});

const commonDrinkFields = {
  name: z.string(),
  style: z.string().optional(),
  abv: z.number().min(0).max(60).optional(),
  description: z.string().optional(),

  // Rich detail-page content shared by all drink categories.
  extendedDescription: z.string().optional(),
  origin: z.string().optional(),
  ingredients: z.array(z.string()).default([]),
  character: z.array(z.string()).default([]),
  bestServed: z.string().optional(),
  highlights: z.array(z.string()).default([]),

  graphic: z.string().optional(),
  producerLogo: z.string().optional(),
  producerTown: z.string().optional(),
  producerWebsite: z.string().url().optional(),
  flavourTags: z.array(z.string()).default([]),
  vegan: z.boolean().optional(),
  glutenFree: z.boolean().optional(),
  featured: z.boolean().default(false),
  status: z.enum(["planned", "confirmed", "unavailable"]).default("confirmed"),
  sortOrder: z.number().int().optional(),
};

const beers = defineCollection({
  loader: glob({ base: "./src/content/beers", pattern: "**/*.{md,mdx}" }),
  schema: z.object({
    brewery: z.string(),
    ...commonDrinkFields,

    // Organiser-only. Stored in content, never shown publicly.
    volumePints: z.number().int().positive(),
    format: z.enum(["cask", "keg", "pin"]),
  }),
});

const ciders = defineCollection({
  loader: glob({ base: "./src/content/ciders", pattern: "**/*.{md,mdx}" }),
  schema: z.object({
    producer: z.string(),
    ...commonDrinkFields,

    // Organiser-only. Stored in content, never shown publicly.
    volumePints: z.number().int().positive(),
    format: z.enum(["cask", "keg", "pin"]),
  }),
});

const wines = defineCollection({
  loader: glob({ base: "./src/content/wines", pattern: "**/*.{md,mdx}" }),
  schema: z.object({
    producer: z.string(),
    ...commonDrinkFields,
  }),
});

const gins = defineCollection({
  loader: glob({ base: "./src/content/gins", pattern: "**/*.{md,mdx}" }),
  schema: z.object({
    producer: z.string(),
    ...commonDrinkFields,
  }),
});

const entertainment = defineCollection({
  loader: glob({ base: "./src/content/entertainment", pattern: "**/*.{md,mdx}" }),
  schema: z.object({
    name: z.string(),
    kind: z.enum(["music", "entertainment", "other"]).default("music"),
    description: z.string(),
    image: z.string().optional(),
    startTime: z.string().optional(),
    endTime: z.string().optional(),
    website: z.string().url().optional(),
    featured: z.boolean().default(false),
    status: z.enum(["planned", "confirmed", "cancelled"]).default("confirmed"),
    sortOrder: z.number().int().optional(),
  }),
});

const food = defineCollection({
  loader: glob({ base: "./src/content/food", pattern: "**/*.{md,mdx}" }),
  schema: z.object({
    vendor: z.string(),
    description: z.string(),
    vegetarian: z.boolean().optional(),
    vegan: z.boolean().optional(),
    glutenFree: z.boolean().optional(),
    website: z.string().url().optional(),
    featured: z.boolean().default(false),
    status: z.enum(["planned", "confirmed", "cancelled"]).default("confirmed"),
    sortOrder: z.number().int().optional(),
  }),
});

const goodCauses = defineCollection({
  loader: glob({ base: "./src/content/good-causes", pattern: "**/*.{md,mdx}" }),
  schema: z.object({
    name: z.string(),
    description: z.string(),
    image: z.string().optional(),
    website: z.string().url().optional(),
    featured: z.boolean().default(false),
    year: z.number().int().optional(),
    sortOrder: z.number().int().optional(),
  }),
});

const sponsors = defineCollection({
  loader: glob({ base: "./src/content/sponsors", pattern: "**/*.{md,mdx}" }),
  schema: z.object({
    name: z.string(),
    description: z.string(),
    website: z.string().url().optional(),
    logo: z.string().optional(),
    featured: z.boolean().default(false),
    status: z.enum(["prospective", "confirmed", "inactive"]).default("confirmed"),
  }),
});

export const collections = {
  festival,
  news,
  beers,
  ciders,
  wines,
  gins,
  entertainment,
  food,
  goodCauses,
  sponsors,
};

# Blewbury Beer Festival Website Architecture

## Status

Current architecture as of August 2026.

## Principles

The site is:

- static-first
- content-driven
- validated at build time
- hosted without an always-running application server
- maintained through Git
- deliberately lightweight

## Front End

The public website is built with Astro.

Astro generates static HTML for the public site. JavaScript is added only where required.

## Content

Repeatable festival content is stored using Astro Content Collections.

Current collections:

- `festival`
- `news`
- `beers`
- `entertainment`
- `food`
- `good-causes`
- `sponsors`

Collection schemas live in:

`src/content.config.ts`

Content entries live below:

`src/content/`

## Why Content Collections

Content Collections provide:

- schema validation
- typed content
- predictable data structures
- simple Markdown authoring
- separation of content from presentation
- safe future developer tooling

A malformed content entry should fail the build rather than silently produce a broken page.

## Editorial Workflow

The long-term editorial workflow is:

1. Add or update a content entry.
2. Run the local build.
3. Review the site.
4. Commit the change.
5. Push to GitHub.
6. AWS Amplify deploys the static site.

Future CLI commands may create content entries, but should not rewrite existing page source.

## Hosting

Target production hosting is AWS Amplify Hosting.

The current WordPress/Lightsail site remains live until the Astro replacement has been tested and the production domain is ready to move.

## Migration Strategy

Migration is incremental.

The existing `festival.ts` data remains temporarily in place while pages are converted to Content Collections one at a time.

This avoids a large-bang migration.

Planned order:

1. Create and validate Content Collections.
2. Convert News.
3. Convert Drinks.
4. Convert Entertainment.
5. Convert Food.
6. Convert Good Causes and Sponsors.
7. Remove duplicated legacy data only after nothing references it.

## Developer Tooling

Python tooling is used for:

- validation
- audits
- content creation
- migration utilities
- image optimisation
- release checks

Python tooling should not perform fragile source-code rewrites.

## Deployment Philosophy

Keep infrastructure proportional to the site's needs.

No database, application server or CMS should be introduced unless a real requirement justifies it.

# ADR-001: Use Astro for the Public Website

**Status:** Accepted  
**Date:** 2026-08-08

## Context

The Blewbury Beer Festival website is primarily a static content website.

Its main requirements are:

- fast page delivery
- low hosting cost
- simple maintenance
- excellent mobile performance
- straightforward deployment
- no dependency on a traditional CMS

WordPress provides substantially more complexity than the site requires.

## Decision

Use Astro as the primary web framework.

Astro will generate static HTML for the public site, with JavaScript added only where genuinely required.

## Consequences

### Positive

- Very fast pages
- Minimal browser JavaScript
- Excellent fit for static content
- Straightforward component model
- Easy deployment to AWS Amplify
- Content can be stored directly in the repository

### Negative

- Editing content requires repository changes rather than a traditional CMS
- Contributors need a Git-based workflow or a future editing interface

## Review

Revisit only if future requirements make a static-first architecture unsuitable.

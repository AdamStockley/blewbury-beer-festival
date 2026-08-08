# ADR-004: Remove WordPress from the Festival Website

**Status:** Accepted  
**Date:** 2026-08-08

## Context

The existing website uses WordPress on AWS Lightsail.

The site does not require dynamic page generation, database-backed publishing, user comments, e-commerce, plugins or server-side PHP.

## Decision

The replacement website will not use WordPress.

The current WordPress site will remain live during development and migration.

It will be decommissioned only after the replacement site is tested and the production domain has been moved successfully.

## Consequences

### Positive

- Reduced security surface
- Reduced maintenance
- Reduced hosting cost
- No plugin dependency
- No WordPress updates
- No database maintenance

### Negative

- Existing WordPress editing workflows disappear
- Relevant content must be migrated

## Migration Principle

Do not destroy or modify the current production installation until the new site is proven in production.

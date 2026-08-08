# ADR-002: Use AWS Amplify Hosting

**Status:** Accepted  
**Date:** 2026-08-08

## Context

The existing site is hosted on AWS Lightsail using WordPress.

This requires an always-running server and associated maintenance despite the website being primarily static.

The replacement requires:

- HTTPS
- custom domain support
- CDN delivery
- automatic deployment
- low operating cost
- minimal infrastructure management

## Decision

Deploy the Astro site using AWS Amplify Hosting.

GitHub will act as the source repository and production deployments will be triggered from the configured production branch.

## Consequences

### Positive

- No continuously running server
- No WordPress/PHP/MySQL infrastructure
- Integrated CDN
- Managed HTTPS
- Simple Git-based deployment
- Very low cost for expected traffic

### Negative

- Some AWS-specific deployment configuration
- A future migration would require changing hosting configuration

## Review

Review if traffic, functionality or AWS pricing materially changes.

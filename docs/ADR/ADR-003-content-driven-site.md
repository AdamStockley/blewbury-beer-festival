# ADR-003: Use Structured, Content-Driven Pages

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Festival information changes progressively as the event approaches.

Examples include beers, breweries, performers, food vendors, sponsors, beneficiaries and news.

Hard-coding individual entries into page templates would increase maintenance effort and create inconsistency.

## Decision

Store repeatable festival information as structured data or content records.

Page templates and reusable components will render those records consistently.

## Consequences

### Positive

- Easier content maintenance
- Consistent presentation
- Supports "coming soon" states cleanly
- Future filtering and search become easier
- Reusable across future festival years

### Negative

- Requires a defined content schema
- Schema changes need to be managed carefully

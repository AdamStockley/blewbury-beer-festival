from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent


DOCS = {
    "docs/ADR/ADR-001-use-astro.md": """
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
""",
    "docs/ADR/ADR-002-use-aws-amplify-hosting.md": """
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
""",
    "docs/ADR/ADR-003-content-driven-site.md": """
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
""",
    "docs/ADR/ADR-004-remove-wordpress.md": """
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
""",
    "docs/ADR/ADR-005-no-ticket-sales.md": """
# ADR-005: Do Not Build Ticketing or E-commerce

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Blewbury Beer Festival currently has no requirement for advance ticket sales.

Adding ticketing would introduce unnecessary complexity including payment processing, customer records, refunds, compliance obligations and greater security requirements.

## Decision

Do not build ticket sales, payment processing or e-commerce functionality.

The site will remain an information and promotion platform unless the organising committee's requirements change.
""",
    "docs/ADR/ADR-006-photography-optional.md": """
# ADR-006: Do Not Depend on Event Photography

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Photography from previous events may contain identifiable individuals.

Using such photography can create permission and privacy concerns.

## Decision

Design the website so that it looks complete without photography.

The primary visual language will use typography, colour, geometric layouts, festival-poster graphics, illustration and approved branding assets.

Photography may be added when appropriate usage rights and permissions are clear.
""",
    "docs/ADR/ADR-007-concise-homepage.md": """
# ADR-007: Keep the Homepage Concise

**Status:** Accepted  
**Date:** 2026-08-08

## Context

An early homepage design contained substantial explanatory content and several large sections.

Although visually effective, this created excessive scrolling, particularly on mobile devices.

## Decision

The homepage should remain deliberately concise.

It should answer:

1. What is the event?
2. When is it?
3. Where is it?
4. Why should I attend?

Detailed information belongs on dedicated pages.

## Target Structure

- Hero
- Compact countdown
- Beer / Music / Food summary
- Good Causes summary
- Latest announcement
- Footer / Volunteer CTA
""",
    "docs/ADR/ADR-008-reusable-design-system.md": """
# ADR-008: Build a Reusable Design System

**Status:** Accepted  
**Date:** 2026-08-08

## Context

The site will contain several pages with related visual requirements.

A future Blewbury Cricket Club redesign may also benefit from reusable structural ideas, although it should retain its own visual identity.

## Decision

Implement reusable components and shared design tokens for typography, spacing, colours, buttons, navigation, cards, section headings, calls to action and footer patterns.

Components should be reusable without forcing every Blewbury website to look identical.
""",
    "docs/wireframes/HOMEPAGE.md": """
# Homepage Wireframe

**Status:** Current direction  
**Date:** August 2026

The homepage should be deliberately concise.

## Structure

```text
NAV

BLEWBURY
BEER FESTIVAL

Saturday 3 October 2026
Blewbury, Oxfordshire

[ PLAN YOUR VISIT ]

COUNTDOWN

BEER | MUSIC | FOOD
compact teaser cards

DRINKING BEER. DOING GOOD.
short explanation + link

LATEST
one current announcement

VOLUNTEER / CONTACT / FOOTER
```

## Mobile Principle

The mobile homepage should remain short.

Avoid expanding every desktop element into a large vertical feature section.

Cards should be compact and easy to scan.

## Homepage Exclusions

Do not place the following in full on the homepage:

- complete beer lists
- performer biographies
- full entertainment timetable
- food menus
- parking instructions
- FAQs
- sponsor directory
- previous festival history
- long-form festival narrative
""",
    "docs/wireframes/PAGE_LAYOUTS.md": """
# Standard Page Layouts

## General Content Page

Used for Visit, Good Causes and Volunteer.

```text
Header

Page Hero
- Eyebrow
- H1
- Short introduction

Primary Content

Optional CTA

Footer
```

## Collection Page

Used for Beer, Music and Food.

```text
Header

Page Hero

Intro / status message

Filters (future, only if useful)

Content cards

Supporting information

Footer
```

## News Article

```text
Header

Article title
Date
Optional category

Readable-width article body

Back to News

Footer
```

## Mobile Rules

- Keep content in natural document order.
- Avoid unnecessary side-by-side layouts.
- Avoid oversized vertical whitespace.
- Use 44px minimum interactive targets.
- Keep navigation simple.
- Do not make users scroll through decorative content to reach useful information.
""",
    "docs/assets/README.md": """
# Design Assets

This directory contains design-system assets used in project documentation.

Potential future assets include:

- colour palette reference
- typography samples
- spacing reference
- approved logos
- festival motif development
- icon reference

Only committed, approved design assets should live here.
""",
    "docs/assets/logo-development/README.md": """
# Logo and Motif Development

This directory is reserved for future logo or graphic motif development.

The current website does not depend on a new logo.

Potential directions include:

- stylised hop cone
- circular festival stamp
- abstract pint/glass motif
- barley or hop geometry
""",
    "docs/DEVELOPER_WORKFLOW.md": """
# Developer Workflow

## Principle

Prefer repeatable tooling over manual file editing.

## Conventions

Use:

- Git for version control
- Python for multi-file generation or transformation
- small shell commands for Git and build operations
- one logical change per commit

Avoid:

- large heredoc shell scripts
- manual repetitive edits
- untracked one-off transformations

## Standard Change Flow

1. Check repository status.
2. Run or create a repeatable tool.
3. Review the diff.
4. Build the site.
5. Commit one logical change.

## Tooling

Project utilities live in `tools/`.

Scripts should be safe to re-run, create missing directories, overwrite only files they own, print what they changed, and fail clearly if something unexpected happens.
""",
}


def _write(root: Path, relative: str, content: str, check_only: bool) -> bool:
    path = root / relative
    wanted = dedent(content).lstrip()
    current = path.read_text(encoding="utf-8") if path.exists() else None
    changed = current != wanted

    if check_only:
        status = "DIFF" if changed else "OK"
        print(f"{status:4} {relative}")
        return changed

    path.parent.mkdir(parents=True, exist_ok=True)
    if changed:
        path.write_text(wanted, encoding="utf-8")
        print(f"WROTE {relative}")
    else:
        print(f"OK    {relative}")
    return changed


def run(args: argparse.Namespace, root: Path) -> int:
    changed = 0
    for relative, content in DOCS.items():
        changed += int(_write(root, relative, content, args.check))

    if args.check:
        print(f"\n{changed} documentation file(s) differ.")
        return 1 if changed else 0

    print(f"\nDocumentation complete. {changed} file(s) changed.")
    return 0


def register(subparsers) -> None:
    parser = subparsers.add_parser(
        "docs",
        help="Create or refresh project documentation.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check whether generated docs are current without changing files.",
    )
    parser.set_defaults(func=run)

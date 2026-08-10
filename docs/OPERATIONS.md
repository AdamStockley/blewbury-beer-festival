# Blewbury Beer Festival Website -- Operations Manual

**Version:** 1.0\
**Status:** Production\
**Last updated:** 10 August 2026

------------------------------------------------------------------------

# Purpose

This document is the operational handbook for the Blewbury Beer Festival
website. It is intended to allow future maintenance without relying on
prior knowledge of the migration project.

------------------------------------------------------------------------

# System Overview

The site is built with Astro and hosted on AWS Amplify Gen 2.

Core components:

-   Astro static frontend
-   AWS Amplify Gen 2
-   CloudFront CDN
-   Route 53 DNS
-   API Gateway
-   AWS Lambda
-   Amazon SES
-   Cloudflare Turnstile

------------------------------------------------------------------------

# Resource Inventory

## AWS

-   Account: 950645756314
-   Region: eu-west-2
-   CLI profile: las-dev
-   Amplify App ID: d2nh6jvn6p8uji

## Domains

-   https://blewbury-beer-festival.co.uk
-   https://www.blewbury-beer-festival.co.uk
-   Amplify preview: https://main.d2nh6jvn6p8uji.amplifyapp.com

## Repository

https://github.com/AdamStockley/blewbury-beer-festival

------------------------------------------------------------------------

# Repository Structure

-   amplify/
    -   backend.ts
    -   functions/
-   public/
    -   images/
    -   favicon.ico
-   src/
    -   components/
    -   pages/
    -   styles/
-   docs/

------------------------------------------------------------------------

# Deployment

Deployments are automatic.

    git add .
    git commit -m "Description"
    git push origin main

Amplify builds frontend and backend.

The build intentionally uses `npm install` rather than `npm ci`.

------------------------------------------------------------------------

# Forms

General Contact

-   API Gateway
-   Lambda
-   SES

Sponsor a Barrel

-   API Gateway
-   Lambda
-   SES

Both are protected by Cloudflare Turnstile.

------------------------------------------------------------------------

# Turnstile

If adding a new hostname update:

1.  Cloudflare hostname list
2.  Lambda ALLOWED_HOSTNAMES
3.  API Gateway CORS

Remember hostname changes can take several minutes to propagate.

------------------------------------------------------------------------

# DNS

Managed in Route53.

Production points to Amplify-managed CloudFront.

Legacy Lightsail records have been removed.

------------------------------------------------------------------------

# Smoke Test

After every deployment verify:

-   Homepage
-   Drinks
-   Food
-   Music
-   Sponsors
-   Contact
-   Sponsor form
-   Email delivery
-   Turnstile
-   Mobile navigation
-   Custom 404
-   robots.txt
-   sitemap-index.xml

------------------------------------------------------------------------

# Troubleshooting

## Build fails

Check Amplify deployment logs.

## Form fails

Check browser console then:

-   API Gateway
-   Lambda logs
-   CORS

## Email fails

Check:

-   SES
-   Lambda
-   Amplify secrets

## Turnstile fails

Check:

-   Site key
-   Secret
-   Allowed hostnames
-   Browser console

------------------------------------------------------------------------

# Annual Release Checklist

Before each festival:

-   Update drinks
-   Update food vendors
-   Update entertainment
-   Update sponsors
-   Update good causes
-   Publish latest news
-   Test all forms
-   Verify email delivery
-   Check sitemap
-   Test mobile
-   Review accessibility

------------------------------------------------------------------------

# Migration History

Completed August 2026.

Removed:

-   WordPress
-   Beer Festival Lightsail instance
-   Beer Festival static IP
-   Unused Lightsail static IP

Remaining Lightsail resources belong to Blewbury Cricket Club.

------------------------------------------------------------------------

# Future Enhancements

-   Producer pages
-   Extended wine notes
-   Gin guide
-   Analytics
-   Committee editing workflow

------------------------------------------------------------------------

# Design Principles

The website should remain:

-   Static-first
-   Serverless
-   Low-cost
-   Secure
-   Source-controlled
-   Easy to understand
-   Easy to deploy

When in doubt, prefer simple managed AWS services over self-managed
infrastructure.

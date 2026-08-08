# Drinks Companion v1

## Purpose

The Drinks area is designed for use both before and during the festival.

QR codes around the venue can point to:

- `/drinks` for the complete bar
- `/drinks/<drink-id>` for an individual drink

## Individual Drink Pages

Every confirmed beer, cider, wine and gin can automatically receive its own page.

Current examples:

- `/drinks/mysterious-brewing-jurgen`
- `/drinks/little-ox-daydreamer`
- `/drinks/tutts-clump-reading-gold`

## Public information

Individual pages can show:

- official product artwork
- producer
- product name
- style
- ABV
- visitor description
- flavour tags
- producer location
- producer website
- dietary information where confirmed

Operational serving format and stock volume remain hidden.

## Festival Favourites

Individual drink pages include an optional favourite button.

Favourites are stored only in the visitor's browser using `localStorage`.

There is:

- no account
- no login
- no server database
- no personal data collection

## Artwork policy

Preferred artwork order:

1. official pump clip
2. official product label / bottle / can artwork
3. official producer logo
4. graphical placeholder

Only known-approved or otherwise suitable official promotional artwork should be committed.

## Wine and Gin

The dynamic page architecture already supports wine and gin collections.

Their index placeholders remain until the 2026 selections are confirmed.

# Drink Tasting Passport v4

## Decision

The previous Favourite model has been removed.

Each drink now has one of three local states:

- Not tried
- Liked
- Not for me

## Interaction

Each row has:

- 👍 Like
- 👎 Not for me

Selecting the active option again resets the drink to Not tried.

The states are mutually exclusive.

## Filters

The Drinks page can be filtered by tasting status:

- All tastings
- Liked
- Not for me
- Not tried

This works alongside the existing:

- text search
- type
- style
- ABV

## My Festival Passport

The summary shows:

- number tried
- number liked
- number marked Not for me

## Privacy

Ratings are stored in browser `localStorage` only.

Storage key:

`bbf-2026-drink-ratings`

There is no account, server storage or personal-data collection.

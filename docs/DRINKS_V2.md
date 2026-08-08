# Drinks Experience v2

## Scope

Version 2 of the Drinks experience includes:

- 11 confirmed beers
- 2 confirmed ciders
- visitor-friendly drink descriptions
- optional approved artwork support
- wine placeholder
- gin placeholder
- responsive desktop/tablet/mobile layouts
- operational stock fields retained but hidden publicly

## Artwork

Each beer and cider supports an optional `graphic` field.

Example:

```yaml
graphic: "/images/drinks/loddon-hullabaloo.png"
```

Artwork should only be added where there is a suitable official or approved asset.

Cards intentionally remain visually complete without artwork.

## Future Content

Once supplied, wine and gin products can be added to their collections and the placeholders replaced with product listings.

No custom CMS or drink-entry CLI is required at present.

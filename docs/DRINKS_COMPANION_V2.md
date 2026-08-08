# Drinks Companion v2

## Goals

Version 2 is optimised for people using the site on their phones during the festival.

## Improvements

- All artwork occupies an identical fixed-height area.
- Real artwork and fallback artwork align consistently.
- Flavour notes are displayed as readable pills.
- Cards have restrained hover/lift behaviour on pointer devices.
- Search works by drink name, producer, style and flavour tag.
- Filters are provided for drink type and ABV.
- Wine and Gin remain visible but disabled in filters until lists are confirmed.
- Favourite hearts are available directly from the drinks list.
- A Festival Passport summary shows the number of drinks saved on that device.

## Privacy

Festival Passport favourites use browser `localStorage` only.

No personal data is sent anywhere.

## Serving / Stock Data

`format` and `volumePints` remain available in content for organisers but are deliberately omitted from the public interface.

## Next visual step

Continue replacing fallback artwork with official producer-supplied:

1. pump clips
2. labels / bottle / can graphics
3. producer logos

The layout does not need to change when artwork is added.

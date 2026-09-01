# Dr. Dobby — redesign

Static site, no build step needed to run it. Preview it with:

```
python3 build/serve.py          # http://127.0.0.1:8777
```

That server sends `Cache-Control: no-store`, so edits to `site.css` / `site.js` show up
on a plain reload. Plain `python3 -m http.server` works too, but Chrome will cache the
stylesheet and you'll need a hard reload (⇧⌘R) after every change.

## Structure — five pages × three languages

Same information architecture as doctordobby.com: a short landing that points
into full inner pages.

```
index.html                      EN  home
services/                           all 10 services
pet-shop/                           the three categories
installations/                      the five rooms
contact/                            details, map, form

es/  es/servicios/  es/tienda-mascota/  es/instalaciones/  es/contacto/
ru/  ru/servisy/    ru/zoomagazin/      ru/infrastruktura/ ru/kontakty/

assets/site.css                 all styles
assets/site.js                  all behaviour, incl. the 3D logo
assets/logo.png                 the original logo, background removed
assets/dobby-silhouette.svg     the traced doberman on its own
build/build-pages.py            regenerates all 15 pages from one template
build/serve.py                  local preview server, no caching
```

The landing carries only teasers — three service cards, the pet-shop band, the room
names as chips, and a contact strip — each linking to the page that holds the full
text, exactly like the original. Every page links to its own counterpart in the other
two languages, so switching language keeps you where you were.

## What changed vs. doctordobby.com

- **Removed:** Grooming salon, Team (nav, sections, footer links) in all three languages.
- **Kept, verbatim:** every other text, taken from the live site in each language —
  EN `/en/…`, ES `/`, `/servicios/`, `/instalaciones/`, `/tienda-mascota/`,
  RU `/ru/…`.

Two paragraphs are written rather than taken, because the source has none:
the Russian *Игрушки и аксессуары* description (their CMS shows the oral-hygiene text
there by mistake), and the Russian contact intro (theirs is a leftover Spanish line).
The short call-to-action blocks that close each inner page are also mine.

## Editing text

Don't edit the HTML by hand — 15 files drift apart fast. Edit the language
dictionaries in `build/build-pages.py`, then:

```
python3 build/build-pages.py
```

Markup, CSS classes and script stay identical across all pages; only the strings differ.
To move to `/en/ /es/ /ru/` directories, or to put Spanish at the root the way the
current site does, change `PATHS` at the top of that file and rebuild — every internal
link, `hreflang` and asset path is computed from it.

## Colours — sampled from the logo file

| Token | Value | Where it comes from |
|---|---|---|
| `--violet` | `#a24eea` | "Dr. Dobby" wordmark |
| `--violet-900` | `#3d1668` | dark shade, footer + headings |
| `--peach` | `#f8b07c` | the logo disc |
| `--ink` | `#14101a` | the doberman silhouette |
| `--rule` | `#b2b2b2` | the divider under the wordmark |

The peach disc behind the dog — in the hero and at the top of every inner page — carries
the logo's violet ring, drawn as a `radial-gradient` stop so it scales with the disc
instead of needing a fixed border width.

## The logo

`assets/logo.png` is the original logo from `2026-08-31 18.48.04.jpg` with the white
background keyed out — each fringe pixel was un-matted against the nearest logo colour,
so the edges stay clean on any background. It sits in the header of all 15 pages.
It is 371×156, about 2.5× the size it renders at, so it stays sharp on retina.
**If the client has the original vector file, drop it in as `assets/logo.svg` and swap
the `<img src>`** — that is the only real upgrade left for the mark.

It sits in the footer too. The footer used to be dark violet, which swallowed the black
dog and the grey strapline; rather than build a second, altered mark for dark grounds,
the footer itself is now warm sand (`--sand`) with a peach rule on top — so one logo file
serves the whole site, untouched.

## The 3D logo

`assets/dobby-silhouette.svg` is the doberman traced from the logo JPG. The same path is
inlined in every page as `<symbol id="dobby">` and does several jobs: the flat fallback,
the disc motif at the top of each inner page, the pet-shop watermark, and the source
shape for the 3D model.

The model is **not** an extrusion, and it is not a flat cut-out either. The page reads
that outline, builds a signed distance field from it, and drives a rounded height profile
off the field — so the outline stays exactly the logo's while the body becomes a smooth,
sculpted volume. It then **splits the shape where the legs part company with the chest**:
the torso is meshed once, the legs are meshed once and instanced on both flanks, so the
dog stands on four legs and reads as a real animal when it turns. Normals are computed
analytically from the field gradient, so the shading is smooth with no welding pass.
Around **89 000 triangles** on screen, built in roughly **170 ms** — once, off the critical
path, while the flat SVG is still showing (a smaller grid on phones).

The split line is found automatically — the first scanline below the chest that cuts two
spans, both already leg-narrow — so it still works if the silhouette is ever replaced.

Rendered with Three.js **WebGPURenderer** and TSL node materials, pinned to `0.185.1`.

- **Only the home page** loads it — the import map and the `preconnect` are emitted there
  and nowhere else, so the inner pages stay light.
- The dog is **pure black**, like the silhouette in the logo. Nothing tints it — the
  volume reads through specular alone, and the lights are white with one faint warm
  bounce off the peach disc.
- WebGPU where available, automatic **WebGL2 fallback** everywhere else (both tested).
- Loaded lazily, only when the hero is near the viewport.
- Skipped entirely under `prefers-reduced-motion` or Data Saver — the flat SVG stays.
- If the CDN or the GPU fails, the flat SVG stays and nothing else breaks.

## Typography

EN/ES use **Bricolage Grotesque** (display) + **Instrument Sans** (text) + **IBM Plex Mono**
(labels, hours, phone numbers). Neither of the first two ships Cyrillic, so the Russian
pages load **Unbounded** + **Onest** instead, with the same IBM Plex Mono. The swap is a
`html[lang="ru"]` block in `site.css`; nothing else about the Russian pages differs.

## Photos

The design works with none. If you get photos, the slots are ready:

- **Installations** — replace the `<svg>` inside `.inst__plate` with `<img src="…" alt="…">`.
  The plate is square, `object-fit: cover`, already rounded and clipped.
- **Pet shop** — `.pcard` has room above the heading for a 16:9 image.

Don't put a photo in the hero: the 3D mark is the hero.

## Still to wire up

- The contact form validates and confirms in the browser but sends nothing.
  Point it at a mail endpoint (Formspree, a PHP handler, whatever the host offers).
  It lives on `contact/` only, in all three languages.
- Privacy Policy / Cookies Policy / Legal Notice link to `#` everywhere.
## The map

`contact/` carries a real slippy map — streets, buildings, house numbers — drawn with
**Leaflet 1.9.4** over standard **OpenStreetMap** tiles. No API key and no cookies, so the
page still needs no consent banner; Leaflet's own flagged attribution prefix is cleared and
the required OSM credit stays. It loads from cdnjs only when the block comes near the
viewport, and if that fails the flat sketch underneath simply stays — the block is never
empty. Wheel-zoom is off until you click into the map, so the page keeps its own scroll.

The marker is **the logo**, not a generic pin: the peach disc with its violet ring and the
doberman inside it, on a violet tail so it still points at the door.

Coordinates live in `GEO` in `build-pages.py` — `36.552841, -4.6163597`, the clinic's own
Google listing, cross-checked against an OSM geocode of the street. **Note the `pb=` embed
still on doctordobby.com predates that listing and sits about 250 m west of the real door**,
so it is deliberately not the source.

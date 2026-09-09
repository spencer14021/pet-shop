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
assets/promos.json              the promotions, written in the panel
assets/logo.png                 the original logo, background removed
assets/dobby-silhouette.svg     the traced doberman on its own
admin/index.html                the promotions panel, in Russian
admin/save.php                  its save endpoint, password-guarded
build/build-pages.py            regenerates all 18 pages from one template
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

## The promotions panel

`/admin/` is where the client writes the monthly promotion herself, in Russian,
with all three languages of the text on one card. Everything she writes lands in
`assets/promos.json`; `site.js` reads that file on every page and builds the window
from it, so **a new promotion changes no page and needs no rebuild**.

**The window never opens by itself.** A running promotion puts a coin marked `%` in
the bottom-left corner, opposite the recommendation pill, and an entry in the menu
after the last page; the window opens when one of them is clicked, as often as it is
clicked. `?promo` on any address opens it on load — that is how the panel's three
check links work. There is no picture in it and nothing to time: text, a button, and
the two ways in.

The panel finds out for itself how it can save, by asking `admin/save.php` on load:

- **PHP on the host** — password field and “Сохранить на сайт”. `save.php` narrows
  the request to the fields the panel owns, keeps the previous version as
  `assets/promos.backup.json`, and writes through a temp file and a rename, so a
  visitor loading the site mid-save gets one whole version or the other.
  **The password is a constant at the top of `save.php`** and it refuses to write
  while that constant is still the shipped placeholder.
- **No PHP** — the panel says so and switches to “Скачать promos.json”, which the
  client uploads to `assets/` with a file manager. Nothing else changes.

`build/serve.py` answers the same endpoint locally, reading the password out of
`save.php`, so the whole round trip can be tried here before anything is uploaded.

The coin is stacked discs turned with CSS 3D rather than the hero's WebGPU pipeline,
which is loaded on the home page alone — a 44px badge on all eighteen pages is no
reason to ship a renderer.

**The window only ever speaks the language of the page it is on.** A promotion
written in Russian and shown to an English reader cannot be acted on, so a language
that has no title stays quiet — and to keep that from meaning "no promotion for the
other two", the panel fills the empty languages by machine translation
(`api.mymemory.translated.net`, free, no key) when the client saves, or on the
card's «Перевести» button. The translation lands in the fields for her to correct,
and all three languages are stored in `promos.json`: the site itself translates
nothing and depends on no service at runtime. If the service is down, the panel says
so and saves what there is.

The CTA button is picked from the site's own pages by name (`page:contact`) rather
than by path: one promotion serves all three languages, and `site.js` fills in
`ru/kontakty/` or `es/contacto/` from the page it is building the window on. That
list is `PAGES` in `site.js` — the same six pages as `PATHS` here, and renaming a
page means renaming it in both.

## Moving the site to another domain

Copy the folder. Nothing in a page, in the panel or in `promos.json` carries a
domain: every link, asset path, `hreflang` and the panel's own data path is worked
out relative to the file asking for it, so the site runs the same at a new domain
or from a subfolder of one (`example.com/dobby/`). The single exception is
`SITE_URL` in `build/build-pages.py`, which feeds the structured-data record and
the sender name on the forms — change it and rebuild.

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

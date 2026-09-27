# FoundRy visual assets

Original vector artwork created for the September 2026 README makeover. The
palette follows the repository's Glee-fully brand profile v1.1.0: paper
`#f6f2ee`, surface `#fffdfa`, ink `#2e2b29`, pink `#d94f63` and teal `#2d6f7e`.
The toolbox represents useful building blocks; the sparkle connects to the
application's existing masthead. No stock art, external fonts or image service
is required. Assets follow the repository's [license](../../../LICENSE.md).

## Files

| Source or export | Purpose |
|---|---|
| [cover.svg](cover.svg) | Editable 1280 × 640 cover; system-font fallback typography |
| [social-preview.png](social-preview.png) | Raster cover for the README and social-preview upload |
| [icon.svg](icon.svg) | Editable 512 × 512 full-color browser icon |
| [favicon.ico](favicon.ico) | Multi-resolution 16, 32 and 48 px browser fallback |
| [favicon-16.png](favicon-16.png), [favicon-32.png](favicon-32.png) | Explicit small browser icons |
| [apple-touch-icon.png](apple-touch-icon.png) | 180 × 180 home-screen image |
| [icon-192.png](icon-192.png), [icon-512.png](icon-512.png) | Manifest shortcut icons |
| [icon-maskable-512.png](icon-maskable-512.png) | Opaque paper background; entire mark fits within the central safe circle |
| [safari-pinned-tab.svg](safari-pinned-tab.svg) | Monochrome silhouette, tinted teal by the HTML mask-icon link |

PNG exports were rasterized from the SVG sources using Sharp; Pillow packaged
the ICO sizes. These are authoring tools only, not application dependencies.
The maskable export places the full icon at 320 × 320 in a 512 × 512 paper square.
When changing a source, regenerate its derived images and visually check the
smallest favicon and the social cover. Preserve the declared dimensions.

## Where metadata takes effect

The [application HTML](../index.html) wires the title, description, theme color,
favicon, touch icon, Safari mask icon, [manifest](../site.webmanifest), Open Graph
and Twitter card tags. The image tags use the public repository's raw PNG URL;
that URL becomes available when these assets reach `main`. Local browser icons
use local paths and work without a network connection while the server runs.

The app is loopback-only and marked `noindex, nofollow`. External crawlers cannot
reach it. Sharing tags describe its identity but do not create a publicly
crawlable application. No public app URL, offline guarantee, service worker or
hosted deployment is implied by the manifest. A saved shortcut still needs the
local Python server and the same local origin/port.

## GitHub repository social preview

README Markdown cannot override GitHub's HTML metadata. The cover is embedded
in the README, but the repository social-preview setting is independent.

1. Open this repository's **Settings → General → Social preview**.
2. Choose **Edit → Upload an image** and upload [social-preview.png](social-preview.png).
3. Check the crop and save. Test a repository link after the host refreshes its cache.

Committing these files does not itself configure that GitHub setting. The PNG is
ready for upload; do not report repository sharing previews as configured until
that setting has been verified.

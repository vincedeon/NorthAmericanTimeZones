# North American Time Zones — standalone edition v1.6

A live time zone map and clock page for Canada, the United States (including Puerto Rico and the US Virgin Islands) and Mexico.
Original by Vince d'Eon, VE6LK (CC0): https://github.com/vincedeon/NorthAmericanTimeZones
Standalone edition by Tom Salzer, KJ7T. Both the original and this edition are CC0 (public domain).

## Using it

Double-click `time-zones-local.html` in the main folder of this repository (or open the GitHub Pages link). Everything (libraries and map data) is inside that one
file, so it runs with no internet connection and no web server. Copy it to any machine.

- **UTC clock** at the top, with seconds (can be turned off). All clocks use fixed-width digit cells, so nothing shifts sideways as the time ticks.
- **+1 day / −1 day markers** on cards, sub-area lines and map labels wherever the date differs
  from your home zone's date (from UTC if no home is set) — e.g. Guam is usually “Thu · +1 day”.
- **Home zone** clock and gold outline on the map. Auto-detected from the computer's time
  zone, or chosen in Settings.
- **Kiosk mode**: map and clocks fill the window; mouse pointer and buttons hide after
  3 seconds. Press `K` (or the Kiosk button) to toggle, `F` for full screen, `Esc` to exit.
- **Settings** (`S` or the gear button): home zone, 12/24-hour, UTC seconds, light/dark
  theme, font, page text size, map label size, start in kiosk mode. Saved in the browser.
- **URL options** for a single visit (not saved), handy for a dedicated display:
  `time-zones-local.html?kiosk=1&h12=1&home=us:P`
  Keys: `kiosk`, `h12`, `secs`, `theme` (auto/light/dark), `font` (orig/sans/serif/legible/mono),
  `size` and `ms` (70–170, percent), `home` (auto, none, or an id such as `ca:Alberta`, `us:P`, `mx:mxC`).

## Time rules

Most zones use the browser's built-in time-zone rules, so daylight time changes are automatic.
Canada's 2026 permanent-time zones (BC, Alberta, NWT, Manitoba, northwest Ontario and a few
sub-areas) are hard-coded offsets: they are set by provincial legislation that browsers' built-in
time-zone data may not include yet; edit the `CA` and `V`
tables in `tz-map.template.html` if they change. Mexico follows its 2022 law: no daylight time
except Baja California and the US-border municipalities. Sub-zone outlines are approximate.

## Rebuilding

Edit `tz-map.template.html`, then from this `source` folder run `python build.py`. It inlines the
files in `vendor/` and writes the finished page to `../time-zones-local.html`. Change `VERSION`
in `build.py` (and the version text in the template) for a new release.

## Bundled third-party files (`vendor/`)

Full licence texts are in `LICENSES.txt`.


- D3 7.9.0 and topojson-client 3.1.0, ISC licence (Mike Bostock)
- world-atlas 2.0.2 `countries-50m.json`, ISC licence
- Natural Earth v5.1.2 admin-1 and lakes, public domain — trimmed to Canada, the US and Mexico
  (Mexico from the 1:10m set, simplified), Great Lakes only, rewound for D3

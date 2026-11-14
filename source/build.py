#!/usr/bin/env python3
"""Build the standalone North American Time Zones page.

Reads tz-map.template.html and inlines D3, topojson-client and the three map data
files so the result runs from a double-click with no internet connection.

Usage (from this folder):  python build.py
Output: ../time-zones-local.html (the finished single-file page)
"""
import json, pathlib

VERSION = "1.6"
HERE = pathlib.Path(__file__).parent
VENDOR = HERE / "vendor"

def js_safe(text):
    # keep "</script>" sequences from ending the inline script early
    return text.replace("</", "<\\/")

def compact(name):
    return json.dumps(json.loads((VENDOR / name).read_text(encoding="utf-8")),
                      separators=(",", ":"), ensure_ascii=False)

page = (HERE / "tz-map.template.html").read_text(encoding="utf-8")
parts = {
    "<script>/*D3*/</script>": "<script>" + js_safe((VENDOR / "d3.min.js").read_text(encoding="utf-8")) + "</script>",
    "<script>/*TOPOJSON*/</script>": "<script>" + js_safe((VENDOR / "topojson-client.min.js").read_text(encoding="utf-8")) + "</script>",
    "/*WORLD*/null": js_safe(compact("countries-50m.json")),
    "/*ADMIN*/null": js_safe(compact("admin-can-usa-mex.geojson")),
    "/*LAKES*/null": js_safe(compact("great-lakes.geojson")),
}
for marker, content in parts.items():
    assert page.count(marker) == 1, marker
    page = page.replace(marker, content)

# In this repository the finished page replaces ../time-zones-local.html,
# so the existing GitHub Pages link always shows the latest build.
out = HERE.parent / "time-zones-local.html"
out.write_text(page, encoding="utf-8")
print(f"Wrote {out.name} v{VERSION} ({out.stat().st_size/1e6:.1f} MB)")

#!/usr/bin/env python3
"""Rebuild the Organelle patches index (the interactive tag explorer).

Run this whenever you add, remove, or re-tag a patch markdown file under
docs/Organelle/patches/. It scans every patch's YAML frontmatter (title + tags),
bakes the metadata into a self-contained tag-cloud page, and overwrites
docs/Organelle/patches/index.md.

To add a new patch:
    1. Create docs/Organelle/patches/<Category>/<slug>.md with frontmatter:
           ---
           title: My Patch
           tags:
             - Synthesizer
             - Delay
           ---
    2. Run:  dev/.venv/bin/python dev/build_patch_index.py

Unlike import_patches.py (a one-time snapshot of the old Webflow site), this
script reads only the local markdown files, so it keeps working after that
site goes offline.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
PATCHES_DIR = REPO_ROOT / "docs" / "Organelle" / "patches"
IMG_DIR = PATCHES_DIR / "images"

# Self-contained tag-explorer page. `__DATA__` is replaced with a JSON array
# of {t: title, u: url, c: category, g: [tags]}. Uses Material CSS variables so
# it follows the active theme/palette. Edit here to change the explorer UI.
EXPLORER_TEMPLATE = r"""# Organelle Patches

A library of <span id="pc-count"></span> patches for the Organelle. Browse them by category in the sidebar, or filter by tag and search by name below. Combine tags to narrow things down.

<div id="patch-explorer">
  <input id="pc-search" type="text" placeholder="Search patches by name..." autocomplete="off">
  <div id="pc-cloud" class="pc-cloud"></div>
  <div id="pc-active"></div>
  <div id="pc-results" class="pc-results"></div>
</div>

<style>
#patch-explorer { margin: 1.4rem 0 2rem; }
#pc-search {
  width: 100%; box-sizing: border-box; padding: 0.6rem 0.8rem;
  font-size: inherit; border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 0.4rem; background: var(--md-default-bg-color);
  color: var(--md-default-fg-color); margin-bottom: 1.2rem;
}
.pc-cloud {
  display: flex; flex-wrap: wrap; gap: 0.4rem 0.55rem;
  align-items: baseline; line-height: 1.4; margin-bottom: 1.2rem;
}
.pc-tag {
  cursor: pointer; border-radius: 1rem; padding: 0.15em 0.7em;
  font-size: 0.8rem;
  color: var(--md-default-fg-color); background: var(--md-default-fg-color--lightest);
  white-space: nowrap; transition: background 0.12s ease, color 0.12s ease, opacity 0.12s ease;
  user-select: none;
}
.pc-tag:hover { background: var(--md-default-fg-color--lighter); }
.pc-tag .pc-n { opacity: 0.5; font-size: 0.7em; margin-left: 0.25em; }
.pc-tag.pc-on { background: var(--md-primary-fg-color); color: var(--md-primary-bg-color); }
.pc-tag.pc-on .pc-n { opacity: 0.75; }
.pc-tag.pc-dim { opacity: 0.3; }
#pc-active { margin-bottom: 1rem; font-size: 0.8rem; min-height: 1.2em; }
#pc-active a { cursor: pointer; }
.pc-results { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 0.6rem; }
.pc-item {
  display: block; padding: 0.6rem 0.8rem; border-radius: 0.4rem;
  border: 1px solid var(--md-default-fg-color--lightest);
  text-decoration: none !important; color: var(--md-default-fg-color) !important;
  transition: border-color 0.12s ease, transform 0.12s ease;
}
.pc-item:hover { border-color: var(--md-default-fg-color--light); transform: translateY(-2px); }
.pc-item .pc-title { font-weight: 500; }
.pc-item .pc-cat { font-size: 0.72rem; opacity: 0.55; }
.pc-empty { opacity: 0.6; font-style: italic; }
</style>

<script>
(function () {
  var PATCHES = __DATA__;
  var active = new Set();
  var search = "";

  var counts = {};
  PATCHES.forEach(function (p) { p.g.forEach(function (t) { counts[t] = (counts[t] || 0) + 1; }); });
  var tags = Object.keys(counts).sort(function (a, b) { return counts[b] - counts[a] || a.localeCompare(b); });

  var cloud = document.getElementById("pc-cloud");
  tags.forEach(function (t) {
    var el = document.createElement("span");
    el.className = "pc-tag";
    el.dataset.tag = t;
    el.innerHTML = t.replace(/&/g, "&amp;").replace(/</g, "&lt;") + '<span class="pc-n">' + counts[t] + "</span>";
    el.addEventListener("click", function () {
      if (active.has(t)) active.delete(t); else active.add(t);
      render();
    });
    cloud.appendChild(el);
  });

  var searchBox = document.getElementById("pc-search");
  searchBox.addEventListener("input", function () { search = this.value.trim().toLowerCase(); render(); });

  function matches(p) {
    if (search && p.t.toLowerCase().indexOf(search) === -1) return false;
    for (var t of active) { if (p.g.indexOf(t) === -1) return false; }
    return true;
  }

  function render() {
    var shown = PATCHES.filter(matches);

    document.getElementById("pc-count").textContent = PATCHES.length;

    // remaining tags among the shown set, for dimming dead-ends
    var live = {};
    shown.forEach(function (p) { p.g.forEach(function (t) { live[t] = true; }); });
    Array.prototype.forEach.call(cloud.children, function (el) {
      var t = el.dataset.tag;
      el.classList.toggle("pc-on", active.has(t));
      el.classList.toggle("pc-dim", !active.has(t) && !live[t]);
    });

    var act = document.getElementById("pc-active");
    if (active.size) {
      act.innerHTML = "Filtering by <strong>" + Array.from(active).map(function (t) {
        return t.replace(/&/g, "&amp;").replace(/</g, "&lt;");
      }).join("</strong> + <strong>") + "</strong> &nbsp; <a id='pc-clear'>clear ×</a>";
      document.getElementById("pc-clear").addEventListener("click", function () { active.clear(); render(); });
    } else {
      act.innerHTML = "";
    }

    var res = document.getElementById("pc-results");
    if (!shown.length) {
      res.innerHTML = '<p class="pc-empty">No patches match that combination.</p>';
      return;
    }
    res.innerHTML = shown.map(function (p) {
      return '<a class="pc-item" href="' + p.u + '">' +
        '<span class="pc-title">' + p.t.replace(/&/g, "&amp;").replace(/</g, "&lt;") + "</span><br>" +
        '<span class="pc-cat">' + p.c + "</span></a>";
    }).join("");
  }

  render();
})();
</script>
"""


def parse_frontmatter(text: str) -> dict:
    """Return the YAML frontmatter of a markdown file as a dict ({} if none)."""
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def scan_patches() -> list[dict]:
    """Read every patch markdown file and return a list of
    {t: title, u: url, c: category, g: [tags]}, sorted by title."""
    patches: list[dict] = []
    for md_file in PATCHES_DIR.rglob("*.md"):
        if md_file.name == "index.md" or IMG_DIR in md_file.parents:
            continue
        rel = md_file.relative_to(PATCHES_DIR)
        fm = parse_frontmatter(md_file.read_text(encoding="utf-8"))
        title = str(fm.get("title") or md_file.stem)
        tags = [str(t) for t in (fm.get("tags") or []) if str(t).strip()]
        # Patches in a category subfolder use the folder name as their category
        # label. Top-level patches (e.g. PLAY) have no category folder, mirroring
        # how they're grouped on the instrument; they get a blank category.
        category = rel.parts[0] if len(rel.parts) >= 2 else ""
        url = "/".join(quote(p) for p in rel.with_suffix("").parts) + "/"
        patches.append({"t": title, "u": url, "c": category, "g": tags})
    patches.sort(key=lambda p: p["t"].lower())
    return patches


def build_index_page(patches: list[dict]) -> str:
    data = json.dumps(patches, ensure_ascii=False, separators=(",", ":"))
    return EXPLORER_TEMPLATE.replace("__DATA__", data)


def regenerate() -> int:
    """Scan patches, rewrite index.md, and return the patch count."""
    patches = scan_patches()
    (PATCHES_DIR / "index.md").write_text(build_index_page(patches), encoding="utf-8")
    return len(patches)


def main() -> int:
    if not PATCHES_DIR.exists():
        print(f"error: {PATCHES_DIR} not found", file=sys.stderr)
        return 2
    n = regenerate()
    print(f"wrote {PATCHES_DIR / 'index.md'} ({n} patches)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""One-time import of Organelle Patches from the old Webflow CMS into mkdocs.

This is a migration tool: it pulls the initial snapshot from the Webflow site
before that site goes offline. Day-to-day, patches are added by hand as markdown
files and the index is rebuilt with build_patch_index.py (no Webflow needed).

Usage:
    export WEBFLOW_API_TOKEN=...
    dev/.venv/bin/python dev/import_patches.py

Writes one markdown file per patch to docs/Organelle/patches/<slug>.md,
downloads cover images to docs/Organelle/patches/images/<slug>/, and rebuilds
docs/Organelle/patches/index.md via build_patch_index.regenerate().
"""
from __future__ import annotations

import os
import re
import sys
import time
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests
from markdownify import markdownify as md

SITE_ID = "5b52623a2da7dd5838ef67fd"
PATCHES_COLLECTION_ID = "5b7701f1d79b5270ea9c15bb"
TAGS_COLLECTION_ID = "5b7701f1d79b522a599c15a6"

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "docs" / "Organelle" / "patches"
IMG_DIR = OUT_DIR / "images"

# Source-of-truth for category grouping on the index page.
PATCHES_FOLDER = REPO_ROOT.parent / "Organelle_Patches"
CATEGORY_ORDER = ["Effects", "Hybrids", "Samplers", "Synthesizers", "Utilities", "Wepa!"]


def api_get(path: str, token: str, **params: Any) -> dict:
    r = requests.get(
        f"https://api.webflow.com/v2{path}",
        headers={"Authorization": f"Bearer {token}", "accept-version": "2.0.0"},
        params=params,
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def fetch_all_items(collection_id: str, token: str) -> list[dict]:
    items: list[dict] = []
    offset = 0
    while True:
        page = api_get(f"/collections/{collection_id}/items", token, limit=100, offset=offset)
        items.extend(page["items"])
        total = page["pagination"]["total"]
        offset += len(page["items"])
        if offset >= total or not page["items"]:
            return items


def download_image(url: str, dest: Path) -> None:
    if dest.exists():
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    dest.write_bytes(r.content)


def image_filename(url: str, fallback: str) -> str:
    name = Path(urlparse(url).path).name or fallback
    # Strip query strings if any made it through.
    return re.sub(r"[?#].*$", "", name) or fallback


def html_to_md(html: str | None) -> str:
    if not html:
        return ""
    # Webflow stores soft line breaks as U+2028 / U+2029; turn those into <br>
    # so numbered lists and "Knob1: ... Knob2: ..." rows don't collapse onto one line.
    html = html.replace(" ", "<br>").replace(" ", "<br>")
    # Zero-width joiners were used as visual spacers; strip them.
    html = html.replace("‍", "")
    # Authors typed literal markdown (**bold**, #### headings) into the rich text
    # editor, so don't let markdownify escape it back out.
    return md(
        html,
        heading_style="ATX",
        bullets="-",
        escape_asterisks=False,
        escape_underscores=False,
    ).strip()


def yaml_escape(s: str) -> str:
    if any(c in s for c in ":#-?&*!|>'\"%@`") or s.strip() != s:
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def extract_tags(field_data: dict, tag_names: dict[str, str]) -> list[str]:
    """Resolve a patch's tag IDs to names: main tag first, then secondary,
    deduplicated and order-preserving."""
    main_tag = tag_names.get(field_data.get("tag") or "", "")
    secondary = [tag_names[t] for t in (field_data.get("tags") or []) if t in tag_names]
    seen: set[str] = set()
    out: list[str] = []
    for t in ([main_tag] if main_tag else []) + secondary:
        if t and t not in seen:
            seen.add(t)
            out.append(t)
    return out


def build_page(patch: dict, tag_names: dict[str, str]) -> tuple[str, list[tuple[str, Path]]]:
    """Return (markdown_text, list_of_image_downloads)."""
    f = patch["fieldData"]
    slug = f["slug"]
    name = f["name"]
    downloads: list[tuple[str, Path]] = []

    all_tags = extract_tags(f, tag_names)

    # Cover image. Patches live one directory deep (in a category folder),
    # so image refs need to go up one level.
    cover_md = ""
    cover = f.get("patch-cover-image")
    if cover and cover.get("url"):
        fname = image_filename(cover["url"], "cover.jpg")
        rel = f"../images/{slug}/{fname}"
        downloads.append((cover["url"], IMG_DIR / slug / fname))
        cover_md = f"![{name}]({rel})\n\n"

    # Frontmatter.
    fm_lines = ["---", f"title: {yaml_escape(name)}"]
    if f.get("post-date"):
        fm_lines.append(f"date: {f['post-date'][:10]}")
    if all_tags:
        fm_lines.append("tags:")
        fm_lines.extend(f"  - {yaml_escape(t)}" for t in all_tags)
    fm_lines.append("---\n")
    frontmatter = "\n".join(fm_lines)

    # Header block: tags + download + media.
    meta_bits: list[str] = []
    if all_tags:
        meta_bits.append("**Tags:** " + ", ".join(all_tags))
    if f.get("download-url"):
        meta_bits.append(f"**[Download Patch]({f['download-url']})**")
    meta = "\n\n".join(meta_bits)

    overview = html_to_md(f.get("patch-overview"))
    description = html_to_md(f.get("description"))

    youtube_id = (f.get("youtube-video-id") or "").strip()
    yt_embed = ""
    if youtube_id:
        yt_embed = (
            f'<div class="video-embed"><iframe width="560" height="315" '
            f'src="https://www.youtube.com/embed/{youtube_id}" '
            f'title="YouTube video player" frameborder="0" '
            f'allow="accelerometer; autoplay; clipboard-write; encrypted-media; '
            f'gyroscope; picture-in-picture" allowfullscreen></iframe></div>'
        )

    soundcloud_id = (f.get("soundcloud-id") or "").strip()
    sc_embed = ""
    if soundcloud_id:
        sc_embed = (
            f'<iframe width="100%" height="166" scrolling="no" frameborder="no" '
            f'src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/'
            f'{soundcloud_id}&color=%23ff5500"></iframe>'
        )

    sections = [frontmatter, f"# {name}\n"]
    if yt_embed:
        sections.append(yt_embed)
    if sc_embed:
        sections.append(sc_embed)
    if cover_md.strip():
        sections.append(cover_md.rstrip())
    if meta:
        sections.append(meta)
    if overview:
        sections.append(overview)
    if description:
        sections.append("## Details\n\n" + description)

    body = "\n\n".join(s for s in sections if s).rstrip() + "\n"
    return body, downloads


def _norm(s: str) -> str:
    # Drop parenthesized aliases like " (AARRPP)", then keep alphanumerics only.
    s = re.sub(r"\(.*?\)", "", s)
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def build_category_map() -> dict[str, str]:
    """Map normalized patch name → category by scanning Organelle_Patches folders."""
    mapping: dict[str, str] = {}
    if not PATCHES_FOLDER.exists():
        print(f"warn: {PATCHES_FOLDER} not found, categories will be empty", file=sys.stderr)
        return mapping
    for category in CATEGORY_ORDER:
        cat_dir = PATCHES_FOLDER / category
        if not cat_dir.exists():
            continue
        # Wepa! is a patch itself (loose files), not a folder of subpatches.
        if not any(p.is_dir() for p in cat_dir.iterdir()):
            mapping[_norm(category)] = category
            continue
        for entry in cat_dir.iterdir():
            if entry.is_dir():
                mapping[_norm(entry.name)] = category
    return mapping


def categorize(patches: list[dict], category_map: dict[str, str]) -> dict[str, list[dict]]:
    by_cat: dict[str, list[dict]] = {c: [] for c in CATEGORY_ORDER + ["Other"]}
    for p in patches:
        f = p["fieldData"]
        key = _norm(f["name"])
        category = category_map.get(key) or category_map.get(_norm(f["slug"])) or "Other"
        by_cat[category].append(p)
    return by_cat


def cleanup_old_markdown() -> None:
    """Remove all .md files under OUT_DIR (except images/) so stale files
    from previous runs or recategorizations don't linger."""
    if not OUT_DIR.exists():
        return
    for md_file in OUT_DIR.rglob("*.md"):
        if IMG_DIR in md_file.parents:
            continue
        md_file.unlink()
    # Also remove now-empty category directories so renames don't leave shells.
    for sub in OUT_DIR.iterdir():
        if sub.is_dir() and sub != IMG_DIR and not any(sub.iterdir()):
            sub.rmdir()


def main() -> int:
    token = os.environ.get("WEBFLOW_API_TOKEN")
    if not token:
        print("error: set WEBFLOW_API_TOKEN", file=sys.stderr)
        return 2

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    IMG_DIR.mkdir(parents=True, exist_ok=True)

    print("fetching tags...")
    tag_items = fetch_all_items(TAGS_COLLECTION_ID, token)
    tag_names = {t["id"]: t["fieldData"]["name"] for t in tag_items}
    print(f"  {len(tag_names)} tags")

    print("fetching patches...")
    patches = fetch_all_items(PATCHES_COLLECTION_ID, token)
    print(f"  {len(patches)} patches")

    category_map = build_category_map()
    print(f"  {len(category_map)} folder→category mappings loaded")
    by_cat = categorize(patches, category_map)

    cleanup_old_markdown()

    written = 0
    image_jobs: list[tuple[str, Path]] = []
    for category, items in by_cat.items():
        if not items:
            continue
        cat_dir = OUT_DIR / category
        cat_dir.mkdir(parents=True, exist_ok=True)
        for p in items:
            body, dls = build_page(p, tag_names)
            slug = p["fieldData"]["slug"]
            (cat_dir / f"{slug}.md").write_text(body, encoding="utf-8")
            image_jobs.extend(dls)
            written += 1
        print(f"  {category}: {len(items)} patches")
    print(f"wrote {written} patch pages")

    print(f"downloading {len(image_jobs)} cover images...")
    for url, dest in image_jobs:
        try:
            download_image(url, dest)
        except Exception as e:
            print(f"  failed {url}: {e}", file=sys.stderr)
        time.sleep(0.05)

    # Rebuild the tag-explorer index from the markdown we just wrote. This is
    # the same generator used day-to-day after the old site goes offline.
    from build_patch_index import regenerate
    print(f"wrote index.md ({regenerate()} patches)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

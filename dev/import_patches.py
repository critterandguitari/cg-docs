#!/usr/bin/env python3
"""Import Organelle Patches from the Webflow CMS into mkdocs.

Usage:
    export WEBFLOW_API_TOKEN=...
    dev/.venv/bin/python dev/import_patches.py

Writes one markdown file per patch to docs/Organelle/patches/<slug>.md,
downloads cover images to docs/Organelle/patches/images/<slug>/,
and regenerates docs/Organelle/patches/index.md.
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


def build_page(patch: dict, tag_names: dict[str, str]) -> tuple[str, list[tuple[str, Path]]]:
    """Return (markdown_text, list_of_image_downloads)."""
    f = patch["fieldData"]
    slug = f["slug"]
    name = f["name"]
    downloads: list[tuple[str, Path]] = []

    main_tag = tag_names.get(f.get("tag") or "", "")
    secondary = [tag_names[t] for t in (f.get("tags") or []) if t in tag_names]
    # Deduplicate while preserving order; drop main tag from the secondary list.
    seen = set()
    all_tags: list[str] = []
    for t in ([main_tag] if main_tag else []) + secondary:
        if t and t not in seen:
            seen.add(t)
            all_tags.append(t)

    # Cover image.
    cover_md = ""
    cover = f.get("patch-cover-image")
    if cover and cover.get("url"):
        fname = image_filename(cover["url"], "cover.jpg")
        rel = f"images/{slug}/{fname}"
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


def build_index(patches: list[dict], tag_names: dict[str, str]) -> str:
    by_tag: dict[str, list[dict]] = {}
    for p in patches:
        tag = tag_names.get(p["fieldData"].get("tag") or "", "Uncategorized")
        by_tag.setdefault(tag, []).append(p)

    lines = ["# Organelle Patches\n",
             "Documentation for all Organelle patches.\n"]
    for tag in sorted(by_tag):
        lines.append(f"## {tag}\n")
        for p in sorted(by_tag[tag], key=lambda x: x["fieldData"]["name"].lower()):
            f = p["fieldData"]
            lines.append(f"- [{f['name']}]({f['slug']}.md)")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


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

    written = 0
    image_jobs: list[tuple[str, Path]] = []
    for p in patches:
        body, dls = build_page(p, tag_names)
        slug = p["fieldData"]["slug"]
        (OUT_DIR / f"{slug}.md").write_text(body, encoding="utf-8")
        image_jobs.extend(dls)
        written += 1
    print(f"wrote {written} patch pages")

    print(f"downloading {len(image_jobs)} cover images...")
    for url, dest in image_jobs:
        try:
            download_image(url, dest)
        except Exception as e:
            print(f"  failed {url}: {e}", file=sys.stderr)
        time.sleep(0.05)

    (OUT_DIR / "index.md").write_text(build_index(patches, tag_names), encoding="utf-8")
    print("wrote index.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())

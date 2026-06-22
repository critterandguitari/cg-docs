# cg-docs
Critter & Guitari Documentation

Built with [MkDocs](https://www.mkdocs.org/) + the Material theme. Pages live in
`docs/`. Local preview:

```
dev/.venv/bin/python -m mkdocs serve
```

## Organelle patches

Patch pages live under `docs/Organelle/patches/<Category>/<slug>.md`. The patches
landing page (`docs/Organelle/patches/index.md`) is a generated, interactive tag
explorer — do not edit it by hand.

### Add or change a patch

1. Create or edit `docs/Organelle/patches/<Category>/<slug>.md` with frontmatter:

   ```yaml
   ---
   title: My Patch
   tags:
     - Synthesizer
     - Delay
   ---
   ```

   - The **category** comes from the folder name; the **page URL** comes from the
     file path. To recategorize a patch, move the file to a different folder.
   - `tags` drives the tag cloud (sizes/counts recompute automatically).

2. Rebuild the index:

   ```
   dev/.venv/bin/python dev/build_patch_index.py
   ```

`dev/build_patch_index.py` reads only the local markdown, so it is the script to
use day-to-day. To change the explorer's look or behavior, edit
`EXPLORER_TEMPLATE` in that file and rerun it.

`dev/import_patches.py` is a **one-time** migration tool that pulled the initial
snapshot from the old Webflow site (which is going offline). It reuses
`build_patch_index.py` to rebuild the index, so the two stay in sync. You should
not normally need to run it.

# PDF Download for Documentation Site

## Goal
Offer downloadable/printer-friendly PDFs of the documentation hosted on GitHub Pages (static site). Key requirements:
- Table of contents with page numbers
- Proper image sizing (OLED screenshots are large and black, look bad in browser print)
- Works with existing static GitHub Pages hosting

## Recommended Approach: mkdocs-with-pdf

Uses WeasyPrint to generate PDFs at build time. PDFs are output as static files and deployed alongside the HTML — no server-side rendering needed.

### Changes Required

**mkdocs.yml** — add plugin:
```yaml
plugins:
  - with-pdf:
      output_path: pdf/manual.pdf
      cover_title: Critter & Guitari Documentation
```

**deploy-mkdocs-auto.yml** — install system deps and Python package:
```yaml
    - name: Install WeasyPrint dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz0b libffi-dev libjpeg-dev libopenjp2-7-dev

    - name: Install MkDocs and dependencies
      run: pip install mkdocs mkdocs-material mkdocs-with-pdf
```

### Considerations
- Currently generates one PDF for the whole site. Separate per-product PDFs (Organelle, etc.) are possible but need more config.
- Image sizing and OLED screenshot styling can be controlled via CSS.
- WeasyPrint has system dependencies (pango, cairo) but these are straightforward to install in the GitHub Actions Ubuntu runner.

## Other Options Explored
- **CSS print stylesheet** (`@media print`): Cheapest fix but no TOC with page numbers.
- **mkdocs-print-site-plugin**: Generates a single printable page; TOC page numbers still browser-dependent.
- **mkdocs-exporter**: Uses headless Chromium via Playwright. Good quality, heavier dependency.
- **Pandoc + LaTeX**: Most control, but separate build pipeline and painful setup.

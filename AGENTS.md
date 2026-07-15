# Repository Guidelines

## Project Structure & Module Organization

- `templates/` contains the TRMNL Liquid layouts: full, half-horizontal, half-vertical, and quadrant. Shared poster data and icons live in `shared.liquid` and `shared-icons.liquid`.
- `quotes.json` is the canonical quote database. `api/random-quote.json` is the generated endpoint consumed by TRMNL, while `.quote-history.json` tracks recent selections.
- `generate_random_quote.py` performs quote rotation; `test_quote_history.py` covers its history and fallback behavior.
- `assets/` stores demo images, icons, posters, and raw source artwork. Keep generated/optimized assets separate from `assets/raw/`.
- `settings.yml` defines plugin metadata and polling configuration. `index.html` is the GitHub Pages landing page.
- `.github/workflows/` validates quote data, refreshes the daily quote, and deploys the static site. Supporting documentation is under `docs/`.

## Build, Test, and Development Commands

This project has no compilation step or package manifest. Use Python 3 from the repository root:

```bash
python3 -m unittest test_quote_history.py
python3 generate_random_quote.py
python3 -m json.tool quotes.json >/dev/null
```

The first command runs the test suite. The second selects a quote and updates generated state, so review changes to `api/random-quote.json` and `.quote-history.json` before committing. The third provides a quick JSON syntax check; CI additionally verifies required `text`, `character`, and `game` fields. Preview template changes in the TRMNL markup editor at the target layout sizes.

## Coding Style & Naming Conventions

Use 4-space indentation and PEP 8 conventions for Python. Use 2 spaces for Liquid, JSON, and YAML, preserving the surrounding style. Name Python functions and variables with `snake_case`; name layout templates with lowercase underscores, such as `half_horizontal.liquid`. Keep quote objects limited to accurate `text`, `character`, and `game` values. Optimize display assets for high-contrast e-ink rendering and use descriptive lowercase filenames.

## Testing Guidelines

Tests use Python's built-in `unittest` framework. Add methods named `test_<behavior>` to `test_quote_history.py`, isolate filesystem writes with temporary directories, and mock randomness or file paths where needed. Run the full suite and JSON validation before opening a pull request. For visual changes, verify every affected layout and include preview screenshots.

## Commit & Pull Request Guidelines

Recent commits use concise, imperative subjects, often with prefixes such as `build:`, `add:`, or `Fix`. Automated quote refresh commits use `automated:` and should remain workflow-owned. Keep each commit focused. Pull requests should explain the change, identify testing performed, link relevant issues, and include screenshots for template or asset updates. Verify quote wording and game attribution from a reliable source.

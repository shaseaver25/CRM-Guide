# Stone Arch CRM — Small Business Guide

An interactive, screenshot-based guide to the cM CRM (crm.stonearch.ai), written for a
brand-new small-business user. Covers every major area of the system with real,
annotated screenshots and plain-English walkthroughs.

## View it

Open **`index.html`** in any browser — it's self-contained (no server needed), as long as
the `screenshots/` folder sits next to it.

To publish it as a website: enable **GitHub Pages** (Settings → Pages → Branch: `main` → `/root`).
Because the guide is `index.html`, it will serve at the Pages URL automatically.

## What's inside

| File | Purpose |
|------|---------|
| `index.html` / `stonearch-crm-guide.html` | The guide (same content; `index.html` is for GitHub Pages) |
| `screenshots/` | Real full-page screenshots of each CRM screen (referenced by the guide) |
| `capture-crm-screenshots.py` | Re-capture every screen automatically (log in once, it does the rest) |
| `RUN-SCREENSHOTS.md` | How to run the capture script |
| `crm-relabel-brief.md` | Change record: the nonprofit → small-business relabeling prompts |

## Updating the screenshots

The guide references screenshots by relative path, so re-running the capture script
refreshes the guide with zero code changes:

```bash
pip3 install playwright && python3 -m playwright install chromium
python3 capture-crm-screenshots.py
```

Log in when the browser opens, press Enter, and the `screenshots/` folder rebuilds itself.

## Sections covered

Dashboard · Members · Contacts · Sales Pipeline · Companies · Calendar · Projects ·
Tasks · Voice Notes · Events · Email Marketing · Content Repository · Admin & Member Clients ·
plus a Daily-Workflow cheat sheet and a Glossary.

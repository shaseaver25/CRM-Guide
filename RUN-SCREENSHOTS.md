# Capture the CRM screenshots automatically

This replaces the manual Cmd+Shift+4 process. Log in once; the script grabs all ~17 pages
full-size into the `screenshots/` folder. Re-run any time to regenerate everything.

## Option A — hand it to Claude Code (paste this prompt)

> In the folder `Curriculum/lesson builder` there's a script `capture-crm-screenshots.py`.
> Set up Playwright (`pip3 install playwright` then `python3 -m playwright install chromium`)
> and run the script. It will open a Chrome window — I'll log in manually, then press Enter
> in the terminal. Let it finish and confirm the PNGs landed in the `screenshots/` folder.
> Don't modify my login or handle my password; I'll type it myself in the browser window.

## Option B — run it yourself in Terminal

```bash
cd "~/Documents/Claude/Projects/Curriculum/lesson builder"
pip3 install playwright
python3 -m playwright install chromium
python3 capture-crm-screenshots.py
```

Then: log in when the Chrome window opens → press Enter in Terminal → wait → done.

## Notes
- **Your password is never seen by the script or by Claude.** You type it in the browser window.
- Files are named `01-dashboard.png`, `02-members.png`, etc. — matching the guide sections.
- The **360° Customer View** (`03-customer-360.png`) opens a pop-up by clicking the first
  customer card. If that one looks wrong, just re-shoot it by hand — everything else is solid.
- The board capture uses a direct URL (the "Operating Launch" board). If you'd rather capture a
  different board, change the URL on the `10-projects-board` line in the script.
- Run this **after** the relabeling has settled, so the screenshots show the small-business labels.

#!/usr/bin/env python3
"""
Capture full-page screenshots of the Stone Arch CRM (crm.stonearch.ai).

How it works:
  1. Opens a real Chrome window.
  2. Waits for YOU to log in (you type your own password — this script never sees it).
  3. After you press Enter, it visits each page and saves a full-page PNG to ./screenshots/.

Setup (one time):
    pip3 install playwright
    python3 -m playwright install chromium

Run:
    python3 capture-crm-screenshots.py

Re-run any time to regenerate everything (overwrites the folder).
"""

import os
import sys
from playwright.sync_api import sync_playwright

BASE = "https://crm.stonearch.ai"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")

# (filename, path, optional_note). The board uses a direct URL so no clicking is needed.
PAGES = [
    ("01-dashboard",        "/",                          None),
    ("02-members",          "/constituents",              None),
    ("04-contacts",         "/contacts",                  None),
    ("05-member-clients",   "/admin/customers",           None),
    ("06-sales-pipeline",   "/pipeline",                  None),
    ("07-companies",        "/sites",                     None),
    ("08-calendar",         "/calendar",                  None),
    ("09-projects",         "/projects",                  None),
    ("10-projects-board",   "/projects/a3dccc8c-2720-46e8-8af2-25a6173ef4b5", None),
    ("11-tasks",            "/tasks",                     None),
    ("12-voice-notes",      "/voice-notes",               None),
    ("13-events",           "/events",                    None),
    ("14-email-marketing",  "/email-marketing",           None),
    ("15-content",          "/content-repository",        None),
    ("16-admin",            "/admin",                     None),
    ("17-settings",         "/settings/account",          None),
]


def grab(page, path):
    page.goto(BASE + path, wait_until="domcontentloaded")
    try:
        page.wait_for_load_state("networkidle", timeout=8000)
    except Exception:
        pass
    page.wait_for_timeout(2500)  # let the SPA finish rendering cards/charts


def main():
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        ctx = browser.new_context(viewport={"width": 1440, "height": 900},
                                  device_scale_factor=2)  # crisp/retina
        page = ctx.new_page()

        page.goto(BASE, wait_until="domcontentloaded")
        print("\n" + "=" * 64)
        print("  A Chrome window opened. Log in to the CRM there.")
        print("  When you can see the Dashboard, come back here and press Enter.")
        print("=" * 64)
        input("  Press Enter once you're logged in... ")

        # Standard full-page captures
        for name, path, _ in PAGES:
            try:
                grab(page, path)
                out = os.path.join(OUT, name + ".png")
                page.screenshot(path=out, full_page=True)
                print(f"  saved {name}.png")
            except Exception as e:
                print(f"  SKIPPED {name} ({e})")

        # 360 Customer View modal (opens by clicking the first customer card).
        # Best-effort: if the click misses, capture this one manually.
        try:
            grab(page, "/constituents")
            page.mouse.click(430, 560)   # first card, top-left area
            page.wait_for_timeout(2000)
            page.screenshot(path=os.path.join(OUT, "03-customer-360.png"))  # viewport, modal is tall
            print("  saved 03-customer-360.png")
        except Exception as e:
            print(f"  SKIPPED 03-customer-360 ({e}) — capture this one by hand")

        print("\nDone. Files are in:", OUT)
        input("Press Enter to close the browser... ")
        browser.close()


if __name__ == "__main__":
    main()

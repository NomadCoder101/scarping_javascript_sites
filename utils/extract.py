import time
#https://store.steampowered.com/specials
from playwright.sync_api import sync_playwright
import logging



def extract_full_body_from(from_url,wait_for=None):

    # TIMEOUT=90000
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # browser = p.webkit.launch(headless=True)
        page = browser.new_page()
        page.goto(from_url)
        time.sleep(2 * 60)
        page.wait_for_load_state("networkidle")
        time.sleep(1 * 60)
        page.evaluate("() => window.scroll(0,document.body.scrollHeight)")
        time.sleep(1 * 60)
        # page.wait_for_event("domcontentloaded")
        if wait_for:
            page.wait_for_selector(wait_for)
        
        # page.screenshot(path='steam1.png',full_page=True)
        html = page.inner_html('body')

    return html


# wait_for ="div[class*='_2hhNOdcC6yLwL']"
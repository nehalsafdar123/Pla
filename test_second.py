import re
import pytest
from playwright.sync_api import sync_playwright, Playwright, Page, expect

def open_browser(p):
      browser = p.chromium.launch(headless=False, channel="chrome")
      page = browser.new_page()
      page.goto("https://test-staging.trp.ignishealth.com/accounts/login")
      return page




def testfirstly() -> None:
    with sync_playwright() as p:  
      page=open_browser(p)
    
      username = page.locator("#username").click()

      username = page.locator(
       "#username")
      username.fill("admin")
      password = page.locator(
     "#password")
      password.click()

      password = page.locator(
     "#password")
      password.fill("admin1PWD")

      page.get_by_role("button", name="Log in").first.click()

      entity_gallery = page.locator(
      "body > trp-root > trp-layout > trp-sidebar > nav > div.list-group > div:nth-child(5) > a:nth-child(1) > div > i")
      entity_gallery.click()

      zipnosis2 = page.locator(
      "body > trp-root > trp-layout > section > trp-manage-database > div > div > div:nth-child(2) > div > div:nth-child(3) > trp-stat > div > p-card > div > div > div")
      zipnosis2.click()

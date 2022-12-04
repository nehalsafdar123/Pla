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

      check_for_homepage_and_default3 = page.locator(
    "//h4[normalize-space()='check for homepage and default']")
      check_for_homepage_and_default3.click()

      dashboards = page.locator(
    "//a[normalize-space()='Dashboards']")
      dashboards.click()

      create_dashboard1 = page.locator(
    "//button[normalize-space()='Create Dashboard']")
      create_dashboard1.click()

      name = page.locator(
    "#name")
      name.click()

      name = page.locator(
       "#name")
      name.fill("test2")

# span9 = page.locator(
#                             "//dynamic-ng-bootstrap-form-control[1]/div/div/trp-dynamic-select-picker-form-control/trp-select-picker-form-control/ng-select/div/span")
# span9.click()

# finished_at2 = page.locator(
#                                    "//span[ = 'finished_at']")
# finished_at2.click()

# submitted_at1 = page.locator(
#                                     "//span[ = 'submitted_at']")
# submitted_at1.click()

# span9 = page.locator(
#                             "//dynamic-ng-bootstrap-form-control[1]/div/div/trp-dynamic-select-picker-form-control/trp-select-picker-form-control/ng-select/div/span")
# span9.click()

      span5 = page.locator(
       "#sub_dataset > div > div > div.ng-input")
      span5.click()
  
      check_for_homepage_and_default1 = page.locator(
       "//div/span[normalize-space()= 'check for homepage and default']")
      check_for_homepage_and_default1.click()
  
      save = page.locator(
       "//button[normalize-space()= 'Save']")
      save.click()
  
      div21 = page.locator(
       "//body/div[2]/div")
  
      expect(div21).to_have_text(re.compile("Dashboard is successfully created"))

# step_output = div21.text_content
# assert step_output and ("Dashboard is successfully created" in step_output)

      search_dashboard = page.locator(
       "//input[@placeholder = 'Search Dashboard']")
      search_dashboard.click()
  
      search_dashboard = page.locator(
       "//input[@placeholder = 'Search Dashboard']")
      search_dashboard.fill("test2")
  
      test21 = page.locator(
       "//span[normalize-space() = 'test2']")
      test21.click()
  
      page.wait_for_selector("#scrollableDiv > span > i")
  
      edit_icon_inside_dashboard = page.locator(
       "//form/div[1]/span/i")
      edit_icon_inside_dashboard.click()
  
      span15 = page.locator(
      "//div[1]/form/dynamic-ng-bootstrap-form/dynamic-ng-bootstrap-form-control/div/div/trp-dynamic-select-picker-form-control/trp-select-picker-form-control/ng-select/div/span")
      span15.click()
  
      finished_at3 = page.locator(
       "//div[1]/span[normalize-space()= 'finished_at']")
      finished_at3.click()
  
      span15 = page.locator(
       "//div[1]/form/dynamic-ng-bootstrap-form/dynamic-ng-bootstrap-form-control/div/div/trp-dynamic-select-picker-form-control/trp-select-picker-form-control/ng-select/div/span")
      span15.click()
  
      save5 = page.locator(
       "//button[normalize-space()= 'Save']")
      save5.click()
      div22 = page.locator(
       "//trp-entity-filter/div")
  
      go_to_gallery = page.locator(
       "#second-nav > div > div > trp-entity-dash-action > div > div.col-sm-9.text-right > button.btn.btn-outline-dark.btn-sm.mr-1.pull-right.mb-1.ng-star-inserted")
      go_to_gallery.click()
  
      dashboards = page.locator(
       "//a[normalize-space()= 'Dashboards']")
      dashboards.click()
  
      search_dashboard = page.locator(
       "//input[@placeholder = 'Search Dashboard']")
      search_dashboard.click()
  
      search_dashboard = page.locator(
       "//input[@placeholder = 'Search Dashboard']")
      search_dashboard.fill("test2")
  
      test22 = page.locator(
       "//span[normalize-space()= 'test2']")
      test22.click()
  
      page.wait_for_selector(
       "#finished_at > dynamic-ng-bootstrap-form-control.col-sm-12.ng-star-inserted > div > label")
      div21 = page.locator(
       "#finished_at > dynamic-ng-bootstrap-form-control.col-sm-12.ng-star-inserted > div > label")
      expect(div21).to_have_text(re.compile("finished_at"))
  
# finished_at4 = (
#      "//dynamic-ng-bootstrap-form-control[2]/div/label[ = 'finished_at']")
# page.addons().execute(
#     VisibleElementsOperations.containstextifvisibleweb(
#         text="finished_at",
#         timeout=""), *finished_at4)

      manage_dashboards = page.locator(
       "//button[normalize-space()= 'Manage Dashboards']")
      manage_dashboards.click()

      actions_button=page.locator("tr:nth-child(3) > td:nth-child(7) > span > button")
      actions_button.click()
  
      delete_inside_action_of_dashboard = page.get_by_role("menuitem", name=" Delete")
      delete_inside_action_of_dashboard.click()
  
      yes1 = page.locator(
       "//button[normalize-space()= 'Yes']")
      yes1.click()
  
      div21 = page.locator(
       "//body/div[2]/div")
  
      expect(div21).to_have_text(re.compile("Dashboard was deleted successfully."))
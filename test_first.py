import re
import time

from playwright.sync_api import sync_playwright, Playwright, Page, expect


# ''
# click on entity gallery and then go to zipnosis and then to homepage and default over there select the nehal safdar 1
# dashboard as default and then click vidyo section and then again click zipnosis home button nehal safdar dashboard will be open
# so checking its label overthere .
# Now make the nehal safdar 2 as default dashboard and again click on vidyo and
# come back to zipnosis home nehal safdar 2 dashboard will be open
# '''


def open_browser(p):
    browser = p.chromium.launch(headless=True, channel="chrome")
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://test-staging.trp.ignishealth.com/accounts/login")
    return {'page': page, 'context': context}


def test_make_default() -> None:
    with sync_playwright() as p:
        Content = open_browser(p)

        page = Content['page']
        context = Content['context']

        username = page.locator(
            "#username")
        username.click()

        username = page.locator(
            "#username")
        username.fill("admin")

        password = page.locator(
            "#password")
        password.click()

        password = page.locator(
            "#password")
        password.fill("admin1PWD")

        log_in = page.locator(
            "//button[. = 'Log in ']")
        log_in.click()

        # entity_gallery = page.locator(
        #     "//div/a[. = 'Entities Home']")
        # entity_gallery.click()

        zipnosis = page.locator(
            "//html/body/trp-root/trp-layout/trp-sidebar/nav/div[1]/div[4]/a/div/i")
        zipnosis.click()

        page.get_by_role("heading", name="check for homepage and default").click()

        dashboards = page.locator(
            "//a[. = 'Dashboards']")
        dashboards.click()

        page.get_by_placeholder("Search Dashboard").fill("nehal 1")

        time.sleep(4)

        page.locator("//html/body/trp-root/trp-layout/section/trp-dataset-details/div/div/div[2]/p-tabview/div/div[2]/p-tabpanel[1]/div/p-table/div/div[2]/table/tbody/tr/td[7]/button[1]").first.click()

        time.sleep(4)

        encounter_home3 = page.locator(
            "//a[. = 'Encounter Home']")
        encounter_home3.click()

        zipnosis = page.locator(
            "//html/body/trp-root/trp-layout/trp-sidebar/nav/div[1]/div[4]/a/div/i")
        zipnosis.click()

        zipnosis = page.locator(
            "//html/body/trp-root/trp-layout/trp-sidebar/nav/div[1]/div[4]/a/div/i")
        zipnosis.click()

        nehal_safdar_1 = page.locator(
            "//p-inplace/div")

        expect(nehal_safdar_1).to_have_text(re.compile("nehal 1"))

        page.get_by_role("button", name="Manage Dashboards").click()

        page.get_by_placeholder("Search Dashboard").fill("nehal 2")

        time.sleep(4)

        page.locator(
            "//html/body/trp-root/trp-layout/section/trp-dataset-details/div/div/div[2]/p-tabview/div/div[2]/p-tabpanel[1]/div/p-table/div/div[2]/table/tbody/tr/td[7]/button[1]").first.click()

        time.sleep(4)

        zipnosis = page.locator(
            "//html/body/trp-root/trp-layout/trp-sidebar/nav/div[1]/div[4]/a/div/i")
        zipnosis.click()

        zipnosis = page.locator(
            "//html/body/trp-root/trp-layout/trp-sidebar/nav/div[1]/div[4]/a/div/i")
        zipnosis.click()

        nehal_safdar_2 = page.locator(
            "//p-inplace/div")
        expect(nehal_safdar_2).to_have_text(re.compile("nehal 2"))

        page.get_by_role("button", name="Manage Dashboards").click()

        page.get_by_placeholder("Search Dashboard").fill("nehal 2")

        time.sleep(4)

        page.locator(
            "//html/body/trp-root/trp-layout/section/trp-dataset-details/div/div/div[2]/p-tabview/div/div[2]/p-tabpanel[1]/div/p-table/div/div[2]/table/tbody/tr/td[7]/button[1]").first.click()



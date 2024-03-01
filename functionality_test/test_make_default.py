import pytest
from playwright.sync_api import Page, expect


@pytest.mark.browser_context_args(storage_state="superuser_login_state.json")
def test_make_default(page: Page) -> None:
    """
    click on entity gallery and then go to zipnosis and then to homepage and default over there select the nehal safdar 1
    dashboard as default and then click vidyo section and then again click zipnosis home button nehal safdar dashboard will be open
    so checking its label overthere.Now make the nehal safdar 2 as default dashboard and again click on vidyo and
    come back to zipnosis home nehal safdar 2 dashboard will be open
    """

    page.goto("/")
    expect(page.get_by_role("link", name="Support Account")).to_be_visible()
    go_to_entities_home(page)
    page.get_by_role("heading", name="Zipnosis").click()
    page.get_by_role("heading", name="check for homepage and default").click()
    page.get_by_placeholder("Search Dashboard").fill("nehal safdar 1")

    # click default button
    page.locator('[data-ui-tests="mark-default-button"]').click()
    page.wait_for_timeout(2000)

    # Go to zipnosis from sidebar
    page.locator('[data-ui-tests="zipnosis-left-sidebar"]').click()
    expect(page.get_by_role("button", name="Manage Dashboards")).to_be_visible()
    expect(page.locator("p-inplace").get_by_text("nehal safdar 1")).to_be_visible()
    page.get_by_role("button", name="Manage Dashboards").click()
    page.get_by_placeholder("Search Dashboard").fill("nehal safdar 2")

    # Clicking on Default button
    page.locator('[data-ui-tests="mark-default-button"]').click()
    page.wait_for_timeout(2000)
    page.locator('[data-ui-tests="zipnosis-left-sidebar"]').click()
    expect(page.get_by_role("button", name="Manage Dashboards")).to_be_visible()
    expect(page.locator("p-inplace").get_by_text("nehal safdar 2")).to_be_visible()

    # To Reset default
    page.get_by_role("button", name="Manage Dashboards").click()
    page.get_by_placeholder("Search Dashboard").fill("nehal safdar 2")
    page.locator('[data-ui-tests="mark-default-button"]').click()


def go_to_entities_home(page):
    sidebar_element = page.locator(".sidebar.collapsed")
    entity_gallery = sidebar_element.locator('a[href="/manage-database"]')
    entity_gallery.click()

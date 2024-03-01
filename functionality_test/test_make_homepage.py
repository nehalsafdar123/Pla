import pytest
from playwright.sync_api import Page, expect


@pytest.mark.browser_context_args(storage_state="superuser_login_state.json")
def test_make_homepage(page: Page) -> None:
    """
    Make homepage nehal safdar 1 by going to zipnosis and then to Homepage and default section
    logout and then login nehal safdar 1 dashboard will be open.
    Make homepage nehal safdar 2 by going to zipnosis and then to Homepage and default section
    logout and then login nehal safdar 2 dashboard will be open.
    """

    page.goto("/")
    expect(page.get_by_role("link", name="Support Account")).to_be_visible()
    go_to_entities_home(page)
    page.get_by_role("heading", name="zipnosis").click()
    page.get_by_role("heading", name="check for homepage and default").click()
    page.get_by_placeholder("Search Dashboard").fill("nehal safdar 1")

    # Clicking on HomePage button
    page.locator('[data-ui-tests="mark-homepage-button"]').click()
    page.wait_for_timeout(1000)

    page.goto("/")
    expect(page.get_by_role("button", name="Manage Dashboards")).to_be_visible()
    expect(page.locator("p-inplace").get_by_text("nehal safdar 1")).to_be_visible()
    page.get_by_role("button", name="Manage Dashboards").click()
    page.get_by_placeholder("Search Dashboard").fill("nehal safdar 2")

    # Clicking on HomePage
    page.locator('[data-ui-tests="mark-homepage-button"]').click()
    page.wait_for_timeout(1000)

    # check if we're redirected to Homepage
    page.goto("/")
    expect(page.get_by_role("button", name="Manage Dashboards")).to_be_visible()
    expect(page.locator("p-inplace").get_by_text("nehal safdar 2")).to_be_visible()
    page.get_by_role("button", name="Manage Dashboards").click()
    page.get_by_placeholder("Search Dashboard").fill("nehal safdar 2")
    page.locator('[data-ui-tests="mark-homepage-button"]').click()


def go_to_entities_home(page):
    sidebar_element = page.locator(".sidebar.collapsed")
    entity_gallery = sidebar_element.locator('a[href="/manage-database"]')
    entity_gallery.click()

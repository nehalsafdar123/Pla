import pytest
from playwright.sync_api import Page, expect


@pytest.mark.browser_context_args(storage_state="superuser_login_state.json")
def test_passing_and_not_passing_values_check(page: Page) -> None:
    """
    Applying state filter in check on staging data . results we get is deducted from the original passing value and then this result is compared with final failed
    value
    """

    page.goto("/")
    expect(page.get_by_role("link", name="Support Account")).to_be_visible()
    go_to_entities_home(page)
    page.get_by_role("heading", name="Zipnosis").click()
    page.get_by_text("check on staging").click()
    page.get_by_role("tab", name="Data Access Control").click()
    page.get_by_placeholder("Search Data Access").fill("check on")
    page.get_by_role("button", name="check on staging").click()
    page.get_by_role("heading", name="Passing (54)").click()
    page.get_by_role("button", name="Advanced Filters").click()
    page.get_by_placeholder("Search for filter").fill("state")
    page.get_by_label("Data").get_by_text("state").click()

    # clicking state dropdown to apply filter
    page.locator("#cl_state_a1ab826edde458068625_select > div > span").click()
    page.wait_for_timeout(2000)
    page.get_by_placeholder("Search...").fill("1011")
    page.get_by_role("option", name="1011").click()
    page.get_by_role("button", name="Insert Filter").click()
    page.get_by_role("button", name="Search", exact=True).click()
    page.get_by_role("heading", name="Passing (1)").click()
    page.get_by_role("heading", name="Not Passing (53)").click()


def go_to_entities_home(page):
    sidebar_element = page.locator(".sidebar.collapsed")
    entity_gallery = sidebar_element.locator('a[href="/manage-database"]')
    entity_gallery.click()

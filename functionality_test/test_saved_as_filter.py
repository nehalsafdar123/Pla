import pytest
from playwright.sync_api import Page, expect


@pytest.mark.browser_context_args(storage_state="superuser_login_state.json")
def test_saved_as_filter(page: Page) -> None:
    """
    filter is applied and then save it . then going load a save filter to se if it is available.
    Apply it from there and then deleting it.Filter is deleted successfully now and no more filter can be seen.
    """

    page.goto("/")
    expect(page.get_by_role("link", name="Support Account")).to_be_visible()
    go_to_entities_home(page)
    page.get_by_role("heading", name="Zipnosis").click()
    page.get_by_role("heading", name="wreewr").click()
    page.get_by_role("tab", name="Data Access Control").click()
    page.get_by_placeholder("Search Data Access").fill("wreewr")
    page.get_by_role("button", name="wreewr").click()
    page.get_by_role("button", name="Advanced Filters").click()
    page.get_by_placeholder("Search for filter").fill("state")
    page.get_by_label("Data").get_by_text("state").click()
    page.locator("#cl_state_a1ab826edde458068625_select > div > span").click()
    page.get_by_role("option", name="1001").click()
    page.get_by_role("button", name="Insert Filter").click()
    page.get_by_role("button", name="Save As Filter").click()
    page.get_by_role("textbox").fill("nehal1")
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="Selected Filter : (nehal1)").click()
    page.get_by_role("button", name="Delete Filter").click()
    page.get_by_role("button", name="Yes").click()

    #  Is 'No filter can be seen on load a save filter' present?
    page.get_by_role("button", name="Load a Saved Filter").click()
    page.get_by_label("Filters").locator("span").first.click()
    page.get_by_text("No items found").click()


def go_to_entities_home(page):
    sidebar_element = page.locator(".sidebar.collapsed")
    entity_gallery = sidebar_element.locator('a[href="/manage-database"]')
    entity_gallery.click()

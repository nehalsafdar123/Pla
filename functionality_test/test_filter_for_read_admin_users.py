import pytest
from playwright.sync_api import Page, expect


@pytest.mark.browser_context_args(storage_state="superuser_login_state.json")
def test_filter_for_read_admin_user(page: Page) -> None:
    """
    Logged in with "admintestuser" going to zipnosis and then go to data of check on staging dataset and applying filter of finished at in advanced filter section.
    Afterwards saving that filter in name of "11" and seeing whether we are seeing that saved filter in selected filter selecting it and then deleting it.
    Now opening read test user going to check on staging and then go to data and then applying filter.read only user shall not be able to save the filter therefore
    we will see that if that save filter button is visible here or not.
    """

    page.goto("/")
    expect(page.get_by_role("link", name="Support Account")).to_be_visible()

    go_to_entities_home(page)
    page.get_by_role("heading", name="Zipnosis").click()
    page.get_by_text("check on staging").click()
    page.get_by_role("tab", name="Data Access Control").click()
    page.get_by_placeholder("Search Data Access").fill("check on staging")
    page.locator('[data-ui-tests = "share-subdataset"]').click()
    page.wait_for_timeout(1000)
    page.get_by_label("Share With").locator("span").first.click()
    page.get_by_role("option", name="Read Test User").click()
    page.get_by_role("option", name="Admin Test User").click()
    page.locator(".ng-arrow-wrapper").first.click()
    page.get_by_role("button", name="Save").click()

    page.goto("/accounts/login")
    page.get_by_label("User Name").fill("admintestuser")
    page.locator('input[type="password"]').fill("admin1PWD")
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_role("link", name="Admin Test User")).to_be_visible()
    go_to_entities_home(page)
    page.wait_for_timeout(1000)
    page.get_by_role("heading", name="Zipnosis").click()
    page.get_by_text("check on staging").click()
    page.get_by_role("tab", name="Data Access Control").click()
    page.get_by_placeholder("Search Data Access").fill("check on staging")
    page.get_by_role("button", name="check on staging").click()
    page.get_by_role("button", name="Advanced Filters").click()
    page.get_by_label("Data").get_by_text("finished_at").click()
    page.get_by_placeholder("Set Date Range").click()
    page.get_by_role("button", name="Apply").click()
    page.get_by_role("button", name="Insert Filter").click()
    page.get_by_role("button", name="Save As Filter").click()
    page.get_by_role("textbox").fill("11")
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="Selected Filter : (11)").click()
    page.get_by_role("button", name="Delete Filter").click()
    page.get_by_role("button", name="Yes").click()

    page.goto("/accounts/login")
    page.get_by_label("User Name").fill("readtestuser")
    page.locator('input[type="password"]').fill("admin1PWD")
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_role("link", name="Read Test User")).to_be_visible()
    go_to_entities_home(page)
    page.wait_for_timeout(1000)
    page.get_by_role("heading", name="Zipnosis").click()
    page.get_by_text("check on staging").click()
    page.get_by_role("tab", name="Data Access Control").click()
    page.get_by_placeholder("Search Data Access").fill("check on staging")
    page.get_by_role("button", name="check on staging").click()
    page.get_by_role("button", name="Advanced Filters").click()
    expect(page.get_by_role("button", name="Save As Filter")).not_to_be_visible()


def go_to_entities_home(page):
    sidebar_element = page.locator(".sidebar.collapsed")
    entity_gallery = sidebar_element.locator('a[href="/manage-database"]')
    entity_gallery.click()

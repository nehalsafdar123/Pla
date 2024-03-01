import pytest
from playwright.sync_api import Page, expect


@pytest.mark.browser_context_args(storage_state="superuser_login_state.json")
def test_saved_filters(page: Page) -> None:  # noqa: MFL000
    """
    creating and saving filter by using admin account but first creating subdataset of "saved filter test" now login
    with admin test user and go to same entity and apply that filter Now delete the filter that was applied and then go
    to admin to see if the same filter that was saved is deleted or not
    """

    page.goto("/")
    expect(page.get_by_role("link", name="Support Account")).to_be_visible()
    go_to_entities_home(page)

    page.get_by_role("heading", name="Zipnosis").click()
    page.get_by_role("heading", name="Tenants permission Test").click()
    page.get_by_role("tab", name="Data Access Control").click()
    page.get_by_role("button", name="Create Data Access").click()
    page.get_by_label("Title").fill("saved filter test")
    page.wait_for_timeout(3000)
    page.locator("#cl_businessli_sslinename_941fb7024a1c8dd864f0").get_by_role(
        "combobox"
    ).click()
    page.get_by_role("option", name="Virtual Urgent Care").click()
    page.get_by_role("region", name="Share With").locator("span").first.click()
    page.get_by_text("Admin Test User").click()
    page.get_by_role("region", name="Share With").locator("span").first.click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Save").click()
    page.get_by_role("tab", name="Dashboards").click()
    page.get_by_role("tab", name="Data Access Control").click()
    page.get_by_placeholder("Search Data Access").fill("saved filter")
    page.get_by_role("button", name="saved filter test").click()
    page.get_by_role("button", name="Advanced Filters").click()
    page.get_by_label("Data").get_by_text("state").click()
    page.locator("#cl_state_a1ab826edde458068625_select span").first.click()
    page.wait_for_timeout(1000)
    page.get_by_role("option", name="1001").click()
    page.get_by_role("button", name="Insert Filter").click()
    page.get_by_role("button", name="Save As Filter").click()
    page.get_by_role("textbox").fill("filter saved")
    page.get_by_role("button", name="Save").click()

    page.goto("/accounts/login")
    page.get_by_label("User Name").fill("admintestuser")
    page.locator('input[type="password"]').fill("admin1PWD")
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_role("link", name="Admin Test User")).to_be_visible()
    go_to_entities_home(page)
    page.wait_for_timeout(1000)
    page.get_by_role("heading", name="Zipnosis").click()
    page.get_by_role("heading", name="Tenants permission Test").click()
    page.get_by_role("tab", name="Data Access Control").click()
    page.get_by_placeholder("Search Data Access").fill("saved filter")
    page.get_by_role("button", name="saved filter test").click()
    page.get_by_role("button", name="Load a Saved Filter").click()
    page.get_by_role("tabpanel", name="Filters").locator("span").first.click()
    page.get_by_text("filter saved").click()
    page.get_by_role("button", name="Delete Filter").click()
    page.get_by_role("button", name="Yes").click()
    page.get_by_text("Filter was successfully deleted").click()

    page.goto("/accounts/login")
    page.get_by_label("User Name").fill("admin")
    page.locator('input[type="password"]').fill("admin1PWD")
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_role("link", name="Support Account")).to_be_visible()

    go_to_entities_home(page)
    page.get_by_role("heading", name="Zipnosis").click()
    page.get_by_role("heading", name="Tenants permission Test").click()
    page.get_by_role("tab", name="Data Access Control").click()
    page.get_by_placeholder("Search Data Access").fill("saved filter")
    page.get_by_role("row", name="saved filter test").get_by_role("button").nth(
        5
    ).click()
    page.get_by_role("menuitem", name="Delete").click()
    page.get_by_role("button", name="Yes").click()


def go_to_entities_home(page):
    sidebar_element = page.locator(".sidebar.collapsed")
    entity_gallery = sidebar_element.locator('a[href="/manage-database"]')
    entity_gallery.click()

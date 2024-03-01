import pytest
from playwright.sync_api import Page, expect


@pytest.mark.browser_context_args(storage_state="superuser_login_state.json")
def test_clone_a_dashboard(page: Page) -> None:
    """
    clone an already existing dashboard in zipnosis and then see by searching its name whether it was created or not.
    ALso see whether the widget was also cloned inside it or not. afterwards delete that cloned dashboard
    """

    page.goto("/")
    expect(page.get_by_role("link", name="Support Account")).to_be_visible()

    go_to_entities_home(page)
    page.get_by_role("heading", name="Encounter").click()
    page.get_by_role("heading", name="CH Drilldown2").click()
    page.get_by_placeholder("Search Dashboard").fill("drill down dashboard")

    # clicked on action button
    page.locator(".ng-star-inserted > button").first.click()
    page.get_by_role("menuitem", name="Clone").click()
    page.get_by_text("Dashboard was successfully cloned").click()

    go_to_entities_home(page)
    page.get_by_role("heading", name="Encounter").click()
    page.get_by_role("heading", name="CH Drilldown2").click()
    page.get_by_placeholder("Search Dashboard").fill("drill down dashboard - copy")
    page.get_by_role("button", name="drill down dashboard - copy").click()
    widget = page.locator('[data-ui-tests="widget"]')
    expect(widget).to_be_visible()

    page.get_by_role("button", name="Manage Dashboards").click()
    page.get_by_placeholder("Search Dashboard").fill("drill down dashboard - copy")

    # action button and then delete dashboard
    page.locator('[data-ui-tests="dashboard-actions-button"]').click()
    page.get_by_role("menuitem", name="Delete").click()
    page.get_by_role("button", name="Yes").click()
    page.get_by_text("Dashboard was deleted successfully.").click()


def go_to_entities_home(page):
    sidebar_element = page.locator(".sidebar.collapsed")
    entity_gallery = sidebar_element.locator('a[href="/manage-database"]')
    entity_gallery.click()

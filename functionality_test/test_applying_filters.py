import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.browser_context_args(storage_state="superuser_login_state.json")
def test_applying_filters(page: Page) -> None:
    """
    Applying filters for viyo section in join time of vidyo CDRS data now applying it . we will get passing and not passing values.fetching passing value from here
    and save it in variable and then search for results button is clicked . we will see what results we fetch in applying filter is same as after searching or not
    """
    page.goto("/")
    expect(page.get_by_role("link", name="Support Account")).to_be_visible()
    go_to_entities_home(page)
    page.get_by_role("heading", name="Encounter").click()
    page.get_by_role("heading", name="CH Drilldown2").click()
    page.get_by_role("tab", name="Data Access Control").click()
    page.get_by_placeholder("Search Data Access").fill("CH Drilldown2")
    page.get_by_role("button", name="CH Drilldown2").click()
    page.get_by_role("button", name="Advanced Filters").click()
    page.get_by_placeholder("Search for filter").fill("Created At")
    page.get_by_label("Data").get_by_text("Created At").click()
    page.get_by_placeholder("Set Date Range").click()

    # click cuton button and then click on custom inside it
    page.get_by_role("button", name="Custom").click()
    page.get_by_role("button", name="Custom").nth(1).click()
    page.get_by_placeholder("yyyy-mm-dd").first.fill("2021-06-06")
    page.get_by_placeholder("yyyy-mm-dd").nth(1).fill("2022-03-10")
    page.get_by_role("button", name="Apply").click()
    page.get_by_role("button", name="Insert Filter").click()

    expect(
        page.get_by_role("cell", name="Created At (Date Range 2021-")
    ).to_contain_text(re.compile("2021-06-06T00:00:00,2022-03-10T23:59:59"))
    page.get_by_role("cell", name="170", exact=True).click()
    page.get_by_role("button", name="Search").first.click()
    page.get_by_role("heading", name="Passing (170)").click()

    page.get_by_role("button", name="Clear Search").click()
    page.wait_for_timeout(2000)

    page.get_by_label("Data").get_by_text("Created At").click()
    page.get_by_placeholder("Set Date Range").click()
    page.get_by_placeholder("yyyy-mm-dd").first.fill("2021-06-02")
    page.get_by_placeholder("yyyy-mm-dd").nth(1).fill("2022-03-02")
    page.get_by_role("button", name="Apply").click()
    page.get_by_role("button", name="Insert Filter").click()
    page.get_by_role("button", name="Search").first.click()
    page.get_by_role("heading", name="Passing (0)").click()


def go_to_entities_home(page):
    sidebar_element = page.locator(".sidebar.collapsed")
    entity_gallery = sidebar_element.locator('a[href="/manage-database"]')
    entity_gallery.click()

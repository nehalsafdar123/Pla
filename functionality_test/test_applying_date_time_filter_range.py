import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.browser_context_args(storage_state="superuser_login_state.json")
def test_applying_date_time_filter_range(page: Page) -> None:
    """
    to test datetime filter range we do select the vidyo entity and then in vidyo entity i select the month first and then  year to make it eleigible in every year afterwards
    just select a month in next year and apply it . compare the result with desired output . it should be same
    """

    page.goto("/")
    expect(page.get_by_role("link", name="Support Account")).to_be_visible()
    go_to_entities_home(page)
    page.get_by_role("heading", name="Encounter").click()
    page.get_by_role("heading", name="CH Drilldown2").click()
    page.get_by_role("tab", name="Data Access Control").click()
    page.get_by_placeholder("Search Data Access").fill("CH Drilldown")
    page.get_by_role("button", name="CH Drilldown2").click()
    page.get_by_role("button", name="Advanced Filters").click()

    page.get_by_placeholder("Search for filter").fill("Created At")
    page.get_by_label("Data").get_by_text("Created At").click()
    page.get_by_placeholder("Set Date Range").click()
    page.get_by_label("Select month").select_option("7")
    page.get_by_label("Select year").select_option("2021")

    # Now go to october from july month
    for _month_increment in range(3):
        page.get_by_label("Next month").click()

    page.get_by_role("gridcell", name="Friday, October 1, 2021").get_by_text(
        "1"
    ).click()
    page.get_by_role("gridcell", name="Friday, October 15, 2021").get_by_text(
        "15"
    ).click()
    page.get_by_role("button", name="Apply").click()
    page.get_by_role("button", name="Insert Filter").click()

    # check if we are getting correct filter values
    expect(
        page.get_by_role("cell", name="Created At (Date Range 2021-10")
    ).to_have_text(re.compile("2021-10-01T00:00:00,2021-10-15T23:59:59"))
    page.get_by_role("button", name="Search").first.click()
    page.get_by_role("heading", name="Passing (9)").click()

    # clear filter and then re-apply filter on different date
    page.get_by_role("button", name="Clear Search").click()
    page.wait_for_timeout(1000)

    page.get_by_label("Data").get_by_text("Created At").click()
    page.get_by_placeholder("Set Date Range").click()
    page.get_by_label("Select month").select_option("10")
    page.get_by_label("Select year").select_option("2021")
    page.get_by_label("Saturday, October 16,").get_by_text("16").click()
    page.get_by_label("Saturday, October 30,").get_by_text("30").click()
    page.get_by_role("button", name="Apply").click()
    page.get_by_role("button", name="Insert Filter").click()
    page.get_by_role("button", name="Search", exact=True).click()
    page.get_by_role("heading", name="Passing (10)").click()


def go_to_entities_home(page):
    sidebar_element = page.locator(".sidebar.collapsed")
    entity_gallery = sidebar_element.locator('a[href="/manage-database"]')
    entity_gallery.click()

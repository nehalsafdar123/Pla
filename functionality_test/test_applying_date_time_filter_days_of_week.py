import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.browser_context_args(storage_state="superuser_login_state.json")
def test_applying_date_time_filter_days_of_week(page: Page) -> None:
    """
    Applying week days filter by going to vidyo section . At first we select join time and then select week days after matching the output with our required result we
    edit the filter and now select only monday thursday and friday and compare the output
    """

    page.goto("/")
    expect(page.get_by_role("link", name="Support Account")).to_be_visible()
    go_to_entities_home(page)
    page.get_by_role("heading", name="Vidyo CDR").click()
    page.get_by_role("heading", name="check for vidyo").click()
    page.get_by_role("tab", name="Data Access Control").click()
    page.get_by_placeholder("Search Data Access").fill("check for vidyo")
    page.get_by_role("button", name="check for vidyo").click()
    page.get_by_role("button", name="Advanced Filters").click()
    page.get_by_placeholder("Search for filter").fill("join")
    page.get_by_label("Data").get_by_text("Join Time").click()
    page.get_by_title("Time Frame").locator("span").nth(2).click()
    page.get_by_placeholder("Search...").fill("days of the week")
    page.get_by_text("Days of The Week").click()

    # clicking on weekdays checkbox
    page.get_by_text("Weekdays").click()
    page.get_by_role("button", name="Insert Filter").click()

    # check for weekdays selection
    join_time_days_of_the_week = page.get_by_role(
        "cell", name="Join Time (Days of the Week"
    )
    expect(join_time_days_of_the_week).to_contain_text(
        re.compile("Monday,Tuesday,Wednesday,Thursday,Friday")
    )
    page.wait_for_timeout(1000)

    # click on edit filter button
    page.locator('[data-ui-tests = "advanced-filters-edit-button"]').click()

    page.locator("div").filter(has_text=re.compile(r"^Tuesday$")).locator(
        "span"
    ).click()
    page.locator("div").filter(has_text=re.compile(r"^Wednesday$")).locator(
        "span"
    ).click()
    page.get_by_role("button", name="Update Filter").click()
    join_time_days_of_the_week = page.get_by_role(
        "cell", name="Join Time (Days of the Week"
    )
    expect(join_time_days_of_the_week).to_contain_text(
        re.compile("Monday,Thursday,Friday")
    )
    page.get_by_role("button", name="Search", exact=True).click()
    page.get_by_role("cell", name="0", exact=True).click()


def go_to_entities_home(page):
    sidebar_element = page.locator(".sidebar.collapsed")
    entity_gallery = sidebar_element.locator('a[href="/manage-database"]')
    entity_gallery.click()

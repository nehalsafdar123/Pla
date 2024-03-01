import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.browser_context_args(storage_state="superuser_login_state.json")
def test_print_functionality(page: Page) -> None:
    """
    Going inside data of check on staging of zipnosis entity and then click on print and [age will be appear
    where the entity name should be same as that of the entity where you clicked the print button of entity
    """

    page.goto("/")
    expect(page.get_by_role("link", name="Support Account")).to_be_visible()
    go_to_entities_home(page)
    page.get_by_role("heading", name="Zipnosis").click()
    page.get_by_role("heading", name="check for homepage and default").click()
    page.get_by_role("tab", name="Data Access Control").click()
    page.get_by_placeholder("Search Data Access").fill("check for homepage and default")
    page.get_by_role("button", name="check for homepage and default").click()
    page.get_by_role("button", name="Column visibility").click()
    page.get_by_role("link", name="business_line_name").click()
    page.locator(".dt-button-background").click()

    with page.expect_popup() as popup_info:
        page.get_by_role("button", name="Print").click()
    page1 = popup_info.value
    #
    # page1.get_by_role("heading", name="Zipnosis Home").click()
    expect(page1.get_by_text("Zipnosis Home")).to_have_text(re.compile("Zipnosis Home"))
    page1.get_by_role("cell", name="finished_at").click()
    page1.get_by_role("cell", name="submitted_at").click()
    page1.get_by_role("cell", name="state").click()

    page.goto("/accounts/login")
    page.get_by_label("User Name").fill("admin")
    page.locator('input[type="password"]').fill("admin1PWD")
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_role("link", name="Support Account")).to_be_visible()
    go_to_entities_home(page)
    page.get_by_role("heading", name="Zipnosis").click()
    page.get_by_role("heading", name="check for homepage and default").click()
    page.get_by_role("tab", name="Data Access Control").click()
    page.get_by_placeholder("Search Data Access").fill("check for homepage and default")
    page.get_by_role("button", name="check for homepage and default").click()
    page.get_by_role("button", name="Column visibility").click()
    page.get_by_role("link", name="business_line_name").click()


def go_to_entities_home(page):
    sidebar_element = page.locator(".sidebar.collapsed")
    entity_gallery = sidebar_element.locator('a[href="/manage-database"]')
    entity_gallery.click()

import os

import pytest
from playwright.sync_api import Page, expect


def boolean_import(page, settings):
    imports_and_integrations = page.locator('a[href="/imports-integration"]')
    imports_and_integrations.click()
    page.get_by_role("link", name="Imports").click()
    page.get_by_role("link", name="New Import").first.click()

    page.get_by_label("Name Your Dataset").fill("Boolean Test")
    page.get_by_text("Select Entity").click()
    page.get_by_label("Zipnosis").click()
    page.get_by_text("Select Data Source").click()
    page.get_by_label("Csv").click()
    file_path = os.path.join(
        settings.ui_tests_root,
        "functionality_test/boolean_field.csv",
    )
    page.get_by_label("Choose file").set_input_files(file_path)
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(2000)
    page.get_by_role("heading", name="Start Import").click()
    page.wait_for_timeout(1000)


@pytest.mark.browser_context_args(storage_state="superuser_login_state.json")
def test_boolean_filter(page: Page, settings) -> None:
    """
    Boolean import is done and data is filtered on a boolean field True and False
    """
    page.goto("/")
    expect(page.get_by_role("link", name="Support Account")).to_be_visible()
    page.wait_for_timeout(1000)

    boolean_import(page, settings)
    go_to_entities_home(page)
    page.get_by_role("heading", name="zipnosis").click()
    page.get_by_role("heading", name="Boolean Test").click()
    page.get_by_role("tab", name="Data Access Control").click()
    page.get_by_role("button", name="Boolean Test").click()
    page.get_by_role("button", name="Advanced Filters").click()
    page.get_by_role("tabpanel", name="Data").get_by_text("booleanfield").click()
    page.locator(
        "#cl_booleanfie_oleanfield_f57400a9d828ec8d6389_select span"
    ).first.click()
    page.get_by_role("option", name="True").click()
    page.get_by_role("button", name="Insert Filter").click()
    page.get_by_role("button", name="Search", exact=True).click()
    page.get_by_role("heading", name="Passing (16)").click()
    page.wait_for_timeout(1000)
    page.locator('[data-ui-tests = "advanced-filters-edit-button"]').click()

    page.get_by_label("Data").get_by_title("True").locator("span").nth(1).click()
    page.get_by_role("option", name="True").click()
    page.get_by_role("option", name="False").click()
    page.get_by_role("button", name="Update Filter").click()
    page.get_by_role("button", name="Search", exact=True).click()
    page.get_by_role("heading", name="Passing (4,983)").click()
    page.wait_for_timeout(2000)
    page.locator('[data-ui-tests = "advanced-filters-edit-button"]').click()
    page.get_by_label("Data").get_by_title("False").locator("span").nth(1).click()
    page.get_by_role("option", name="True").click()
    page.get_by_role("button", name="Update Filter").click()
    page.get_by_role("button", name="Search", exact=True).click()
    page.get_by_role("heading", name="Passing (4,999)").click()


def go_to_entities_home(page):
    sidebar_element = page.locator(".sidebar.collapsed")
    entity_gallery = sidebar_element.locator('a[href="/manage-database"]')
    entity_gallery.click()

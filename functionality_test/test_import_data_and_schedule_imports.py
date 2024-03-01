import pytest
from playwright.sync_api import Page, expect


@pytest.mark.browser_context_args(storage_state="admin_test_user_login_state.json")
def test_import_data_and_scheduled_tasks(page: Page) -> None:
    """
    Import data is only done by admin accounts therefore to check it login with admin account go to administration
    then clicking on import no message is shown means it is working fine. Now checking with read only user and opening the administration
    section and seeing whether that import section is not there which is working fine
    """

    page.goto("/")
    expect(page.get_by_role("link", name="Admin Test User")).to_be_visible()
    imports_and_integrations = page.locator('a[href="/imports-integration"]')
    imports_and_integrations.click()
    expect(page.get_by_role("link", name="Imports")).to_be_visible()

    page.goto("/accounts/login")
    page.get_by_label("User Name").fill("readtestuser")
    page.locator('input[type="password"]').fill("admin1PWD")
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_role("link", name="Read Test User")).to_be_visible()
    imports_and_integrations = page.locator('a[href="/imports-integration"]')
    imports_and_integrations.click()

    expect(page.get_by_role("link", name="Imports")).not_to_be_visible()
    page.get_by_role("link", name="Scheduled Tasks").click()
    expect(page.get_by_role("button", name="Details")).not_to_be_visible()

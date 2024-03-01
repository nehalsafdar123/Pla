import pytest
from playwright.sync_api import Page, expect


@pytest.mark.browser_context_args(storage_state="user_tenant1_login_state.json")
def test_user_and_group_permission(page: Page) -> None:
    """
    going to users list in administration of user@tenant1 to see number of user therefore there is not user
    other than user1tenant1 now going to groups and seeing inside details to share with user 2 but that user is not
    found which is correct. Now going to tenant permission test and try to share the subdatset with a user but no
    user found which is also correct. Now checking number of groups which is 1 that is only of this tenant.
    """

    page.goto("/")
    expect(page.get_by_role("link", name="user1 tenant1")).to_be_visible()
    go_to_administration(page)
    page.get_by_role("link", name="Users").click()

    # checking there is only 1 user in tenant
    page.get_by_text("Showing 1 to 1 of 1 entries").click()

    go_to_administration(page)
    page.get_by_role("link", name="User Groups").click()
    page.get_by_role("button", name="Details").click()
    page.get_by_role("button", name="Edit").click()

    page.get_by_label("User Group Data").locator("span").nth(1).click()
    page.get_by_placeholder("Search...").fill("user2")
    expect(page.get_by_text("No items found")).to_contain_text("No items found")

    # page.get_by_role("heading", name="No data yet, choose from the").click()
    go_to_entities_home(page)
    page.get_by_role("heading", name="Vidyo CDR").click()
    page.get_by_role("heading", name="vidyo instance test's Data").click()

    # Click 'Permissions/Sharing' link
    page.get_by_role("tab", name="Data Access Control").click()
    page.locator('[data-ui-tests="share-subdataset"]').click()
    page.wait_for_timeout(1000)
    page.get_by_label("Share With").locator("span").first.click()

    # No item will found because there is no other user and then closing the opened dropdown
    expect(page.get_by_text("No items found")).to_contain_text("No items found")
    page.get_by_label("Share With").locator("span").first.click()

    # checking with groups now
    page.get_by_label("Share With").locator("span").nth(2).click()

    # Group will only contain 1 group since there is no other groups
    expect(page.get_by_role("option", name="Group Tenant1")).to_contain_text(
        "Group Tenant1"
    )


def go_to_administration(page):
    sidebar_element = page.locator(".sidebar.collapsed")
    administration = sidebar_element.locator('a[href="/administration"]')
    administration.click()


def go_to_entities_home(page):
    sidebar_element = page.locator(".sidebar.collapsed")
    entity_gallery = sidebar_element.locator('a[href="/manage-database"]')
    entity_gallery.click()

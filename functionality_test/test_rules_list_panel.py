import pytest
from playwright.sync_api import Page, expect


@pytest.mark.browser_context_args(storage_state="superuser_login_state.json")
def test_rules_list_panel(page: Page) -> None:  # noqa: MFL000
    """
    In this test case we apply filter and then check the test list rules panel . 1st filter is apply
    and then second . we will see by default and is here now i change "1 and 2" to "1 or 2" and then apply
    the 3rd filter . it should be "1 or 2 and 3" now by deleting filter whole test rule list is updated
    from or to and
    """

    page.goto("/")
    expect(page.get_by_role("link", name="Support Account")).to_be_visible()
    go_to_entities_home(page)
    page.get_by_role("heading", name="Zipnosis").click()
    page.get_by_role("heading", name="check on staging").click()
    page.get_by_role("tab", name="Data Access Control").click()
    page.get_by_role("button", name="check on staging").click()
    page.get_by_role("button", name="Advanced Filters").click()

    # Add first filter
    page.get_by_label("Data").get_by_text("business_line_name").click()
    page.locator(
        "#cl_businessli_sslinename_941fb7024a1c8dd864f0_select span"
    ).first.click()
    page.get_by_role("option", name="Virtual Urgent Care").click()
    page.get_by_role("button", name="Insert Filter").click()

    # Add Second filter
    page.get_by_label("Data").get_by_text("state").click()
    page.locator("#cl_state_a1ab826edde458068625_select > div > span").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("Search...").fill("1011")
    page.get_by_label("Data").get_by_text("1011").click()
    page.get_by_role("button", name="Insert Filter").click()
    page.get_by_label("Data").locator("span").click()

    # check if panel list have correct value
    expect(
        page.locator("span")
        .filter(has_text="Operators must be equal to")
        .get_by_role("textbox")
    ).to_have_value("1 AND 2")

    page.get_by_label("Data").get_by_text("finished_at").click()
    page.get_by_placeholder("Set Date Range").click()
    page.get_by_role("button", name="Apply").click()
    page.get_by_role("button", name="Insert Filter").click()
    expect(
        page.locator("span")
        .filter(has_text="Operators must be equal to")
        .get_by_role("textbox")
    ).to_have_value("1 AND 2 AND 3")

    # Add OR filter and update panel list
    page.locator("span").filter(has_text="Operators must be equal to").get_by_role(
        "textbox"
    ).fill("")
    page.locator("span").filter(has_text="Operators must be equal to").get_by_role(
        "textbox"
    ).fill("1 OR (2 AND 3)")

    # Delete to see if we get 1 AND 2 after deleting 1 filter
    page.locator('[data-ui-tests = "advanced-filters-delete-button"]').first.click()
    expect(
        page.locator("span")
        .filter(has_text="Operators must be equal to")
        .get_by_role("textbox")
    ).to_have_value("1 AND 2")

    page.locator("span").filter(has_text="Operators must be equal to").get_by_role(
        "textbox"
    ).fill("")
    page.locator("span").filter(has_text="Operators must be equal to").get_by_role(
        "textbox"
    ).fill("1 or 2")
    page.wait_for_timeout(2000)

    # Now add another filter we should get 1 OR (2 AND 3)
    page.get_by_label("Data").get_by_text("business_line_name", exact=True).click()
    page.locator(
        "#cl_businessli_sslinename_941fb7024a1c8dd864f0_select span"
    ).first.click()
    page.wait_for_timeout(1000)
    page.get_by_role("option", name="Virtual Urgent Care").click()
    page.get_by_role("button", name="Insert Filter").click()
    expect(
        page.locator("span")
        .filter(has_text="Operators must be equal to")
        .get_by_role("textbox")
    ).to_have_value("1 OR (2 AND 3)")


def go_to_entities_home(page):
    sidebar_element = page.locator(".sidebar.collapsed")
    entity_gallery = sidebar_element.locator('a[href="/manage-database"]')
    entity_gallery.click()

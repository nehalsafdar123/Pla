import pytest
from playwright.sync_api import Page, expect


@pytest.mark.browser_context_args(storage_state="superuser_login_state.json")
def test_string_filters_annual_void(page: Page) -> None:  # noqa: MFL000
    """
    Filtering test is being done on a fixed now of rows every time and on the same data. In this test case we are filtering on ENcounter Type consisting of operators IN, CONTAINS, STARTS WITH, ENDS WITH,
    having lower and upper case values. Also wrong values are inserted to see correct results. In the end inside contains operator i am using T double space to test out patient and result should be zero
    """

    page.goto("/")
    expect(page.get_by_role("link", name="Support Account")).to_be_visible()
    go_to_entities_home(page)

    page.get_by_role("heading", name="Encounter").click()
    page.get_by_role("heading", name="CH Drilldown2").click()
    page.get_by_role("tab", name="Data Access Control").click()
    page.get_by_role("button", name="CH Drilldown2").click()
    page.get_by_role("button", name="Advanced Filters").click()
    page.get_by_placeholder("Search for filter").fill("Encounter")
    page.get_by_role("tabpanel", name="Data").get_by_text("Encounter Type").click()
    page.locator(
        "#cl_encountert_ountertype_db407875c277e3efb193_select span"
    ).first.click()
    page.get_by_placeholder("Search...").fill("Ann")

    # Filter Annual selected
    page.get_by_role("option", name="Annual").click()
    page.get_by_role("button", name="Insert Filter").click()
    page.get_by_role("button", name="Search").first.click()
    page.get_by_role("cell", name="133", exact=True).click()
    page.get_by_role("heading", name="Passing (133)").click()
    page.wait_for_timeout(2000)
    page.locator('[data-ui-tests = "advanced-filters-edit-button"]').click()
    page.get_by_title("In", exact=True).locator("span").nth(2).click()
    page.get_by_placeholder("Search...").fill("Start")
    page.get_by_role("option", name="Starts With").click()

    # Filtering on Ann
    page.get_by_label("Encounter Type", exact=True).fill("")
    page.get_by_label("Encounter Type", exact=True).fill("Ann")
    page.get_by_role("button", name="Update Filter").click()
    page.get_by_role("cell", name="Encounter Type (Starts With Ann)").click()
    page.get_by_role("button", name="Search").first.click()
    page.get_by_role("cell", name="133", exact=True).click()
    page.get_by_role("heading", name="Passing (133)").click()
    page.wait_for_timeout(2000)
    page.locator('[data-ui-tests = "advanced-filters-edit-button"]').click()
    page.wait_for_timeout(1000)
    page.get_by_label("Encounter Type", exact=True).fill("ann")
    page.get_by_role("button", name="Update Filter").click()
    page.get_by_role("cell", name="Encounter Type (Starts With ann)").click()
    page.get_by_role("button", name="Search").first.click()
    page.get_by_role("cell", name="133", exact=True).click()
    page.get_by_role("heading", name="Passing (133)").click()
    page.wait_for_timeout(2000)
    page.locator('[data-ui-tests = "advanced-filters-edit-button"]').click()

    # Filtering on al
    page.get_by_label("Encounter Type", exact=True).fill("")
    page.get_by_label("Encounter Type", exact=True).fill("al")
    page.get_by_role("button", name="Update Filter").click()
    page.get_by_role("cell", name="Encounter Type (Starts With al)").click()
    page.get_by_role("cell", name="0", exact=True).first.click()
    page.locator('[data-ui-tests = "advanced-filters-edit-button"]').click()
    page.get_by_title("Starts With", exact=True).locator("span").nth(2).click()

    # Now changing operator and using Starts with to test further
    page.get_by_placeholder("Search...").fill("Ends")
    page.get_by_role("option", name="Ends With").click()

    # Filtering on 'al'
    page.get_by_role("button", name="Update Filter").click()
    page.get_by_role("cell", name="Encounter Type (Ends With al)").click()
    page.get_by_role("button", name="Search").first.click()
    page.get_by_role("cell", name="133", exact=True).click()
    page.get_by_role("heading", name="Passing (133)").click()
    page.wait_for_timeout(1000)
    page.locator('[data-ui-tests = "advanced-filters-edit-button"]').click()

    # 78. Filtering on 'AL'
    page.get_by_label("Encounter Type", exact=True).fill("AL")
    page.get_by_role("button", name="Update Filter").click()
    page.get_by_role("cell", name="Encounter Type (Ends With AL)").click()
    page.get_by_role("button", name="Search").first.click()
    page.get_by_role("cell", name="133", exact=True).click()
    page.wait_for_timeout(3000)
    page.locator('[data-ui-tests = "advanced-filters-edit-button"]').click()

    # Filtering on 'A' the second last word
    page.get_by_label("Encounter Type", exact=True).fill("")
    page.get_by_label("Encounter Type", exact=True).fill("A")
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Update Filter").click()
    page.get_by_role("cell", name="Encounter Type (Ends With A)").click()
    page.get_by_role("cell", name="0", exact=True).first.click()
    page.wait_for_timeout(1000)
    page.locator('[data-ui-tests = "advanced-filters-edit-button"]').click()
    page.get_by_title("Ends With", exact=True).locator("span").nth(2).click()
    page.get_by_placeholder("Search...").fill("Contains")
    page.get_by_role("option", name="Contains").click()

    # Filtering on 'id' in contains operator
    page.get_by_label("Encounter Type", exact=True).fill("id")
    page.get_by_role("button", name="Update Filter").click()
    page.get_by_role("cell", name="Encounter Type (Contains id)").click()
    page.get_by_role("button", name="Search").first.click()
    page.get_by_role("cell", name="134", exact=True).click()
    page.wait_for_timeout(1000)
    page.locator('[data-ui-tests = "advanced-filters-edit-button"]').click()

    # Checking result with T P
    page.get_by_label("Encounter Type", exact=True).fill("")
    page.get_by_label("Encounter Type", exact=True).fill("T P")
    page.get_by_role("button", name="Update Filter").click()
    page.get_by_role("cell", name="Encounter Type (Contains T P)").click()
    page.get_by_role("cell", name="131", exact=True).click()
    page.locator('[data-ui-tests = "advanced-filters-edit-button"]').click()
    page.get_by_label("Encounter Type", exact=True).fill("t  ")
    page.get_by_role("button", name="Update Filter").click()

    # Checking result with double space between two results
    page.get_by_role("cell", name="Encounter Type (Contains t  )").click()
    page.get_by_role("cell", name="0", exact=True).first.click()


def go_to_entities_home(page):
    sidebar_element = page.locator(".sidebar.collapsed")
    entity_gallery = sidebar_element.locator('a[href="/manage-database"]')
    entity_gallery.click()

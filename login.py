from playwright.sync_api import Page, expect


def test_superuser_login(page: Page):
    """
    The idea here is to save the logged-in user state (access token, refresh token, ...)
    in a file and then load that state at the start of every test to avoid having to
    log in for every test.
    """
    page.goto("/accounts/login")
    page.get_by_label("User Name").fill("admin")
    page.locator('input[type="password"]').fill("admin1PWD")
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_role("link", name="Support Account")).to_be_visible()
    page.context.storage_state(path="superuser_login_state.json")


def test_user_tenant1_login(page: Page):
    page.goto("/accounts/login")
    page.get_by_label("User Name").fill("user@tenant1")
    page.locator('input[type="password"]').fill("admin1PWD")
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_role("link", name="user1 tenant1")).to_be_visible()
    page.context.storage_state(path="user_tenant1_login_state.json")


def test_user_tenant2_login(page: Page):
    page.goto("/accounts/login")
    page.get_by_label("User Name").fill("user@tenant2")
    page.locator('input[type="password"]').fill("admin1PWD")
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_role("link", name="user2 tenant2")).to_be_visible()
    page.context.storage_state(path="user_tenant2_login_state.json")


def test_admin_test_user_login(page: Page):
    page.goto("/accounts/login")
    page.get_by_label("User Name").fill("admintestuser")
    page.locator('input[type="password"]').fill("admin1PWD")
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_role("link", name="Admin Test User")).to_be_visible()
    page.context.storage_state(path="admin_test_user_login_state.json")


def test_read_test_user_login(page: Page):
    page.goto("/accounts/login")
    page.get_by_label("User Name").fill("readtestuser")
    page.locator('input[type="password"]').fill("admin1PWD")
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_role("link", name="Read Test User")).to_be_visible()
    page.context.storage_state(path="read_test_user_login_state.json")

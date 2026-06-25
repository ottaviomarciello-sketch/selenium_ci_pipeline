import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage


def test_login_success(page: Page):
    base_url = "https://demoqa.com"

    login_page = LoginPage(page)

    login_page.go(base_url)

    def test_login(page, user_data):
        login_page.login(user_data["username"], user_data["password"])

    # assertion (molto importante!)
    page.wait_for_selector("#userName-value")
    assert page.inner_text("#userName-value") == 'ottymrc'

    page.wait_for_selector("#gotoStore", timeout=5000)

    assert page.locator("#gotoStore").is_visible()
import pytest
from project_demoqa.pages.login_page import LoginPage
from project_demoqa.utils.config import USERNAME, PASSWORD

@pytest.mark.smoke
def test_login_success(page):
    login_page = LoginPage(page)

    login_page.go_to_login()
    login_page.login(USERNAME, PASSWORD)

    assert login_page.is_login_successful()


@pytest.mark.parametrize("user, password", [
    ("wrongUser", "Password.82!"),
    ("ottymrc", "wrongPass"),
])
def test_login_fail(page, user, password):
    login_page = LoginPage(page)

    login_page.go_to_login()
    login_page.login(user, password)

    assert "Invalid" in login_page.get_error_message()
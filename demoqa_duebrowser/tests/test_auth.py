from demoqa_duebrowser.pages.login_page import LoginPage
from demoqa_duebrowser.pages.register_page import RegisterPage
from demoqa_duebrowser.utils.config import BASE_URL


def test_register_and_login(page):
    register_page = RegisterPage(page)
    login_page = LoginPage(page)

    # genera utente random
    username, password = register_page.generate_user()

    # prova registrazione (simulata)
    register_page.go(BASE_URL)
    register_page.register(username, password)

    # login
    login_page.go(BASE_URL)
    login_page.login(username, password)

    page.wait_for_selector("#userName-value", timeout=5000)

    assert username in page.locator("#userName-value").text_content()


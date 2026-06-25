import pytest
from playwright.sync_api import sync_playwright
from project_demoqa.utils.config import HEADLESS

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=HEADLESS,
            slow_mo=300
        )
        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()
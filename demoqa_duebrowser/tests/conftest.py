import pytest
from playwright.sync_api import sync_playwright
from demoqa_duebrowser.utils.config import HEADLESS


# parametrizzazione browser (Chrome + Edge)
@pytest.fixture(params=["chromium", "edge"])
def browser_type(request):
    return request.param

@pytest.fixture(scope="function")
def page(browser_type):
    with sync_playwright() as p:

        if browser_type == "chromium":
            browser = p.chromium.launch(headless=HEADLESS)

        elif browser_type == "edge":
            browser = p.chromium.launch(
                channel="msedge",
                headless=HEADLESS
            )
<<<<<
        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()
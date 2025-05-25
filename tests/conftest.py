import pytest
from playwright.sync_api import sync_playwright

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="class")
def browser(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--window-size=1920,1080"
            ]
        )
        context = browser.new_context(viewport=None)
        page = context.new_page()
        request.cls.page = page
        yield page
        browser.close()

from pages.base_page import BasePage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

class HomeAccountPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def get_home_account_message(self,username):
        try:
            locator = self.page.locator("h1", has_text=f"Welcome, {username}")
            return locator
        except PlaywrightTimeoutError:
            raise AssertionError("Expected Google Home Text was not displayed.")
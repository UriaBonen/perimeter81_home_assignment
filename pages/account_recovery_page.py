from pages.base_page import BasePage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


class AccountRecoveryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def get_account_recovery_message(self):
        try:
            locator = self.page.locator("#headingText",has_text="Account Recovery")
            locator.wait_for(state="visible")
            return locator
        except PlaywrightTimeoutError:
            raise AssertionError("Expected Account Recovery Text was not displayed.")

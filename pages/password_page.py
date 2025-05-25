from pages.base_page import BasePage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


class PasswordPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.password_input = ".whsOnd.zHQkBf"
        self.forgot_password_button = "Forgot password?"

    def fill_password(self, password):
        self.page.get_by_label("Enter your password").wait_for(state="visible")
        self.page.get_by_label("Enter your password").fill(password)

    def click_login_button(self):
        self.click_by_role(role="button", name="Next")

    def click_next_button(self):
        self.click_by_role(role="button", name="Next")

    def click_forgot_password(self):
        self.click_by_role(role="button",name=self.forgot_password_button)

    def get_empty_password_error_message(self):
        try:
            locator = self.page.locator('div[aria-live="polite"] >> text=Enter a password')
            locator.wait_for(state="visible")
            return locator
        except PlaywrightTimeoutError:
            raise AssertionError("Expected error message for empty password was not displayed.")

    def get_wrong_password_error_message(self):
        try:
            locator = self.page.locator('div[aria-live="polite"] >> text=Wrong password')
            locator.wait_for(state="visible")
            return locator
        except PlaywrightTimeoutError:
            raise AssertionError("Expected error message for wrong password was not displayed.")



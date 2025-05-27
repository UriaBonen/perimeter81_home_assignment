from pages.base_page import BasePage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = "#identifierId"


    def fill_username(self, username):
        self.fill(self.username_input, username)

    def click_next_button(self):
        self.click_by_role(role="button", name="Next")


    def get_empty_email_error_message(self):
        try:
            locator = self.page.locator("div.Ekjuhf.Jj6Lae")
            locator.wait_for(state="visible")
            return locator
        except PlaywrightTimeoutError:
            raise AssertionError("Expected error message for empty email was not displayed.")

    def get_invalid_email_error_message(self):
        try:
            locator = self.page.locator("div.Ekjuhf.Jj6Lae")
            locator.wait_for(state="visible")
            return locator
        except PlaywrightTimeoutError:
            raise AssertionError("Expected error message for invalid email was not displayed.")









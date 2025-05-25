from hamcrest import assert_that

from pages.base_page import BasePage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


class TwoStepVerificationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.two_step_verification_message = "#headingText"
        self.two_step_message = '2-Step Verification'

    def validate_two_step_verification_message_is_visible(self):
        self.page.locator(self.two_step_verification_message,has_text=self.two_step_message).wait_for(state='visible')
        element_text = self.get_text(selector=self.two_step_verification_message)
        assert self.two_step_message in element_text


    def get_two_step_verification_text(self):
        try:
            locator = self.page.locator(self.two_step_verification_message,has_text=self.two_step_message)
            locator.wait_for(state="visible")
            return locator
        except PlaywrightTimeoutError:
            raise AssertionError("Expected error message for wrong password was not displayed.")

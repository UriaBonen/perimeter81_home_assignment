import pytest
from hamcrest import assert_that, equal_to
from pyexpat.errors import messages

import utils.data
from pages.account_recovery_page import AccountRecoveryPage
from pages.home_account_page import HomeAccountPage
from pages.login_page import LoginPage
from pages.password_page import PasswordPage
from pages.two_step_verification_page import TwoStepVerificationPage
from tests.conftest import browser
from utils.data import valid_users
from utils.messages import empty_email_error_message, not_exist_mail_error_message, invalid_mail_error_message, \
    empty_password_message, wrong_password_error_message, home_page_message

pytest.mark.usefixtures("browser")


class TestLoginPage:

    def setup_method(self):
        self.login_page = LoginPage(self.page)
        self.password_page = PasswordPage(self.page)
        self.two_step_verification = TwoStepVerificationPage(self.page)
        self.account_recovery_page = AccountRecoveryPage(self.page)
        self.home_page_account = HomeAccountPage(self.page)
        self.page.goto("https://accounts.google.com/")

    def test_send_empty_mail_present_an_error_message(self, browser):
        """TC1: Negative test: empty username,Expected result -> appropriate error message  """
        self.login_page.fill_username('')
        self.login_page.click_next_button()
        error_msg = self.login_page.get_empty_email_error_message().inner_text()
        assert_that(error_msg, equal_to(empty_email_error_message))

    @pytest.mark.parametrize("invalid_email", utils.data.invalid_mail_adders)
    def test_invalid_email(self, browser, invalid_email):
        """TC2: Negative test: invalid username, Expected result -> appropriate error message"""
        self.login_page.fill_username(invalid_email)
        self.login_page.click_next_button()
        error_msg = self.login_page.get_invalid_email_error_message().inner_text()
        assert_that(error_msg, equal_to(invalid_mail_error_message))

    @pytest.mark.parametrize("not_exist_email", utils.data.not_exist_email)
    def test_not_exist_email(self, browser, not_exist_email):
        """TC3: Negative test: Not exist username, Expected result -> appropriate error message"""
        self.login_page.fill_username(not_exist_email)
        self.login_page.click_next_button()
        error_msg = self.login_page.get_invalid_email_error_message().inner_text()
        assert_that(error_msg, equal_to(not_exist_mail_error_message))

    def test_send_empty_password_present_an_error_message(self, browser):
        """TC4: Negative test: empty password ,Expected result -> appropriate error message  """
        self.login_page.fill_username(valid_users.get('mail'))
        self.login_page.click_next_button()
        self.password_page.fill_password(password='')
        self.login_page.click_next_button()
        error_msg = self.password_page.get_empty_password_error_message().inner_text()
        assert_that(error_msg, equal_to(empty_password_message))

    @pytest.mark.parametrize("invalid_password", utils.data.invalid_password)
    def test_wrong_password(self, browser, invalid_password):
        """TC5: Negative test: Valid email wrong password , Expected result -> appropriate error message"""
        self.login_page.fill_username(valid_users.get('mail'))
        self.login_page.click_next_button()
        self.password_page.fill_password(password=invalid_password)
        self.login_page.click_next_button()
        error_msg = self.password_page.get_wrong_password_error_message().inner_text()
        assert_that(error_msg, equal_to(wrong_password_error_message))

    def test_forgot_password(self, browser):
        """TC6: validate that click on forgot password button lead to account recovery screen"""
        self.login_page.fill_username(valid_users.get('mail'))
        self.login_page.click_next_button()
        self.password_page.click_forgot_password()
        account_recovery_text = self.account_recovery_page.get_account_recovery_message().inner_text()
        assert_that('Account recovery', equal_to(account_recovery_text))

    def test_valid_login(self, browser):
        """TC7: Positive main login flow, valid username and password, expected result -> home page screen  """
        self.login_page.fill_username(valid_users.get('mail'))
        self.login_page.click_next_button()
        self.password_page.fill_password(password=valid_users.get('password'))
        self.password_page.click_next_button()
        home_page_account_text = self.home_page_account.get_home_account_message(
            username=valid_users.get('user_name')).inner_text()
        assert_that((home_page_message + valid_users.get('user_name')), equal_to(home_page_account_text))

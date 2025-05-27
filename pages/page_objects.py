from pages.account_recovery_page import AccountRecoveryPage
from pages.login_page import LoginPage
from pages.password_page import PasswordPage
from pages.home_account_page import HomeAccountPage
from pages.two_step_verification_page import TwoStepVerificationPage


class PageObjects:
    def __init__(self, page):
        self.page = page
        self.login_page = LoginPage(page)
        self.password_page = PasswordPage(page)
        self.two_step_verification = TwoStepVerificationPage(page)
        self.account_recovery_page = AccountRecoveryPage(page)
        self.home_page_account = HomeAccountPage(page)

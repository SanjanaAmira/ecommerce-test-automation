
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "form[action='/login'] p")

    def open_login_page(self, base_url):
        self.open(f"{base_url}/login")

    def login(self, email, password):
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

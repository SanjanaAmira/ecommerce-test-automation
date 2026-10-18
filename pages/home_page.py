
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    LOGGED_IN_LABEL = (
        By.XPATH,
        "//a[contains(., 'Logged in as')]"
    )

    def is_logged_in(self):
        return self.wait.until(
            lambda driver: any(
                element.is_displayed()
                for element in driver.find_elements(
                    *self.LOGGED_IN_LABEL
                )
            )
        )

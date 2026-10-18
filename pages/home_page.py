
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class HomePage(BasePage):
    LOGGED_IN_LABEL = (
        By.XPATH,
        "//a[contains(., 'Logged in as')]"
    )
    
    LOGOUT_LINK = (
        By.XPATH,
        "//a[@href='/logout']"
    )
    
    SEARCH_INPUT = (
        By.ID,
        "search_product"
    )
    
    SEARCH_BUTTON = (
        By.ID,
        "submit_search"
    )

    def open_home_page(self, base_url):
        """Navigate to home page."""
        self.open(base_url)

    def is_logged_in(self):
        """Check if user is logged in by looking for 'Logged in as' text."""
        return self.wait.until(
            lambda driver: any(
                element.is_displayed()
                for element in driver.find_elements(
                    *self.LOGGED_IN_LABEL
                )
            )
        )

    def logout(self):
        """Click the logout link."""
        self.click(self.LOGOUT_LINK)

    def search_product(self, search_term):
        """Enter search term and click search button."""
        self.type(self.SEARCH_INPUT, search_term)
        self.click(self.SEARCH_BUTTON)

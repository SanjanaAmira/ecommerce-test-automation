
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        """Wait for element to be present and return it."""
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        """Wait for element to be clickable then click it."""
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type(self, locator, text):
        """Wait for element, clear it, and type text."""
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Wait for element to be visible and get its text."""
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

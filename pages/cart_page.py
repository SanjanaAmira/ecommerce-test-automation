
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, "#cart_info_table tbody tr")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#cart_info_table .cart_description h4 a")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#cart_info_table .cart_price p")
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, "#cart_info_table .cart_quantity button")

    def open_cart_page(self, base_url):
        """Navigate to cart page and wait for page to load."""
        self.open(f"{base_url}/view_cart")
        # Wait for the cart section to be present
        self.wait.until(
            EC.presence_of_element_located((By.ID, "cart_items"))
        )

    def cart_has_items(self):
        return len(self.driver.find_elements(*self.CART_ITEMS)) > 0

    def get_product_name(self):
        return self.find(self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.find(self.PRODUCT_PRICE).text

    def get_product_quantity(self):
        return self.find(self.PRODUCT_QUANTITY).text

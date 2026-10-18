
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, "#cart_info_table tbody tr")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#cart_info_table .cart_description h4 a")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#cart_info_table .cart_price p")
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, "#cart_info_table .cart_quantity button")
    
    # Remove button
    REMOVE_BUTTON = (By.CSS_SELECTOR, ".cart_quantity_delete")
    
    # Checkout button
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//a[contains(text(), 'Proceed To Checkout')]")
    
    # Empty cart message
    EMPTY_CART_MESSAGE = (By.XPATH, "//b[contains(text(), 'Cart is empty')]")

    def open_cart_page(self, base_url):
        """Navigate to cart page and wait for page to load."""
        self.open(f"{base_url}/view_cart")
        # Wait for the cart section to be present
        self.wait.until(
            EC.presence_of_element_located((By.ID, "cart_items"))
        )

    def cart_has_items(self):
        """Check if cart contains any items."""
        return len(self.driver.find_elements(*self.CART_ITEMS)) > 0

    def get_cart_item_count(self):
        """Get the number of items in the cart."""
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_product_name(self):
        """Get the name of the first product in cart."""
        return self.find(self.PRODUCT_NAME).text

    def get_product_price(self):
        """Get the price of the first product in cart."""
        return self.find(self.PRODUCT_PRICE).text

    def get_product_quantity(self):
        """Get the quantity of the first product in cart."""
        return self.find(self.PRODUCT_QUANTITY).text

    def remove_first_product(self):
        """Click the remove button for the first product."""
        self.click(self.REMOVE_BUTTON)
        # Wait a moment for the removal to process
        import time
        time.sleep(1)

    def is_cart_empty(self):
        """Check if cart is empty."""
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.EMPTY_CART_MESSAGE)
            ).is_displayed()
        except Exception:
            # If no items exist, cart is empty
            return not self.cart_has_items()

    def proceed_to_checkout(self):
        """Click the Proceed to Checkout button."""
        self.click(self.PROCEED_TO_CHECKOUT_BUTTON)

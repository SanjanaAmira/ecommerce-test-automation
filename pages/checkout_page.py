
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # Delivery address section
    DELIVERY_ADDRESS_SECTION = (
        By.ID,
        "address_delivery"
    )
    
    # Billing address section
    BILLING_ADDRESS_SECTION = (
        By.ID,
        "address_invoice"
    )
    
    # Order review section
    ORDER_REVIEW_TABLE = (
        By.ID,
        "cart_info"
    )
    
    # Comment box
    COMMENT_TEXTAREA = (
        By.CSS_SELECTOR,
        "textarea[name='message']"
    )
    
    # Place order button
    PLACE_ORDER_BUTTON = (
        By.XPATH,
        "//a[contains(text(), 'Place Order')]"
    )
    
    # Login modal elements (shown when not logged in)
    LOGIN_MODAL = (
        By.CSS_SELECTOR,
        ".modal-content"
    )
    
    REGISTER_LOGIN_LINK = (
        By.XPATH,
        "//u[contains(text(), 'Register / Login')]"
    )

    def is_delivery_address_shown(self):
        """Check if delivery address section is visible."""
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.DELIVERY_ADDRESS_SECTION)
            ).is_displayed()
        except Exception:
            return False

    def is_order_review_shown(self):
        """Check if order review table is visible."""
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.ORDER_REVIEW_TABLE)
            ).is_displayed()
        except Exception:
            return False

    def is_login_modal_shown(self):
        """Check if login modal or register/login link appears."""
        try:
            # Check if we're on the login page (redirected)
            current_url = self.driver.current_url
            if "/login" in current_url:
                return True
            
            # Or check for modal/link
            return self.wait.until(
                EC.visibility_of_element_located(self.REGISTER_LOGIN_LINK)
            ).is_displayed()
        except Exception:
            return False

    def enter_comment(self, comment):
        """Enter a comment in the order comment box."""
        self.type(self.COMMENT_TEXTAREA, comment)

    def click_place_order(self):
        """Click the Place Order button."""
        self.click(self.PLACE_ORDER_BUTTON)

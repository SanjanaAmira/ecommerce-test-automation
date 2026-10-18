
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage


class ProductsPage(BasePage):
    PRODUCTS_TITLE = (
        By.XPATH,
        "//h2[contains(., 'All Products')]"
    )

    PRODUCT_CARDS = (
        By.CSS_SELECTOR,
        ".features_items .product-image-wrapper"
    )

    FIRST_PRODUCT_NAME = (
        By.CSS_SELECTOR,
        ".features_items .productinfo p"
    )

    FIRST_PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        ".features_items .productinfo h2"
    )

    FIRST_ADD_TO_CART = (
        By.CSS_SELECTOR,
        ".features_items .productinfo a.add-to-cart"
    )

    VIEW_CART_LINK = (
        By.CSS_SELECTOR,
        "#cartModal a[href='/view_cart']"
    )

    CONTINUE_SHOPPING_BUTTON = (
        By.CSS_SELECTOR,
        "button[data-dismiss='modal']"
    )

    def open_products_page(self, base_url):
        self.open(f"{base_url}/products")
        self.wait.until(
            EC.visibility_of_element_located(self.PRODUCTS_TITLE)
        )

    def products_are_visible(self):
        return len(
            self.driver.find_elements(*self.PRODUCT_CARDS)
        ) > 0

    def get_first_product_name(self):
        return self.find(self.FIRST_PRODUCT_NAME).text

    def get_first_product_price(self):
        return self.find(self.FIRST_PRODUCT_PRICE).text

    def add_first_product_to_cart(self, navigate_to_cart=False):
        """
        Add first product to cart.
        
        Args:
            navigate_to_cart: If True, attempts to navigate to cart via modal.
                            If False, dismisses modal and stays on products page.
        """
        from selenium.webdriver.support.ui import WebDriverWait
        
        product_button = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_ADD_TO_CART)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            product_button
        )

        ActionChains(self.driver).move_to_element(
            product_button
        ).pause(0.5).click().perform()

        # Use shorter wait for modal handling
        short_wait = WebDriverWait(self.driver, 3)
        
        # Handle the modal that appears after adding to cart
        if navigate_to_cart:
            # Click "View Cart" in the modal
            try:
                view_cart = short_wait.until(
                    EC.element_to_be_clickable(self.VIEW_CART_LINK)
                )
                view_cart.click()
            except Exception:
                # Modal didn't appear, continue
                pass
        else:
            # Dismiss the modal by clicking "Continue Shopping"
            try:
                continue_btn = short_wait.until(
                    EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BUTTON)
                )
                continue_btn.click()
            except Exception:
                # Modal didn't appear or already closed
                pass

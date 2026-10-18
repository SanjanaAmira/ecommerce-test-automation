
import pytest

from config import BASE_URL, TEST_EMAIL, TEST_PASSWORD
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


# TC_LOGIN_06
def test_logout_after_login(driver):
    """Verify that a logged-in user can logout successfully."""
    if not TEST_EMAIL or not TEST_PASSWORD:
        pytest.skip("TEST_EMAIL and TEST_PASSWORD must be set in .env file")
    
    # Login first
    login_page = LoginPage(driver)
    login_page.open_login_page(BASE_URL)
    login_page.login(TEST_EMAIL, TEST_PASSWORD)
    
    # Verify logged in
    home_page = HomePage(driver)
    assert home_page.is_logged_in(), "User should be logged in"
    
    # Logout
    home_page.logout()
    
    # Verify redirected to login page
    assert "/login" in driver.current_url, "Should be redirected to login page after logout"


# TC_CHECKOUT_01
def test_checkout_logged_out_requires_login(driver):
    """Verify that attempting to checkout while logged out prompts for login."""
    # Add product to cart (while logged out) and navigate via modal
    products_page = ProductsPage(driver)
    products_page.open_products_page(BASE_URL)
    products_page.add_first_product_to_cart(navigate_to_cart=True)
    
    # Wait for cart page to load
    import time
    time.sleep(2)
    
    # Verify we're on cart page
    cart_page = CartPage(driver)
    assert "/view_cart" in driver.current_url or "/cart" in driver.current_url, "Should be on cart page"
    
    # Click Proceed to Checkout
    cart_page.proceed_to_checkout()
    
    # Wait for redirect or modal
    time.sleep(3)
    
    # Verify either on login page or modal shows
    current_url = driver.current_url
    is_on_login_page = "/login" in current_url
    
    # If not redirected, check for modal/link
    if not is_on_login_page:
        try:
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            
            short_wait = WebDriverWait(driver, 5)
            register_link = short_wait.until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//u[contains(text(), 'Register / Login')] | //a[contains(text(), 'Register / Login')]"
                ))
            )
            is_on_login_page = register_link.is_displayed()
        except Exception:
            pass
    
    assert is_on_login_page, f"Should redirect to login page or show login prompt. Current URL: {current_url}"


# TC_CHECKOUT_02
def test_checkout_logged_in_shows_address_and_review(driver):
    """Verify that checkout while logged in shows delivery address and order review."""
    if not TEST_EMAIL or not TEST_PASSWORD:
        pytest.skip("TEST_EMAIL and TEST_PASSWORD must be set in .env file")
    
    # Login first
    login_page = LoginPage(driver)
    login_page.open_login_page(BASE_URL)
    login_page.login(TEST_EMAIL, TEST_PASSWORD)
    
    # Verify logged in
    home_page = HomePage(driver)
    assert home_page.is_logged_in(), "User should be logged in"
    
    # Add product to cart
    products_page = ProductsPage(driver)
    products_page.open_products_page(BASE_URL)
    products_page.add_first_product_to_cart(navigate_to_cart=False)
    
    # Navigate to cart
    cart_page = CartPage(driver)
    cart_page.open_cart_page(BASE_URL)
    
    # Click Proceed to Checkout
    cart_page.proceed_to_checkout()
    
    # Verify checkout page shows address and order review
    checkout_page = CheckoutPage(driver)
    assert checkout_page.is_delivery_address_shown(), "Delivery address section should be visible"
    assert checkout_page.is_order_review_shown(), "Order review section should be visible"

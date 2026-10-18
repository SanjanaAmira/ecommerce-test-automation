
from config import BASE_URL
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


# TC_PROD_03
def test_products_page_displays_products(driver):
    """Verify that the products page displays product cards."""
    products_page = ProductsPage(driver)
    products_page.open_products_page(BASE_URL)

    assert products_page.products_are_visible(), "Products should be visible on products page"


# TC_PROD_04
def test_first_product_has_name_and_price(driver):
    """Verify that the first product has both a name and price displayed."""
    products_page = ProductsPage(driver)
    products_page.open_products_page(BASE_URL)

    product_name = products_page.get_first_product_name().strip()
    product_price = products_page.get_first_product_price().strip()
    
    assert product_name, "First product should have a name"
    assert product_price, "First product should have a price"


# TC_CART_01
def test_added_product_appears_in_cart(driver):
    """Verify that a product added to cart appears in the cart with correct name."""
    products_page = ProductsPage(driver)
    products_page.open_products_page(BASE_URL)

    # Get expected product name before adding to cart
    expected_name = products_page.get_first_product_name()
    
    # Add to cart and navigate via modal
    products_page.add_first_product_to_cart(navigate_to_cart=True)

    # We should now be on the cart page
    cart_page = CartPage(driver)
    # Wait a moment to ensure we're on cart page
    import time
    time.sleep(1)

    assert cart_page.cart_has_items(), "Cart should contain items"
    actual_name = cart_page.get_product_name()
    assert actual_name == expected_name, f"Expected '{expected_name}' but got '{actual_name}'"


# TC_CART_03
def test_cart_product_has_price_and_quantity(driver):
    """Verify that cart items display price and quantity correctly."""
    products_page = ProductsPage(driver)
    products_page.open_products_page(BASE_URL)
    
    # Add product to cart without navigating
    products_page.add_first_product_to_cart(navigate_to_cart=False)

    # Navigate to cart page explicitly
    cart_page = CartPage(driver)
    cart_page.open_cart_page(BASE_URL)

    product_price = cart_page.get_product_price().strip()
    product_quantity = cart_page.get_product_quantity()
    
    assert product_price, "Cart product should have a price"
    assert int(product_quantity) >= 1, f"Cart quantity should be at least 1, got {product_quantity}"


from config import BASE_URL
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


# TC_CART_05
def test_remove_item_from_cart(driver):
    """Verify that a product can be removed from the cart."""
    products_page = ProductsPage(driver)
    products_page.open_products_page(BASE_URL)
    
    # Add product to cart
    products_page.add_first_product_to_cart(navigate_to_cart=False)
    
    # Navigate to cart
    cart_page = CartPage(driver)
    cart_page.open_cart_page(BASE_URL)
    
    # Verify cart has items
    assert cart_page.cart_has_items(), "Cart should have items before removal"
    
    # Remove the product
    cart_page.remove_first_product()
    
    # Verify cart is empty
    assert cart_page.is_cart_empty(), "Cart should be empty after removing the product"


# TC_CART_02
def test_add_two_different_products(driver):
    """Verify that two different products can be added to cart."""
    products_page = ProductsPage(driver)
    products_page.open_products_page(BASE_URL)
    
    # Add first product and get its name
    first_product_name = products_page.get_first_product_name()
    products_page.add_first_product_to_cart(navigate_to_cart=False)
    
    # Wait for modal to appear and dismiss it
    import time
    time.sleep(2)
    
    # Scroll back to see second product
    driver.execute_script("window.scrollTo(0, 400);")
    time.sleep(1)
    
    # Add second product
    second_product_name = products_page.get_second_product_name()
    products_page.add_second_product_to_cart(navigate_to_cart=False)
    
    # Wait for modal
    time.sleep(2)
    
    # Navigate to cart
    cart_page = CartPage(driver)
    cart_page.open_cart_page(BASE_URL)
    
    # Verify cart has 2 items
    item_count = cart_page.get_cart_item_count()
    assert item_count == 2, f"Cart should have 2 items, but has {item_count}"
    
    # Additional verification: products should be different
    assert first_product_name != second_product_name, "The two products should have different names"

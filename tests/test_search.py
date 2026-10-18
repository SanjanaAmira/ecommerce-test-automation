
from config import BASE_URL
from pages.products_page import ProductsPage


# TC_PROD_01
def test_search_existing_product(driver):
    """Verify that searching for an existing product shows results."""
    # Navigate to products page which has the search feature
    products_page = ProductsPage(driver)
    products_page.open_products_page(BASE_URL)
    
    # Scroll to top to find search
    driver.execute_script("window.scrollTo(0, 0);")
    
    # Use products page search functionality
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    
    # Find and use search on products page
    search_input = products_page.wait.until(
        EC.visibility_of_element_located((By.ID, "search_product"))
    )
    search_input.send_keys("Top")
    
    search_button = products_page.find((By.ID, "submit_search"))
    search_button.click()
    
    # Verify search results are shown
    assert products_page.search_results_are_shown(), "Search results title should be displayed"
    assert products_page.products_are_visible(), "At least one product should be in search results"


# TC_PROD_02
def test_search_nonexistent_product(driver):
    """Verify that searching for a nonexistent product shows no results."""
    # Navigate to products page which has the search feature
    products_page = ProductsPage(driver)
    products_page.open_products_page(BASE_URL)
    
    # Scroll to top to find search
    driver.execute_script("window.scrollTo(0, 0);")
    
    # Use products page search functionality
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    
    # Find and use search on products page
    search_input = products_page.wait.until(
        EC.visibility_of_element_located((By.ID, "search_product"))
    )
    search_input.send_keys("zzzznonexistent999")
    
    search_button = products_page.find((By.ID, "submit_search"))
    search_button.click()
    
    # Verify no results message is shown
    assert products_page.search_results_are_shown(), "Search results title should be displayed"
    
    # Check either no products are shown OR a "no results" message appears
    has_products = products_page.products_are_visible()
    has_no_results_msg = products_page.no_results_message_shown()
    
    assert not has_products or has_no_results_msg, "Should show no products or a 'no results' message"

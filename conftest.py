
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    """Creates a fresh browser instance for each test function."""
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(10)  # Add implicit wait for stability

    yield browser

    # Cleanup: Clear cookies and quit browser
    try:
        browser.delete_all_cookies()
    except Exception:
        pass
    browser.quit()

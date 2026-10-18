
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """Add custom command line option for headless mode."""
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run Chrome in headless mode (no visible window)",
    )


@pytest.fixture(scope="function")
def driver(request):
    """Creates a fresh browser instance for each test function."""
    # Get headless option from command line
    headless = request.config.getoption("--headless")

    # Configure Chrome options
    options = Options()
    options.page_load_strategy = "eager"  # Don't wait for all resources

    if headless:
        options.add_argument("--headless=new")  # Use new headless mode
        options.add_argument("--window-size=1920,1080")  # Set viewport size
        options.add_argument("--disable-gpu")  # Recommended for Windows
        options.add_argument("--no-sandbox")  # For CI environments
        options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    # Create browser instance
    browser = webdriver.Chrome(options=options)

    # Maximize window only in non-headless mode
    if not headless:
        browser.maximize_window()

    # Set timeouts
    browser.implicitly_wait(10)  # Implicit wait for element finding
    browser.set_page_load_timeout(30)  # Page load timeout
    browser.set_script_timeout(30)  # JavaScript execution timeout

    yield browser

    # Cleanup: Clear cookies and quit browser
    try:
        browser.delete_all_cookies()
    except Exception:
        pass
    browser.quit()

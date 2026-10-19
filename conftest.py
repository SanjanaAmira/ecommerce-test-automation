
import os
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
    browser.set_page_load_timeout(30)  # Page load timeout
    browser.set_script_timeout(30)  # JavaScript execution timeout

    yield browser

    # Cleanup: quit browser
    browser.quit()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshot on test failure.
    Runs after each test phase (setup, call, teardown).
    """
    outcome = yield
    report = outcome.get_result()
    
    # Only capture screenshot if the test call phase failed
    if report.when == "call" and report.failed:
        browser = item.funcargs.get("driver")
        if browser:
            # Create screenshots directory if it doesn't exist
            os.makedirs("screenshots", exist_ok=True)
            
            # Save screenshot with test name
            screenshot_path = f"screenshots/{item.name}.png"
            browser.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved: {screenshot_path}")

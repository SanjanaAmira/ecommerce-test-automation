
import pytest
from selenium.webdriver.common.by import By

from config import BASE_URL, TEST_EMAIL, TEST_PASSWORD
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.open_login_page(BASE_URL)
    return page


def test_login_with_incorrect_password(login_page):
    login_page.login(TEST_EMAIL, "WrongPassword123!")
    message = login_page.get_error_message()
    assert "incorrect" in message.lower()


def test_login_with_unregistered_email(login_page):
    login_page.login(
        "unregistered_test_987@example.com",
        "AnyPassword123!"
    )
    message = login_page.get_error_message()
    assert "incorrect" in message.lower()


def test_login_with_empty_fields(login_page, driver):
    login_page.login("", "")
    email = driver.find_element(*LoginPage.EMAIL_INPUT)
    assert driver.execute_script(
        "return arguments[0].validity.valueMissing", email
    )


def test_login_with_invalid_email_format(login_page, driver):
    login_page.login("testuser.com", "AnyPassword123!")
    email = driver.find_element(*LoginPage.EMAIL_INPUT)
    assert driver.execute_script(
        "return arguments[0].validity.typeMismatch", email
    )


def test_login_with_valid_credentials(login_page):
    if not TEST_EMAIL or not TEST_PASSWORD:
        pytest.skip("Set TEST_EMAIL and TEST_PASSWORD in .env first")

    login_page.login(TEST_EMAIL, TEST_PASSWORD)
    assert HomePage(login_page.driver).is_logged_in()

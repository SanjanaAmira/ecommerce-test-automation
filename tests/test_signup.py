
import pytest
import time

from config import BASE_URL
from pages.signup_page import SignupPage


# TC_SIGNUP_01
def test_signup_new_user_then_delete(driver):
    """Verify that a new user can sign up and then delete their account."""
    signup_page = SignupPage(driver)
    signup_page.open_signup_page(BASE_URL)
    
    # Generate unique email using timestamp
    timestamp = str(int(time.time()))
    test_email = f"testuser_{timestamp}@example.com"
    test_name = f"Test User {timestamp}"
    
    # Step 1: Enter signup credentials
    signup_page.enter_signup_credentials(test_name, test_email)
    
    # Step 2: Fill account information
    signup_page.fill_account_information(
        password="TestPass123!",
        day="15",
        month="5",
        year="1990"
    )
    
    # Step 3: Fill address information
    signup_page.fill_address_information(
        first_name="Test",
        last_name="User",
        company="Test Company",
        address="123 Test Street",
        address2="Apt 4B",
        city="Test City",
        state="Test State",
        zipcode="12345",
        mobile="1234567890"
    )
    
    # Step 4: Create account
    signup_page.submit_account_creation()
    
    # Verify account created
    assert signup_page.is_account_created(), "Account creation confirmation should be shown"
    
    # Step 5: Continue to logged in state
    signup_page.click_continue()
    
    # Step 6: Delete account
    signup_page.delete_account()
    
    # Verify account deleted
    assert signup_page.is_account_deleted(), "Account deletion confirmation should be shown"


# TC_SIGNUP_02
def test_signup_with_existing_email(driver):
    """Verify that signing up with an existing email shows an error."""
    from config import TEST_EMAIL
    
    if not TEST_EMAIL:
        pytest.skip("TEST_EMAIL must be set in .env file")
    
    signup_page = SignupPage(driver)
    signup_page.open_signup_page(BASE_URL)
    
    # Try to sign up with existing email
    signup_page.enter_signup_credentials("Existing User", TEST_EMAIL)
    
    # Verify error message is shown
    assert signup_page.is_signup_error_shown(), "Error message should be displayed"
    error_message = signup_page.get_signup_error()
    assert "already exist" in error_message.lower(), f"Expected 'already exist' in error, got: {error_message}"

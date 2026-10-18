
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class SignupPage(BasePage):
    # Signup form (first step)
    SIGNUP_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    
    # Error message for existing email
    SIGNUP_ERROR = (By.XPATH, "//p[contains(text(), 'Email Address already exist')]")
    
    # Account information form (second step)
    ACCOUNT_INFO_TITLE = (By.XPATH, "//h2[contains(., 'Enter Account Information')]")
    GENDER_MR = (By.ID, "id_gender1")
    GENDER_MRS = (By.ID, "id_gender2")
    PASSWORD_INPUT = (By.ID, "password")
    DAY_SELECT = (By.ID, "days")
    MONTH_SELECT = (By.ID, "months")
    YEAR_SELECT = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    OPTIN_CHECKBOX = (By.ID, "optin")
    
    # Address information
    FIRST_NAME_INPUT = (By.ID, "first_name")
    LAST_NAME_INPUT = (By.ID, "last_name")
    COMPANY_INPUT = (By.ID, "company")
    ADDRESS1_INPUT = (By.ID, "address1")
    ADDRESS2_INPUT = (By.ID, "address2")
    COUNTRY_SELECT = (By.ID, "country")
    STATE_INPUT = (By.ID, "state")
    CITY_INPUT = (By.ID, "city")
    ZIPCODE_INPUT = (By.ID, "zipcode")
    MOBILE_INPUT = (By.ID, "mobile_number")
    
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    
    # Account created confirmation
    ACCOUNT_CREATED_TITLE = (By.CSS_SELECTOR, "h2[data-qa='account-created']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
    
    # Delete account
    DELETE_ACCOUNT_LINK = (By.XPATH, "//a[contains(@href, '/delete_account')]")
    ACCOUNT_DELETED_TITLE = (By.CSS_SELECTOR, "h2[data-qa='account-deleted']")

    def open_signup_page(self, base_url):
        """Navigate to signup/login page."""
        self.open(f"{base_url}/login")

    def enter_signup_credentials(self, name, email):
        """Enter name and email in the initial signup form."""
        self.type(self.SIGNUP_NAME_INPUT, name)
        self.type(self.SIGNUP_EMAIL_INPUT, email)
        self.click(self.SIGNUP_BUTTON)

    def is_signup_error_shown(self):
        """Check if 'Email already exists' error is displayed."""
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.SIGNUP_ERROR)
            ).is_displayed()
        except Exception:
            return False

    def get_signup_error(self):
        """Get the signup error message text."""
        return self.get_text(self.SIGNUP_ERROR)

    def fill_account_information(self, password, day="1", month="1", year="1990"):
        """Fill the account information form."""
        # Wait for account info form to load
        self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_INFO_TITLE)
        )
        
        # Select gender
        self.click(self.GENDER_MR)
        
        # Enter password
        self.type(self.PASSWORD_INPUT, password)
        
        # Select date of birth
        from selenium.webdriver.support.ui import Select
        Select(self.find(self.DAY_SELECT)).select_by_value(day)
        Select(self.find(self.MONTH_SELECT)).select_by_value(month)
        Select(self.find(self.YEAR_SELECT)).select_by_value(year)

    def fill_address_information(self, first_name, last_name, address, 
                                 city, state, zipcode, mobile, 
                                 company="", address2="", country="United States"):
        """Fill the address information form."""
        self.type(self.FIRST_NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        
        if company:
            self.type(self.COMPANY_INPUT, company)
        
        self.type(self.ADDRESS1_INPUT, address)
        
        if address2:
            self.type(self.ADDRESS2_INPUT, address2)
        
        # Select country
        from selenium.webdriver.support.ui import Select
        Select(self.find(self.COUNTRY_SELECT)).select_by_visible_text(country)
        
        self.type(self.STATE_INPUT, state)
        self.type(self.CITY_INPUT, city)
        self.type(self.ZIPCODE_INPUT, zipcode)
        self.type(self.MOBILE_INPUT, mobile)

    def submit_account_creation(self):
        """Click the Create Account button."""
        self.click(self.CREATE_ACCOUNT_BUTTON)

    def is_account_created(self):
        """Check if account was created successfully."""
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.ACCOUNT_CREATED_TITLE)
            )
            return True
        except Exception:
            return False

    def click_continue(self):
        """Click the Continue button after account creation."""
        self.click(self.CONTINUE_BUTTON)

    def delete_account(self):
        """Click the Delete Account link."""
        self.click(self.DELETE_ACCOUNT_LINK)

    def is_account_deleted(self):
        """Check if account was deleted successfully."""
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.ACCOUNT_DELETED_TITLE)
            )
            return True
        except Exception:
            return False

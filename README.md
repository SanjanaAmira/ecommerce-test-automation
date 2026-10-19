# E-Commerce Test Automation Framework

Selenium + Python test automation suite for [automationexercise.com](https://automationexercise.com), demonstrating end-to-end testing of an e-commerce application with Page Object Model design.

---

## 📊 Project Stats

| Metric | Value |
|--------|-------|
| **Automated Tests** | 18 (100% passing) |
| **Test Cases Documented** | 29 (CSV format) |
| **Page Objects** | 7 |
| **Test Coverage** | Login, Signup, Products, Cart, Search, Checkout, Logout |
| **Execution Time (Headless)** | 4:18 average (258 seconds) |
| **Execution Time (Normal)** | Not yet measured (single run) |
| **Stability** | 100% (3 consecutive green runs, 54/54 test executions passed) |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- Chrome browser
- Git

### Installation

```bash
# Clone repository
git clone https://github.com/SanjanaAmira/ecommerce-test-automation.git
cd ecommerce-test-automation

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Configure credentials (REQUIRED for some tests)
# Register a throwaway account at https://automationexercise.com/login
# Then create .env file:
copy .env.example .env  # Windows
cp .env.example .env    # Mac/Linux

# Edit .env with your test account credentials
```

**Note**: Login, logout, signup-with-existing-email, and logged-in checkout tests require valid credentials in `.env`.

### Run Tests

```bash
# Run all tests (with browser visible)
pytest -v

# Run all tests (headless mode - faster, no browser window)
pytest -v --headless

# Run specific test file
pytest tests/test_login.py -v

# Run specific test
pytest tests/test_login.py::test_login_with_valid_credentials -v

# View HTML report (automatically generated)
# Open: reports/report.html in browser
```

---

## 📁 Project Structure

```
ecommerce-test-automation/
├── pages/                      # Page Object Model
│   ├── base_page.py           # Base class with common methods
│   ├── home_page.py           # Home page actions
│   ├── login_page.py          # Login functionality
│   ├── signup_page.py         # Signup and account management
│   ├── products_page.py       # Product browsing and search
│   ├── cart_page.py           # Shopping cart operations
│   └── checkout_page.py       # Checkout flow
│
├── tests/                      # Test modules (18 tests)
│   ├── test_login.py          # Login tests (5)
│   ├── test_signup.py         # Signup tests (2)
│   ├── test_products_cart.py  # Product display and cart (4)
│   ├── test_extended_cart.py  # Advanced cart operations (2)
│   ├── test_search.py         # Product search (2)
│   └── test_logout_checkout.py # Logout and checkout (3)
│
├── reports/                    # HTML test reports (gitignored)
├── screenshots/                # Failure screenshots (gitignored)
├── docs/                       # Additional documentation
│   ├── ROOT_CAUSE_ANALYSIS.md # Root cause analysis of fixed flaky tests
│   └── STABILITY_RUNS.md      # Raw output from stability test runs
├── conftest.py                # Pytest fixtures and hooks
├── config.py                  # Configuration management
├── pytest.ini                 # Pytest configuration
├── .env.example               # Environment variable template
├── test_cases.csv             # 29 documented test cases
├── check_csv.py               # CSV validation script
└── requirements.txt           # Python dependencies
```

---

## ✨ Key Features

### Page Object Model
- Clean separation between test logic and page interactions
- Reusable page components
- Easy maintenance and scalability
- No locators in test files

### Pytest Framework
- Fixtures for browser setup (fresh instance per test)
- Clear test organization
- HTML reporting with pytest-html

### HTML Reporting
- Automatic report generation with pytest-html
- Self-contained (includes CSS)
- Test duration, pass/fail status, metadata

### Screenshot on Failure
- Auto-captures screenshot when test fails
- Saves to `screenshots/<test_name>.png`
- Shows page state at moment of failure

### Headless Mode
- Run without visible browser window
- Ideal for CI/CD pipelines

### Explicit Waits
- Uses explicit waits for reliable synchronization
- No implicit wait (avoids conflicts)
- Predictable, targeted waiting strategies

### Stability
- Fixed 2 flaky tests by addressing synchronization issues
- 100% pass rate over 3 consecutive runs (54/54 test executions)
- Uses explicit waits only (no implicit wait conflicts)
- Modal-based navigation for natural synchronization points

---

## 📝 Test Cases

### Documented: 29 Test Cases
- **Automated**: 18 (62%)
- **Manual/Planned**: 11 (38%)

### Coverage by Feature

| Feature | Automated | Manual | Total |
|---------|-----------|--------|-------|
| Login | 6 | 1 | 7 |
| Signup | 2 | 1 | 3 |
| Products | 4 | 2 | 6 |
| Cart | 4 | 2 | 6 |
| Checkout | 2 | 1 | 3 |
| UI/Navigation | 0 | 4 | 4 |

### Automation Selection

**Automated**:
- Core user journeys (login, signup, cart, checkout)
- Repetitive validation (product display, search)
- Regression-prone areas (cart operations)

**Manual**:
- Security tests requiring network inspection
- Visual verification better suited for human review
- Edge cases needing investigation first

All test cases in `test_cases.csv` include Test Case ID, detailed steps, specific expected results, and automation rationale.

**Validate**: `python check_csv.py`

---

## 🧪 Test Examples

### Login with Incorrect Password (TC_LOGIN_01)
```python
def test_login_with_incorrect_password(login_page):
    login_page.login(TEST_EMAIL, "WrongPassword123!")
    message = login_page.get_error_message()
    assert "incorrect" in message.lower()
```

### Add Product to Cart (TC_CART_01)
```python
def test_added_product_appears_in_cart(driver):
    products_page = ProductsPage(driver)
    products_page.open_products_page(BASE_URL)
    
    expected_name = products_page.get_first_product_name()
    products_page.add_first_product_to_cart(navigate_to_cart=True)
    
    cart_page = CartPage(driver)
    assert cart_page.cart_has_items()
    assert cart_page.get_product_name() == expected_name
```

### Search for Product (TC_PROD_01)
```python
def test_search_existing_product(driver):
    products_page = ProductsPage(driver)
    products_page.open_products_page(BASE_URL)
    
    products_page.search_for("Top")
    
    assert products_page.search_results_are_shown()
    assert products_page.products_are_visible()
```

---

## ⏱️ Performance

### Execution Time

**Automated Suite (18 tests)**:
- **Headless Mode Average**: 258 seconds (4:18)
  - Run 1: 285s
  - Run 2: 231s
- **Normal Mode**: Not yet measured after removing implicit wait
- **Per Test Average**: 14.3 seconds (headless)

**Manual Execution** (estimated):
- Estimated: 45-54 minutes (18 tests × 2.5-3 min each)
- Includes: open browser, navigate, enter data, verify, document
- **Note**: Actual manual measurement not yet performed

**Time Comparison**:
- Automation: 4:18 unattended (tester can work on other tasks)
- Manual: 45+ minutes active tester time (estimated)
- **Note**: Times measured after removing implicit wait that conflicted with explicit waits
- **Recommendation**: Measure actual manual time with stopwatch for accurate comparison

---

## 🔧 Configuration

### Browser Settings
- Chrome with maximize window (normal mode)
- Explicit waits (10 second default)
- Page load timeout: 30 seconds
- Fresh browser instance per test

### Environment Variables
`.env` file (not tracked in Git):
```ini
TEST_EMAIL=your_test_account@example.com
TEST_PASSWORD=your_password
```

### Pytest Configuration
`pytest.ini`:
```ini
addopts = -v --html=reports/report.html --self-contained-html
```

---

## 🐛 Debugging

### Screenshots on Failure
When test fails: `screenshots/<test_name>.png`

### View HTML Report
```bash
start reports/report.html      # Windows
open reports/report.html       # Mac
xdg-open reports/report.html   # Linux
```

### Run with Output
```bash
pytest -v -s  # Shows print statements
```

### Run Last Failed
```bash
pytest --lf -v
```

---

## 🔬 Flaky Tests Fixed

**Issue**: 2 tests failed intermittently due to synchronization problems

**test_remove_item_from_cart**:
- Symptom: "Cart should have items before removal"
- Cause: Race condition - cart page loaded before product fully added
- Fix: Use modal navigation (`navigate_to_cart=True`) which waits for product to be added

**test_checkout_logged_out_requires_login**:
- Symptom: Timeout finding login element
- Cause: Insufficient wait time, only checked modal
- Fix: Check URL redirect first, then fallback to modal with explicit wait

**Result**: 100% stability - 54/54 test executions passed across 3 runs

**Details**: See `docs/ROOT_CAUSE_ANALYSIS.md` for complete technical analysis

---

## 📚 Technologies

- Python 3.13
- Selenium 4
- Pytest
- pytest-html
- python-dotenv
- Chrome WebDriver

---

## 🎯 Future Enhancements

- GitHub Actions CI/CD pipeline
- API testing with Postman/Requests
- Additional cart scenarios (quantity update)
- Payment flow with test card details
- Cross-browser testing
- Parallel test execution

---

## 📖 Additional Documentation

- `docs/ROOT_CAUSE_ANALYSIS.md` - Detailed analysis of fixed flaky tests
- `docs/STABILITY_RUNS.md` - Raw output from stability test runs with timing data
- `test_cases.csv` - 29 documented test cases with automation rationale

---

## 👤 Author

**Sanjana Amira**
- GitHub: [@SanjanaAmira](https://github.com/SanjanaAmira)

---

**Last Updated**: October 2026

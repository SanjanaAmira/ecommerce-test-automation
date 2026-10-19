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
| **Execution Time (Headless)** | 3:54 average (234 seconds) |
| **Execution Time (Normal)** | 4:36 (276 seconds) |
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
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Configure credentials (optional for most tests)
cp .env.example .env
# Edit .env with valid test account credentials
```

### Run Tests

```bash
# Run all tests (with browser visible)
pytest -v

# Run all tests (headless mode - faster)
pytest -v --headless

# Run specific test file
pytest tests/test_login.py -v

# Run specific test
pytest tests/test_login.py::test_login_with_valid_credentials -v

# Generate HTML report (automatic with current config)
pytest
# Report saved to: reports/report.html
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
├── tests/                      # Test modules
│   ├── test_login.py          # Login tests (5)
│   ├── test_signup.py         # Signup tests (2)
│   ├── test_products_cart.py  # Product display and cart (4)
│   ├── test_extended_cart.py  # Advanced cart operations (2)
│   ├── test_search.py         # Product search (2)
│   └── test_logout_checkout.py # Logout and checkout (3)
│
├── reports/                    # HTML test reports (gitignored)
├── screenshots/                # Failure screenshots (gitignored)
├── conftest.py                # Pytest fixtures and hooks
├── config.py                  # Configuration management
├── test_cases.csv             # 29 documented test cases
├── check_csv.py               # CSV validation script
└── requirements.txt           # Python dependencies
```

---

## ✨ Key Features

### 1. Page Object Model
- Clean separation between test logic and page interactions
- Reusable page components
- Easy maintenance and scalability

### 2. Pytest Framework
- Fixtures for browser setup
- Parameterized tests
- Clear test organization
- Parallel execution support

### 3. HTML Reporting
- Automatic HTML report generation with pytest-html
- Self-contained reports (includes CSS)
- Test duration, pass/fail status, metadata

### 4. Screenshot on Failure
- Automatically captures screenshot when test fails
- Saves to `screenshots/<test_name>.png`
- Browser still open at moment of failure (captured before teardown)

### 5. Headless Mode
- Run tests without visible browser window
- 15% faster execution (3:54 vs 4:36)
- Ideal for CI/CD pipelines

### 6. Test Isolation
- Each test gets fresh browser instance
- Cookie cleanup between tests
- No test interdependencies

---

## 📝 Test Cases

### Documented Test Cases: 29
- **Automated**: 18 (62%)
- **Manual/Planned**: 11 (38%)

### Test Coverage by Feature

| Feature | Automated | Manual | Total |
|---------|-----------|--------|-------|
| Login | 6 | 1 | 7 |
| Signup | 2 | 1 | 3 |
| Products | 4 | 2 | 6 |
| Cart | 4 | 2 | 6 |
| Checkout | 2 | 1 | 3 |
| UI/Navigation | 0 | 4 | 4 |

### Automation Selection Criteria

**Automated (Yes)**:
- Core user journeys (login, signup, cart, checkout)
- Repetitive validation (product display, search)
- Regression-prone areas (cart operations)
- Data-driven scenarios (multiple login variations)

**Manual (No)**:
- Security tests requiring network inspection
- Visual/UI verification better for human review
- Edge cases needing investigation before automation
- Features requiring additional implementation effort

All test cases documented in `test_cases.csv` with:
- Test Case ID (mapped to automated tests via comments)
- Detailed test steps
- Expected results (specific, measurable)
- Actual results (only for executed tests)
- Automation decision with rationale

Validate CSV: `python check_csv.py`

---

## ⏱️ Performance

### Execution Time Metrics

**Automated Suite (18 tests)**:
- **Headless Mode Average**: 234 seconds (3:54)
  - Run 1: 224.13s
  - Run 2: 236.35s
  - Run 3: 242.81s
- **Normal Mode**: 276 seconds (4:36)
- **Per Test Average**: 13 seconds (headless)

**Manual Execution** (estimated):
- Based on 2-3 minutes per test case for manual execution (open browser, navigate, enter data, verify, document)
- Estimated: 18 tests × 2.5 minutes = 45 minutes minimum
- Actual measurement: **Not yet performed**

**Time Comparison**:
- Automation: 3:54 (unattended - tester can do other work)
- Manual (estimated): 45+ minutes (active tester time)
- **Note**: Automated time is unattended execution. During this time, tester can review results, work on other tasks, or run multiple test suites in parallel.

**Recommendation**: Perform actual manual timing measurement by executing same 18 test cases manually with stopwatch for accurate comparison.

---

## 🔧 Configuration

### Environment Variables (.env)
```ini
TEST_EMAIL=your_test_account@example.com
TEST_PASSWORD=your_password
```

**Note**: `.env` is gitignored. Never commit real credentials. Use `.env.example` as template.

### Pytest Configuration (pytest.ini)
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
addopts = -v --html=reports/report.html --self-contained-html
```

### Browser Options (conftest.py)
- Default: Chrome with maximize window
- Headless: `--headless` flag
- Timeouts: 30s page load, 10s implicit wait
- Cookie cleanup between tests

---

## 🧪 Test Examples

### Login with Incorrect Password (TC_LOGIN_01)
```python
def test_login_with_incorrect_password(login_page):
    """Verify error message for incorrect password."""
    login_page.login(TEST_EMAIL, "WrongPassword123!")
    message = login_page.get_error_message()
    assert "incorrect" in message.lower()
```

### Add Product to Cart (TC_CART_01)
```python
def test_added_product_appears_in_cart(driver):
    """Verify product added to cart appears with correct name."""
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
    """Verify searching for existing product shows results."""
    products_page = ProductsPage(driver)
    products_page.open_products_page(BASE_URL)
    
    # Perform search
    search_input = products_page.wait.until(
        EC.visibility_of_element_located((By.ID, "search_product"))
    )
    search_input.send_keys("Top")
    search_button = products_page.find((By.ID, "submit_search"))
    search_button.click()
    
    assert products_page.search_results_are_shown()
    assert products_page.products_are_visible()
```

---

## 🐛 Debugging

### Screenshots on Failure
When a test fails, screenshot automatically saved:
```
screenshots/test_name.png
```

### View HTML Report
```bash
# After test run, open in browser
start reports/report.html  # Windows
open reports/report.html   # Mac
xdg-open reports/report.html  # Linux
```

### Run with Verbose Output
```bash
pytest -v -s  # -s shows print statements
```

### Run Last Failed Tests
```bash
pytest --lf -v
```

---

## 🔬 Testing Philosophy

### Stability Over Speed
- Fixed 2 flaky tests by addressing root causes (synchronization issues)
- Proper wait strategies (explicit waits, modal handling)
- 100% pass rate across 3 consecutive runs (54/54 test executions)

### Quality Test Cases
- Specific, measurable expected results
- Only record actual results after genuine execution
- No sensitive data in version control
- Clear automation vs manual decisions with rationale

### Maintainable Code
- Page Object Model for separation of concerns
- DRY principle (Don't Repeat Yourself)
- Clear naming conventions
- Comprehensive documentation

---

## 📚 Technologies Used

- **Python 3.13** - Programming language
- **Selenium 4** - Browser automation
- **Pytest** - Test framework
- **pytest-html** - HTML reporting
- **python-dotenv** - Environment variable management
- **Chrome WebDriver** - Browser driver

---

## 🎯 Future Enhancements

- [ ] GitHub Actions CI/CD pipeline
- [ ] API testing with Postman/Requests
- [ ] Additional cart scenarios (quantity update, multiple items)
- [ ] Payment flow testing (with test card details)
- [ ] Cross-browser testing (Firefox, Edge)
- [ ] Parallel test execution
- [ ] Test data management strategy
- [ ] Visual regression testing
- [ ] Performance testing metrics

---

## 📖 Documentation

- `TEST_SUMMARY.md` - Complete test suite overview
- `STABILITY_REPORT.md` - Stability testing results
- `STABILITY_RUNS.md` - Raw output from test runs
- `CSV_IMPROVEMENTS.md` - Test case quality improvements
- `TEST_COMMANDS.md` - Quick reference for test commands

---

## 🤝 Contributing

This is a portfolio project demonstrating test automation skills. Suggestions for improvements are welcome!

---

## 📄 License

This project is for educational and portfolio purposes.

---

## 👤 Author

**Sanjana Amira**
- GitHub: [@SanjanaAmira](https://github.com/SanjanaAmira)
- Project: [ecommerce-test-automation](https://github.com/SanjanaAmira/ecommerce-test-automation)

---

## 🎓 Skills Demonstrated

- Test automation framework design
- Page Object Model implementation
- Selenium WebDriver proficiency
- Python programming
- Pytest framework expertise
- Test case documentation
- Debugging and troubleshooting
- CI/CD readiness
- Git version control
- Test stability and reliability
- Professional documentation

---

**Last Updated**: December 2024

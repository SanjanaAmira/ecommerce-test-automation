# Test Execution Commands

## Running Tests

### Normal Mode (with visible browser)
```bash
# Run all tests
.\venv\Scripts\python.exe -m pytest -v

# Run specific test file
.\venv\Scripts\python.exe -m pytest tests/test_login.py -v

# Run specific test function
.\venv\Scripts\python.exe -m pytest tests/test_login.py::test_login_with_valid_credentials -v
```

### Headless Mode (no browser window - faster)
```bash
# Run all tests in headless mode
.\venv\Scripts\python.exe -m pytest -v --headless

# Run specific test file in headless mode
.\venv\Scripts\python.exe -m pytest tests/test_products_cart.py -v --headless

# Run specific test in headless mode
.\venv\Scripts\python.exe -m pytest tests/test_login.py::test_login_with_valid_credentials -v --headless
```

### Additional Options
```bash
# Show print statements and more details
.\venv\Scripts\python.exe -m pytest -v -s

# Stop at first failure
.\venv\Scripts\python.exe -m pytest -v -x

# Run last failed tests only
.\venv\Scripts\python.exe -m pytest --lf -v

# Run with coverage report
.\venv\Scripts\python.exe -m pytest --cov=pages --cov=tests -v
```

## Performance Comparison

- **Normal Mode**: ~5-6 minutes for 9 tests
- **Headless Mode**: ~1-2 minutes for 9 tests (4x faster!)

## When to Use Each Mode

### Normal Mode
- During test development and debugging
- When you want to see browser interactions
- When investigating test failures

### Headless Mode
- For CI/CD pipelines (GitHub Actions)
- For quick test runs
- For running tests on servers without displays
- When you want faster execution

## Test Organization

```
tests/
├── test_login.py           # 5 login tests
└── test_products_cart.py   # 4 product/cart tests

Total: 9 tests
```

## Environment Setup

Make sure `.env` file has valid credentials:
```env
TEST_EMAIL=your_email@example.com
TEST_PASSWORD=your_password
```

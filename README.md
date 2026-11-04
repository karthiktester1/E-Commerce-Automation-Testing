# E-Commerce Web Application Automation Testing

## Project Overview
Automated testing of the SauceDemo e-commerce web application using Python, Selenium WebDriver, and Pytest.

## Technologies Used
- Python
- Selenium WebDriver
- Pytest
- pytest-html
- Google Chrome

## Test Scenarios
1. Valid Login
2. Invalid Login
3. Product Page Verification
4. Product Details Verification
5. Logout
6. Add Product to Cart
7. Cart Page Verification
8. Checkout Page Verification
9. Checkout Information
10. Place Order

## Project Structure
```text
Selenium_Python 2/
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_logout.py
│   ├── test_cart.py
│   └── test_order.py
├── reports.html
├── requirements.txt
└── README.md
```

## How to Run Tests
```bash
pip install -r requirements.txt
pytest -v tests
```

## Generate HTML Report
```bash
pytest -v tests --html=reports.html --self-contained-html
```

## Application Under Test
https://www.saucedemo.com/

## Project Status
10 automation test cases implemented and passed in the current test run.
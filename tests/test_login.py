from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# Test 1: Open website
def test_open_website():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    assert driver.title == "Swag Labs"
    driver.quit()


# Test 2: Valid login
def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url
    driver.quit()


# Test 3: Invalid login
def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    assert "saucedemo.com" in driver.current_url

    driver.quit()

# Test 4 Logout Test
def test_logout():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "react-burger-menu-btn").click()

    time.sleep(3)
    
    driver.find_element(By.ID, "logout_sidebar_link").click()   

    assert "saucedemo.com" in driver.current_url
    driver.quit()
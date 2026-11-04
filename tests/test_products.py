from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_product_page():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    title = driver.find_element(By.CLASS_NAME, "title").text

    assert title == "Products"

    driver.quit()

#Test 5 Product details verification

def test_product_details():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    assert len(products) > 0
    assert len(prices) > 0
    time.sleep(3)
    driver.quit()
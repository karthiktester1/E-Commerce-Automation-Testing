from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#test 6
def test_add_to_cart():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(3)

    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

    assert cart_count == "1"

    driver.quit()

#Test 7 Verify Cart Page

def test_cart_page():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    product = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    assert product == "Sauce Labs Backpack"

    driver.quit()
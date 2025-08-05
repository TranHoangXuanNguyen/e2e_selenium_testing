import time
from selenium import webdriver
from pageObject.LoginPageModel import LoginPageModel

def test_login_with_validAccout():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPageModel(driver)
    login_page.login("standard_user", "secret_sauce")
    time.sleep(2)
    assert "inventory" in driver.current_url.lower()
    driver.quit()

def test_login_with_invalidAccout():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPageModel(driver)
    login_page.login("standard_usersss", "secret_sauce")
    time.sleep(2)
    assert "inventory" not in driver.current_url.lower()
    driver.quit()

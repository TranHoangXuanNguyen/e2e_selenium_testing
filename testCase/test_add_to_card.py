import time
from selenium import webdriver
from pageObject.LoginPageModel import LoginPageModel
from pageObject.ProductPageModel import ProductPageModel
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from component.HeaderComponent import HeaderComponent
def test_add_product_to_cart():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPageModel(driver)
    login_page.login("standard_user", "secret_sauce")
    WebDriverWait(driver, 5).until(
      EC.url_contains("inventory")
    )
    header_component = HeaderComponent(driver)
    product_page = ProductPageModel(driver)
    total_item = header_component.get_total_item()
    product_page.add_product1()
    total_item_after = header_component.get_total_item()
    assert total_item + 1 == total_item_after
    driver.quit()
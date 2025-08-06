from selenium.webdriver.common.by import By
from component import HeaderComponent

class ProductPageModel:
    def __init__(self, driver):
        self.driver = driver
        self.add_product1_btn = (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
        self.add_product2_btn = (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-bike-light"]')
        self.add_product3_btn = (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
        self.remove_product1_btn = (By.CSS_SELECTOR, '[data-test="remove-sauce-labs-backpack"]')
        self.remove_product2_btn = (By.CSS_SELECTOR, '[data-test="remove-sauce-labs-bike-light"]')
        self.remove_product3_btn = (By.CSS_SELECTOR, '[data-test="remove-sauce-labs-bolt-t-shirt"]')

    def add_product1(self):
        self.driver.find_element(*self.add_product1_btn).click()

    def add_product2(self):
        self.driver.find_element(*self.add_product2_btn).click()
        
    def add_product3(self):
        self.driver.find_element(*self.add_product3_btn).click()

    def remove_product1(self):
        self.driver.find_element(*self.remove_product1_btn).click()

    def remove_product2(self):
        self.driver.find_element(*self.remove_product2_btn).click()
        
    def remove_product3(self):
        self.driver.find_element(*self.remove_product3_btn).click()


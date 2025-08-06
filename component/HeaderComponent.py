from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class HeaderComponent:
    def __init__(self, driver):
        self.driver = driver
        self.menu_button = (By.CSS_SELECTOR,'[data-test="shopping-cart-link"]')
        self.cart_button = (By.ID, "login-button")
        self.cart_bagde = (By.CSS_SELECTOR,'[data-test="shopping-cart-badge"]')

    def click_menu_btn(self):
        self.driver.find_element(*self.menu_button).click()

    def click_cart_btn(self):
        self.driver.find_element(*self.cart_button).click()

    def get_total_item(self):
        try:
            return int(self.driver.find_element(*self.cart_bagde).text)
        except NoSuchElementException:
            return 0

    

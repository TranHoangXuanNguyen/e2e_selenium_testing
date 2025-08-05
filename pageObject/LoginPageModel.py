from selenium.webdriver.common.by import By

class LoginPageModel:
    def __init__(self, driver):
        self.driver = driver
        #username_input = co 2 gia tri
        self.username_input = (By.CSS_SELECTOR, '[data-test="username"]')
        self.password_input = (By.CSS_SELECTOR, '[data-test="password"]')
        self.login_button = (By.ID, "login-button")

    def enter_username(self, username):
        #find_element(by,value) can truyen vao 2 tham so
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

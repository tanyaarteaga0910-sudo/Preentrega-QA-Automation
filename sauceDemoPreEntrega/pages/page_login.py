from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.username_input = (By.NAME, "user-name")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.NAME, "login-button")
        self.object = (By.CLASS_NAME, "shopping_cart_link")
        self.error_message = (By.XPATH, "//h3[contains(text(),'Epic sadface: Sorry, this user has been locked out.')]")

    def load(self):
        self.driver.get(self.url)

    def object_wait(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.object))

    def login(self,username,password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def objeto(self):
        return self.driver.find_element(*self.object)

    def user_logged_out(self):
        return self.driver.find_element(*self.error_message).text
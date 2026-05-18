from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.ID, "first-name")
        self.lastname_input = (By.ID, "last-name")
        self.zip_input = (By.ID, "postal-code")
        self.error_box = (By.XPATH, "//h3[@data-test='error']")
        self.subtotal_label = (By.CLASS_NAME, "summary_subtotal_label")
        self.total_monto = (By.CLASS_NAME, "summary_total_label")

    def llenar_campos(self,nombre, apellido, zip):
        self.driver.find_element(*self.name_input).send_keys(nombre)
        self.driver.find_element(*self.lastname_input).send_keys(apellido)
        self.driver.find_element(*self.zip_input).send_keys(zip)

    def clic_continuar(self):
        self.driver.find_element(By.NAME, "continue").click()

    def checkout_overview(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Checkout: Overview']")

    def devolver_mensaje_error(self):
        return self.driver.find_element(*self.error_box).text

    def devolver_subtotal(self):
        return self.driver.find_element(*self.subtotal_label).text

    def devolver_total(self):
        return self.driver.find_element(*self.total_monto).text
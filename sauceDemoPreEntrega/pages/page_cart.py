from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self,driver):
        self.driver = driver
        self.remove_jacket_button = (By.ID, "remove-sauce-labs-fleece-jacket")
        self.continue_shopping_button = (By.ID, "continue-shopping")
        self.checkout_button = (By.ID, "checkout")
        self.firstname_input = (By.ID, "first-name")

    def obtener_productos(self):
        productos = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_name']")
        return [p.text for p in productos]

    #voy a definir aqui el botón porque supuestamente es mejor no definir tantos objetos en el init, sobre
    # todo si no son importantes
    def esperar_boton_checkout(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.checkout_button))

    def remover_producto(self):
        self.driver.find_element(*self.remove_jacket_button).click()

    def continue_shopping(self):
        self.driver.find_element(*self.continue_shopping_button).click()

    def checkout_clic(self):
        self.driver.find_element(*self.checkout_button).click()

    def firstname_wait(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.firstname_input))

    def input_primernombre(self):
        return self.driver.find_element(*self.firstname_input)




from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.backpack_add = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        self.jacket_add = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
        self.shirt_add = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
        self.burger_menu = (By.XPATH, "//button[@id='react-burger-menu-btn']")
        self.remove_button = (By.NAME, "remove-sauce-labs-backpack")
        self.cart_number = (By.XPATH, "//span[@class='shopping_cart_badge']")
        self.backpack_remove = (By.XPATH, "//button[@id='remove-sauce-labs-backpack']")
        self.jacket_remove = (By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']")
        self.carrito = (By.XPATH, "//a[@class='shopping_cart_link']")
        self.titulo_productos = (By.XPATH, "//span[@class='title']")

    def button_wait(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.jacket_add))

    def remove_wait(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.remove_button))

    def seleccion_dos_productos(self):
        self.driver.find_element(*self.jacket_add).click()
        self.driver.find_element(*self.backpack_add).click()

    def seleccion_tres_productos(self):
        self.driver.find_element(*self.jacket_add).click()
        self.driver.find_element(*self.backpack_add).click()
        self.driver.find_element(*self.shirt_add).click()

    def remover_dos_productos(self):
        self.driver.find_element(*self.backpack_remove).click()
        self.driver.find_element(*self.jacket_remove).click()

    def texto_boton(self, nombre_producto):
        producto = self.driver.find_element(By.XPATH, f"//div[text()='{nombre_producto}']/ancestor::div[@class='inventory_item']")
        boton = producto.find_element(By.TAG_NAME, "button")
        return boton.text

    def contador_carrito(self):
        contador = self.driver.find_element(*self.cart_number)
        return contador.text

    def carrito_clic(self):
        self.driver.find_element(*self.carrito).click()

    def titulo_pagina(self):
        return self.driver.find_element(*self.titulo_productos)


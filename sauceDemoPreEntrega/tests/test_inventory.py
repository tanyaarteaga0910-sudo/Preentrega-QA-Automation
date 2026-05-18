from pages.page_inventory import InventoryPage
from pages.page_login import HomePage
import time

def test_add_button(driver):

    login = HomePage(driver)
    login.load()
    login.login("standard_user","secret_sauce")

    add_products = InventoryPage(driver)
    add_products.button_wait()
    add_products.seleccion_dos_productos()
    time.sleep(2)

    assert add_products.texto_boton("Sauce Labs Fleece Jacket") == "Remove"
    assert add_products.texto_boton("Sauce Labs Backpack") == "Remove"

def test_cart_count(driver):

    login = HomePage(driver)
    login.load()
    login.login("standard_user","secret_sauce")

    add_products = InventoryPage(driver)
    add_products.button_wait()
    add_products.seleccion_tres_productos()
    cuenta = add_products.contador_carrito()

    assert cuenta == "3"

def remover_productos(driver):
    login = HomePage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    add_products = InventoryPage(driver)
    add_products.button_wait()
    add_products.seleccion_tres_productos()
    cuenta = add_products.contador_carrito()

    assert cuenta == "3"

    add_products.remover_dos_productos()

    assert cuenta == "1"

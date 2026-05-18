import pytest
import time
from pages.page_inventory import InventoryPage
from pages.page_login import HomePage
from pages.page_checkout import CheckoutPage
from pages.page_cart import CartPage
from utils.wait_function import wait_visible_element

def test_correct_checkout(driver):
    login = HomePage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    add_products = InventoryPage(driver)
    add_products.button_wait()
    add_products.seleccion_dos_productos()
    add_products.carrito_clic()

    cart = CartPage(driver)
    cart.esperar_boton_checkout()
    cart.checkout_clic()
    resumen = CheckoutPage(driver)
    locator = resumen.name_input
    wait_visible_element(driver,locator,10)

    resumen.llenar_campos("Tanya", "arteaga", "1234")
    resumen.clic_continuar()
    titulo_resumen = resumen.checkout_overview()
    assert titulo_resumen.is_displayed()

@pytest.mark.parametrize("nombre, apellido, postal, mensaje", [
    ("", "Arteaga", "1234", "Error: First Name is required"),
    ("Tanya", "", "1234", "Error: Last Name is required"),
    ("Tanya", "Arteaga", "", "Error: Postal Code is required"),
    ("","","","Error: First Name is required")
])
def test_invalid_checkout(driver, nombre, apellido, postal, mensaje):

    login = HomePage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    add_products = InventoryPage(driver)
    add_products.button_wait()
    add_products.seleccion_dos_productos()
    add_products.carrito_clic()

    cart = CartPage(driver)
    cart.esperar_boton_checkout()
    cart.checkout_clic()
    resumen = CheckoutPage(driver)
    locator = resumen.name_input
    wait_visible_element(driver,locator,10)

    resumen.llenar_campos(nombre, apellido, postal)
    resumen.clic_continuar()
    time.sleep(2)
    mensaje_error = resumen.devolver_mensaje_error()
    assert mensaje_error == mensaje

def test_validar_montos_resumen(driver):
    login = HomePage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    add_products = InventoryPage(driver)
    add_products.button_wait()
    add_products.seleccion_dos_productos()
    add_products.carrito_clic()

    cart = CartPage(driver)
    cart.esperar_boton_checkout()
    cart.checkout_clic()
    resumen = CheckoutPage(driver)
    locator = resumen.name_input
    wait_visible_element(driver,locator,10)

    resumen.llenar_campos("Tanya", "arteaga", "1234")
    resumen.clic_continuar()
    total_label = resumen.subtotal_label
    wait_visible_element(driver, total_label,10)
    subtotal = resumen.devolver_subtotal()
    total = resumen.devolver_total()

    assert "79.98" in subtotal
    assert "86.38" in total

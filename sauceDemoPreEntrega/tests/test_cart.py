from pages.page_inventory import InventoryPage
from pages.page_login import HomePage
from pages.page_cart import CartPage

def test_verificar_productos(driver):

    login = HomePage(driver)
    login.load()
    login.login("standard_user","secret_sauce")

    add_products = InventoryPage(driver)
    add_products.button_wait()
    add_products.seleccion_dos_productos()
    add_products.carrito_clic()

    cart = CartPage(driver)
    cart.esperar_boton_checkout()
    productos = cart.obtener_productos()

    assert "Sauce Labs Backpack" in productos
    assert "Sauce Labs Fleece Jacket" in productos

def test_boton_remover(driver):
    login = HomePage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    add_products = InventoryPage(driver)
    add_products.button_wait()
    add_products.seleccion_dos_productos()
    add_products.carrito_clic()

    cart = CartPage(driver)
    cart.esperar_boton_checkout()
    cart.remover_producto()
    productos = cart.obtener_productos()

    assert "Sauce Labs Fleece Jacket" not in productos

def test_continuar_comprando(driver):
    login = HomePage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    add_products = InventoryPage(driver)
    add_products.button_wait()
    add_products.seleccion_dos_productos()
    add_products.carrito_clic()

    cart = CartPage(driver)
    cart.esperar_boton_checkout()
    cart.continue_shopping()
    titulo = add_products.titulo_pagina()

    assert titulo.is_displayed()
    assert titulo.text == "Products"

def test_checkout(driver):
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
    cart.firstname_wait()
    pagar = cart.input_primernombre()

    assert pagar.is_displayed()


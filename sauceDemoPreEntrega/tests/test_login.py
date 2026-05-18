import pytest
from pages import page_login
from pages.page_login import HomePage


def test_login(driver, usuarios_login):
    username = usuarios_login["username"]
    password = usuarios_login["password"]
    expected = usuarios_login["resultado"]

    login = HomePage(driver)

    login.load()
    login.login(username,password)

    if expected == "exitoso":
        objeto = login.objeto()
        login.object_wait()
        assert objeto.is_displayed()
    else:
        assert "Epic sadface: Sorry, this user has been locked out." in login.user_logged_out()
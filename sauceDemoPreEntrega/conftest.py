import pytest
from selenium import webdriver
from utils.leer_archivo import read_data

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # <--- modo incógnito
    options.add_argument('--disable-password-manager-reauthentication')
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(params=read_data('usuarios.json'))
def usuarios_login(request):
    return request.param
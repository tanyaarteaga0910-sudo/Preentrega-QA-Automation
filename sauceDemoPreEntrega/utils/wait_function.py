from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def wait_visible_element(driver, locator, tiempo=10):
    return WebDriverWait(driver, tiempo).until(expected_conditions.visibility_of_element_located(locator))
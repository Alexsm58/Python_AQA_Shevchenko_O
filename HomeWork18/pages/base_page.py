from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from HomeWork18.core import BaseLocators

class BasePage:
    def __init__(self, driver, wait_time=10):
        self.driver = driver
        self.web_driver_wait = WebDriverWait(driver, wait_time)
        self.locators = BaseLocators()
        self.cookies = Cookies(driver)
        self.local_storage = LocalStorage(driver)

    def wait_until_element_presence(self, locator: tuple[str, str]):
        return self.web_driver_wait.until(EC.presence_of_element_located(locator))

    def click_on_element(self, locator):
        element = self.wait_until_element_presence(locator)
        element.click()

    def click_header_discount(self):
        self.click_on_element(self.locators.locator_discount)

    def click_delivery(self):
        self.click_on_element((self.locators.locator_delivery))

    def return_card_items_counter(self):
        cart_counter = self.wait_until_element_presence(self.locators.locator_card_items_counter)
        return int(cart_counter.text)


class Cookies:
    def __init__(self, driver):
        self.driver = driver

    def get_cookie(self, name):
        return self.driver.get_cookie(name)

    def add_cookie(self, cookie_dict):
        self.driver.add_cookie(cookie_dict)


class LocalStorage:
    def __init__(self, driver):
        self.driver = driver

    def set_local_storage_item(self, key, value):
        script = f'window.localStorage.setItem("{key}", "{value}");'
        self.driver.execute_script(script)

    def get_local_storage_item(self, key):
        script = f'return window.localStorage.getItem("{key}");'
        return self.driver.execute_script(script)
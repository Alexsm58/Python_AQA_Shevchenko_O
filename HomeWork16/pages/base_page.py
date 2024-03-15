from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, wait_time=10):
        self.driver = driver
        self.web_driver_wait = WebDriverWait(driver, wait_time)
        self.locator_discount = ('xpath', '//nav[@class="header__menu"]/a[@href="/page/diskontna-programa"]')

    def wait_until_element_presence(self, locator: tuple[str, str]):
        return self.web_driver_wait.until(EC.presence_of_element_located(locator))

    def click_on_element(self, locator):
        element = self.wait_until_element_presence(locator)
        element.click()

    def click_header_discount(self):
        self.click_on_element(self.locator_discount)
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, wait_time=10):
        self.driver = driver
        self.web_driver_wait = WebDriverWait(driver, wait_time)
        self.locator_discount = ('xpath', '//li[@class="light-color active-hover "]/a[@href="/products_action/"]')
        self.locator_delivery = ('xpath', '//div[@class="top-menu-left tablet-grid-50 mobile-grid-50"]//a[@href="delivery/m14/"]')
        self.locator_card_items_counter = ('xpath', '//div[@class="header-cart"]//span[@class="cart-top-total-count"]')

    def wait_until_element_presence(self, locator: tuple[str, str]):
        return self.web_driver_wait.until(EC.presence_of_element_located(locator))

    def click_on_element(self, locator):
        element = self.wait_until_element_presence(locator)
        element.click()

    def click_header_discount(self):
        self.click_on_element(self.locator_discount)

    def click_delivery(self):
        self.click_on_element((self.locator_delivery))

    def return_card_items_counter(self):
        cart_counter = self.wait_until_element_presence(self.locator_card_items_counter)
        return int(cart_counter.text)
from HomeWork18.pages.base_page import BasePage
from HomeWork18.core import ProductLocators

class Product(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProductLocators()

    def click_buy(self):
        self.click_on_element(self.locators.locator_button_buy)

    def click_card_glue(self):
        self.click_on_element(self.locators.locator_glue)

    def click_checkbox_glue(self):
        self.click_on_element(self.locators.locator_checkbox_glue)

    def click_footer_button(self):
        self.click_on_element(self.locators.locator_footer_button)

    def click_items_stories(self):
        self.click_on_element(self.locators.locator_items_stories)
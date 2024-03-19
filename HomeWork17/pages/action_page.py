from HomeWork17.pages.base_page import BasePage
from HomeWork17.core import ActionLocators

class ActionPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ActionLocators()

    def click_action_product(self):
        self.click_on_element(self.locators.locator_action_product)

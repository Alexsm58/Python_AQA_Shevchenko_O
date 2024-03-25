from HomeWork18.pages.base_page import BasePage
from HomeWork18.pages.category_page import CategoryPage
from HomeWork18.pages.product_page import Product
from HomeWork18.core import DashboardLocators

class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = DashboardLocators()

    def click_sale(self):
        self.click_on_element(self.locators.locator_sale)
        return CategoryPage(self.driver)

    def click_novosti(self):
        self.click_on_element(self.locators.locator_novosti)
        return CategoryPage(self.driver)

    def click_pagination(self):
        self.click_on_element(self.locators.locator_pagination)

    def click_new_arrivals(self):
        self.click_on_element(self.locators.locator_new_arrivals)
        return Product(self.driver)

    def click_stories(self):
        self.click_on_element(self.locators.locator_stories)
        return Product(self.driver)
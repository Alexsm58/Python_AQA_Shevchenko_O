from HomeWork18.pages.base_page import BasePage, Cookies, LocalStorage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from HomeWork18.pages.product_page import Product
from HomeWork18.core import CategoryLocators

class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CategoryLocators()

    def click_first_product(self):
        self.click_on_element(self.locators.locator_first_product)

    def click_checkbox(self):
        self.click_on_element(self.locators.locator_checkbox_masternet)

    def click_item_novosti(self):
        self.click_on_element(self.locators.locator_item_novosti)

    def click_previous_news(self):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(500,500).perform()
        self.click_on_element(self.locators.locator_previous_news)

    def click_gips_pagination(self):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(500,500).perform()
        self.click_on_element(self.locators.locator_gips_pagination)

    def click_to_profil(self):
        self.click_on_element(self.locators.locator_profil)

    def click_go_to_gips_titan(self):
        self.click_on_element(self.locators.locator_gips_titan)

    def click_sort_product(self):
        self.click_on_element(self.locators.locator_sort_product)
        return LocalStorage, Cookies

    def click_cart_acvapanel(self):
        self.click_on_element(self.locators.locator_cart_acvapanel)
        return Cookies, LocalStorage

    def click_tab_glue(self):
        self.click_on_element(self.locators.locator_glue)
        return Product(self.driver)

    def click_plas_shtukaturki(self, category, items_list):
        category_object = self.click_on_element(category)
        for item in items_list:
            item_object = self.wait_until_element_presence(item)
            assert item_object.is_displayed()
        return category_object
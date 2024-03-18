from HomeWork17.pages.base_page import BasePage
from HomeWork17.pages.category_page import CategoryPage
from HomeWork17.pages.product_page import Product

class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_sale = ('xpath', '//div[@class="left-menu-item"]/a[@data-category="51"][contains(text(), " Гипсокартонные системы")]')
        self.locator_novosti = ('xpath', '//nav[@class="main-menu grid-container"]//li[@class="light-color active-hover "]/a[@href="/s5/"]')

    def click_sale(self):
        self.click_on_element(self.locator_sale)
        return CategoryPage(self.driver)

    def click_novosti(self):
        self.click_on_element(self.locator_novosti)

    def click_pagination(self):
        self.click_on_element(self.locator_pagination)
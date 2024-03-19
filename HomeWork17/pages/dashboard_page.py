from HomeWork17.pages.base_page import BasePage
from HomeWork17.pages.category_page import CategoryPage
from HomeWork17.pages.product_page import Product

class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_sale = ('xpath', '//div[@class="left-menu-item"]/a[@data-category="51"][contains(text(), " Гипсокартонные системы")]')
        self.locator_novosti = ('xpath', '//nav[@class="main-menu grid-container"]//li[@class="light-color active-hover "]/a[@href="/s5/"]')
        self.locator_pagination = ('xpath', '//div[@class="pager align-center"]//a[@href="/gipsokartonnye-sistemy/t51/?page=3"]')
        self.locator_new_arrivals = ('xpath', '//nav[@class="main-menu grid-container"]//li[@class="light-color active-hover "]/a[@href="/products_novelty/"]')
        self.locator_stories = ('xpath', '//nav[@class="main-menu grid-container"]//li[@class="active-color dark-hover "]/a[@href="/stati/s6/"]')

    def click_sale(self):
        self.click_on_element(self.locator_sale)
        return CategoryPage(self.driver)

    def click_novosti(self):
        self.click_on_element(self.locator_novosti)
        return CategoryPage(self.driver)

    def click_pagination(self):
        self.click_on_element(self.locator_pagination)

    def click_new_arrivals(self):
        self.click_on_element(self.locator_new_arrivals)
        return Product(self.driver)

    def click_stories(self):
        self.click_on_element(self.locator_stories)
        return Product(self.driver)
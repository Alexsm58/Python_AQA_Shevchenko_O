from HomeWork16.pages.base_page import BasePage

class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_sale = ('xpath', '//a[@class="categories__item"][@href="category/koti/goduvannia-petslike/sale-gift"]')

    def click_sale(self):
        self.click_on_element(self.locffator_sale)
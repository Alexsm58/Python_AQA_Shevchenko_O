from HomeWork17.pages.base_page import BasePage

class Product(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_button_buy = ('xpath', '//div[@class="button-dual light-color transition-all"]/button[@type="submit"]')
        self.locator_button_one_click = ('xpath', '//div[@class="button-dual light-color transition-all one-click"]/button[@class="button-dual-left  active-gradient  button "]')

    def click_buy(self):
        self.click_on_element(self.locator_button_buy)
        return Product(self.driver)

    def click_buy_one_click(self):
        self.click_on_element(self.locator_button_one_click)
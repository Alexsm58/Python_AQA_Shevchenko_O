from HomeWorkPractice16.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_sale = ('xpath', '//a[@class="categories__item"][@href="category/koti/goduvannia-petslike/sale-gift"]')

    def click_sale(self):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(500,500).perform()
        self.click_on_element(self.locator_sale)

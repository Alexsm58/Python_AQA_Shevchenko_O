from HomeWork17.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_first_product = ('xpath', '//div[@class="product-title subheader-font"]//strong[contains(text(), "Грунтовка под штукатурку ( Краска - грунт ) Эко 10л")]')
        self.locator_checkbox_masternet = ('xpath', '//div[@class="well well-table light-bg"]//a[@href="masternet/b45/"]')
        self.locator_item_novosti = ('xpath', '//div/h2[@class="blog-list-title"]/a[@href="pochemu-stoit-perekryt-kryshu-garazha-evroruberoidom/i197/"]')
        self.locator_previous_news = ('xpath', '//div[@class="prevPost"]')
        self.locator_gips_pagination = ('xpath', '//div[@class="pager align-center"]/a[@href="/gipsokartonnye-sistemy/t51/?page=3"]')


    def click_first_product(self):
        self.click_on_element(self.locator_first_product)

    def click_checkbox(self):
        self.click_on_element(self.locator_checkbox_masternet)

    def click_item_novosti(self):
        self.click_on_element(self.locator_item_novosti)

    def click_previous_news(self):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(500,500).perform()
        self.click_on_element(self.locator_previous_news)

    def click_gips_pagination(self):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(500,500).perform()
        self.click_on_element(self.locator_gips_pagination)
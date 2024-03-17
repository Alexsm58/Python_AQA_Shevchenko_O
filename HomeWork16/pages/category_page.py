from HomeWork16.pages.base_page import BasePage

class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_first_product = ('xpath', '//div[@class="product-title subheader-font"]//strong[contains(text(), "Грунтовка под штукатурку ( Краска - грунт ) Эко 10л")]')
        self.locator_checkbox_masternet = ('xpath', '//div[@class="well well-table light-bg"]//a[@href="masternet/b45/"]')
        self.locator_item_novosti = ('xpath', '//div/h2[@class="blog-list-title"]/a[@href="pochemu-stoit-perekryt-kryshu-garazha-evroruberoidom/i197/"]')
        self.locator_previous_news = ('xpath', '//div[@class="prevPost"]')


    def click_first_product(self):
        self.click_on_element(self.locator_first_product)

    def click_checkbox(self):
        self.click_on_element(self.locator_checkbox_masternet)

    def click_item_novosti(self):
        self.click_on_element(self.locator_item_novosti)

    def click_previous_news(self):
        self.click_on_element(self.click_previous_news)
from HomeWork17.pages.base_page import BasePage

class Product(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_button_buy = ('xpath', '//div[@class="button-dual light-color transition-all"]/button[@type="submit"]')
        self.locator_glue = ('xpath', '//div[@class="product-box light-bg"]/a[@class="product-img"]//img[@title="Клей строительный универсальный Eco 604 (жидкие гвозди) 440 г TYTAN"]')
        self.locator_checkbox_glue = ('xpath', '//div[@class="well well-table light-bg"]//a[@href="dlya-montazha/tytan/t71-b36/"]')
        self.locator_footer_button = ('xpath', '//div[@class="grid-33 tablet-grid-33"]//a[@href="/opt/m15/"]')
        self.locator_items_stories = ('xpath', '//div[@class="blog-list-details grid-100 tablet-grid-100"]/h2[@class="blog-list-title"]/a[@href="gde-kupit-penoplast-v-dnepre/i194/"]')

    def click_buy(self):
        self.click_on_element(self.locator_button_buy)

    def click_card_glue(self):
        self.click_on_element(self.locator_glue)

    def click_checkbox_glue(self):
        self.click_on_element(self.locator_checkbox_glue)

    def click_footer_button(self):
        self.click_on_element(self.locator_footer_button)

    def click_items_stories(self):
        self.click_on_element(self.locator_items_stories)
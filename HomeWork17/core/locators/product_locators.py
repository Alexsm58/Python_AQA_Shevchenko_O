from .base_locators import BaseLocators

class ProductLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self.locator_button_buy = ('xpath', '//div[@class="button-dual light-color transition-all"]/button[@type="submit"]')
        self.locator_glue = ('xpath', '//div[@class="product-box light-bg"]/a[@class="product-img"]//img[@title="Клей строительный универсальный Eco 604 (жидкие гвозди) 440 г TYTAN"]')
        self.locator_checkbox_glue = ('xpath', '//div[@class="well well-table light-bg"]//a[@href="dlya-montazha/tytan/t71-b36/"]')
        self.locator_footer_button = ('xpath', '//div[@class="grid-33 tablet-grid-33"]//a[@href="/opt/m15/"]')
        self.locator_items_stories = ('xpath', '//div[@class="blog-list-details grid-100 tablet-grid-100"]/h2[@class="blog-list-title"]/a[@href="gde-kupit-penoplast-v-dnepre/i194/"]')
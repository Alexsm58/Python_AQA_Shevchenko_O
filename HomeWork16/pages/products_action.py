from HomeWork16.pages.base_page import BasePage

class ProductsAction(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_action_product = ('xpath', '//div[@class="product-box light-bg"]/a[@href="gipsokarton-knauf-vlagostojkij-9-5-mm-1-2-mx2-5-m/p2706/"]')

    def click_action_product(self):
        self.click_on_element(self.locator_action_product)


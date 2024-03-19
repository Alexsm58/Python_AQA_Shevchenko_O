from .base_locators import BaseLocators

class ActionLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self.locator_action_product = ('xpath', '//div[@class="product-box light-bg"]/a[@href="gipsokarton-knauf-vlagostojkij-9-5-mm-1-2-mx2-5-m/p2706/"]')

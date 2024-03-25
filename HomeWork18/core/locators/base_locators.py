
class BaseLocators:
    def __init__(self):
        self.locator_discount = ('xpath', '//li[@class="light-color active-hover "]/a[@href="/products_action/"]')
        self.locator_delivery = ('xpath', '//div[@class="top-menu-left tablet-grid-50 mobile-grid-50"]//a[@href="delivery/m14/"]')
        self.locator_card_items_counter = ('xpath', '//div[@class="header-cart"]//span[@class="cart-top-total-count"]')
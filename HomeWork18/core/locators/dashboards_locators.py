from .base_locators import BaseLocators

class DashboardLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self.locator_sale = ('xpath', '//div[@class="left-menu-item"]/a[@data-category="51"][contains(text(), " Гипсокартонные системы")]')
        self.locator_novosti = ('xpath', '//nav[@class="main-menu grid-container"]//li[@class="light-color active-hover "]/a[@href="/s5/"]')
        self.locator_pagination = ('xpath', '//div[@class="pager align-center"]//a[@href="/gipsokartonnye-sistemy/t51/?page=3"]')
        self.locator_new_arrivals = ('xpath', '//nav[@class="main-menu grid-container"]//li[@class="light-color active-hover "]/a[@href="/products_novelty/"]')
        self.locator_stories = ('xpath', '//nav[@class="main-menu grid-container"]//li[@class="active-color dark-hover "]/a[@href="/stati/s6/"]')
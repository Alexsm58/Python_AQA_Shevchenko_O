from HomeWork16.pages.base_page import BasePage

class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_sale = ('xpath', '//div[@class="left-menu-item"]/a[@data-category="51"][contains(text(), " Гипсокартонные системы")]')
        self.locator_novosti = ('xpath', '//nav[@class="main-menu grid-container"]//li[@class="light-color active-hover "]/a[@href="/s5/"]')
        self.locator_pagination = ('xpath', '//div[@class="pager align-center"]//a[@href="/gipsokartonnye-sistemy/t51/?page=3"]')

    def click_sale(self):
        self.click_on_element(self.locator_sale)

    def click_novosti(self):
        self.click_on_element(self.locator_novosti)

    def click_pagination(self):
        self.click_on_element(self.locator_pagination)
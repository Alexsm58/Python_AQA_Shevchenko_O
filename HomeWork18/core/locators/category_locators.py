from .base_locators import BaseLocators

class CategoryLocators(BaseLocators):
    locator_shtukaturki = ('xpath', '//div[@class="left-menu-item"]/a[@href="shtukaturki-dekorativnye-dlya-vnutrenney-i-naruzhnoy-otdelki/t46/"]')
    locator_dlya_montazha = ('xpath', '//div[@class="left-menu-item"]//a[@href="dlya-montazha/t71/"]')
    def __init__(self):
        super().__init__()
        self.locator_first_product = ('xpath', '//div[@class="product-title subheader-font"]//strong[contains(text(), "Грунтовка под штукатурку ( Краска - грунт ) Эко 10л")]')
        self.locator_checkbox_masternet = ('xpath', '//div[@class="well well-table light-bg"]//a[@href="masternet/b45/"]')
        self.locator_item_novosti = ('xpath', '//div/h2[@class="blog-list-title"]/a[@href="pochemu-stoit-perekryt-kryshu-garazha-evroruberoidom/i197/"]')
        self.locator_previous_news = ('xpath', '//div[@class="prevPost"]')
        self.locator_gips_pagination = ('xpath', '//div[@class="pager align-center"]/a[@href="/gipsokartonnye-sistemy/t51/?page=3"]')
        self.locator_profil = ('xpath', '//div[@class="product-box light-bg"]/a//img[@title="Профиль UA 50 4 метра"]')
        self.locator_gips_titan = ('xpath', '//div[@class="product-box light-bg"]/a//img[@title="Гипсокартон КНАУФ Диамант (Титан) 12,5 mm 1,2 m*2,5 m "]')
        self.locator_sort_product = ('xpath', '//div[@class="product-sort hide-on-mobile"]/a[@href="/gipsokartonnye-sistemy/t51/?sort=name+asc"]')
        self.locator_cart_acvapanel = ('xpath', '//div/a[@href="akvapanel-cementnaya-plita-naruzhnaya-aquapanel-cement-board-outdoor-knauf/p2617/"]/span[1]')
        self.locator_glue = ('xpath', '//div[@class="left-menu-item"]/a[@href="dlya-montazha/t71/"]')


def test_bypass_to_gips(dashboard, driver):
    sale_category = dashboard.click_sale()
    sale_category.click_to_profil()
    assert sale_category.driver.title == 'Профиль UA 50 4 метра'

def test_go_to_gips_titan(dashboard, driver):
    sale_category_gips = dashboard.click_sale()
    sale_category_gips.click_go_to_gips_titan()
    assert sale_category_gips.driver.title == 'Гипсокартон КНАУФ Диамант (Титан) 12,5 mm 1,2 m*2,5 m'

def test_buy_gips_titan(buy_gips, driver):
    buy_gips.click_buy()
    assert buy_gips.return_card_items_counter() == 1

def test_go_to_primer(dashboard, driver):
    buy_primer = dashboard.click_novosti()
    buy_primer.click_header_discount()
    buy_primer.click_checkbox()
    assert buy_primer.driver.title == 'Купить Masternet в Днепре (Днепропетровске)'

def test_go_to_pagination(dashboard, driver):
    go_to_pagination = dashboard.click_sale()
    go_to_pagination.click_gips_pagination()
    assert  go_to_pagination.driver.title == 'Купить гипсокартонные системы в Днепре по лучшей цене с доставкой. Страница 3.'

def test_sort(dashboard, driver):
    sort = dashboard.click_sale()
    sort.click_sort_product()
    sort.click_cart_acvapanel()
    assert sort.driver.title == 'Аквапанель цементная плита наружная ( Aquapanel Cement Board Outdoor ) Knauf'

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

def test_buy_gips_titan(buy_gips, driver):
    buy_gips.click_buy()
    assert buy_gips.return_card_items_counter() == 1
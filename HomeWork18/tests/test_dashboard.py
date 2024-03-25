
def test_go_to_sale(dashboard, driver):
    dashboard.click_sale()
    assert dashboard.driver.title == 'Купить гипсокартонные системы в Днепре по лучшей цене с доставкой'

def test_to_discount(dashboard, driver):
    dashboard.click_header_discount()
    assert dashboard.driver.title == 'Акционные товары'

def test_go_to_novosti(dashboard, driver):
    dashboard.click_novosti()
    assert dashboard.driver.title == 'Новости'

def test_click_serch(dashboard, driver):
    dashboard.click_delivery()
    assert dashboard.driver.title == 'О доставке'

def test_click_pagination(pagination, driver):
    pagination.click_pagination()
    assert pagination.driver.title == 'Купить гипсокартонные системы в Днепре по лучшей цене с доставкой. Страница 3.'

def test_click_check(dashboard, driver):    #added test with Page Factory pattern
    category = dashboard.click_sale()
    category.click_gips_pagination()
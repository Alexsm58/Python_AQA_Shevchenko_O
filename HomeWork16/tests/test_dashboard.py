
def test_go_to_sale(dashboard, driver):
    dashboard.click_sale()
    assert dashboard.driver.title == 'Купить гипсокартонные системы в Днепре по лучшей цене с доставкой'

def test_to_discount(dashboard, driver):
    dashboard.click_header_discount()
    assert dashboard.driver.title == 'Акционные товары'

def test_go_to_novosti(dashboard, driver):
    dashboard.click_novosti()
    assert dashboard.driver.title == 'Новости'
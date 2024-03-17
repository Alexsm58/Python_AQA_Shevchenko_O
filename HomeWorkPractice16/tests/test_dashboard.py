
def test_go_to_sale(dashboard, driver):
    dashboard.click_sale()
    assert dashboard.driver.title == 'Харчування - Акційні пропозиції З подарунком | інтернет-магазин petslike.ua'

def test_to_discount(dashboard, driver):
    dashboard.click_header_discount()
    assert dashboard.driver.title == 'Дисконтна програма | зоомагазин, Україна'

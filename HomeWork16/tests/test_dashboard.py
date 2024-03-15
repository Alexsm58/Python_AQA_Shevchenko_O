
def test_go_to_sale(dashboard, driver):
    dashboard.click_sale()
    assert dashboard.driver.title == 'Зоомагазин Petslike.net - Интернет-Магазин Зоотоваров Для Ваших Питомцев'
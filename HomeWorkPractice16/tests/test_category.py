

def test_first_product(sale, driver):
    sale.click_first_product()
    assert sale.driver.title == 'Optimeal Adult Cat Sterilised Turkey with oat - сухий корм з індичкою та вівсом для стерилізованих кішок та кастрованих котів Купити в Україні - Зоомагазин Petslike.net'
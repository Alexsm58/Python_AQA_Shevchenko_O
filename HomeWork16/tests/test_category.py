
def test_first_product(sale, driver):
    sale.click_first_product()
    assert sale.driver.title == 'Грунтовка под штукатурку ( Краска - грунт ) Эко 10л'

def test_click_checkbox_manufacturer(sale, driver):
    sale.click_checkbox()
    assert sale.driver.title == 'Купить Masternet в Днепре (Днепропетровске)'

def test_click_item_novosti(novosti, driver):
    novosti.click_item_novosti()
    assert novosti.driver.title == 'Почему стоит перекрыть крышу гаража еврорубероидом?'

def test_click_previous_news(previous_news, driver):
    previous_news.click_previous_news()
    assert previous_news.driver.title == 'Шумоизоляция потолка пенопластом'
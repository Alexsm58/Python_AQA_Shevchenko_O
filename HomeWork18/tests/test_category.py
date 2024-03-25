import pytest
from HomeWork18.core.locators.category_locators import CategoryLocators
from HomeWork18.core.data_sample import shtukaturki_list, dlya_montazha_list

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

@pytest.mark.parametrize('category,list_of_subcategories',[(CategoryLocators.locator_shtukaturki,shtukaturki_list),(CategoryLocators.locator_dlya_montazha,dlya_montazha_list)])
def test_click_locator_shtukaturki(sale,category,list_of_subcategories):
    sale.click_plas_shtukaturki(category, list_of_subcategories)

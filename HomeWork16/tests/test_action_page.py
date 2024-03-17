
def test_products_action(products_action, driver):
    products_action.click_action_product()
    assert products_action.driver.title == 'Гипсокартон Knauf влагостойкий - потолочный 9,5 mm 1,2 m*2,5 m'
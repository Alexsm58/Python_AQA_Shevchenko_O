import pytest
from selenium.webdriver import Chrome
from HomeWork18.pages.base_page import BasePage
from HomeWork18.pages.dashboard_page import Dashboard
from HomeWork18.pages.category_page import CategoryPage
from HomeWork18.pages.action_page import ActionPage
from HomeWork18.pages.product_page import Product

@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def dashboard(driver):
    driver.get('https://uks.dp.ua/')
    print(f"Cookies: {driver.get_cookies()}")
    print(f"Cookies: {driver.add_cookie({'name': 'my_cookie', 'value': 'good luck'})}")
    print(f"Single cookies: {driver.get_cookie('my_cookie')}")
    driver.add_cookie({'name': 'tree', 'value': 'apples'})
    driver.get_cookie('tree')
    driver.execute_script('window.localStorage["weather"]="sunny"')
    print(driver.execute_script('return window.localStorage["weather"];'))
    yield Dashboard(driver)

@pytest.fixture
def sale(driver):
    driver.get('https://uks.dp.ua/products_action/')
    yield CategoryPage(driver)

@pytest.fixture
def products_action(driver):
    driver.get('https://uks.dp.ua/products_action/')
    yield ActionPage(driver)

@pytest.fixture
def novosti(driver):
    driver.get('https://uks.dp.ua/novosti/s5/')
    yield CategoryPage(driver)

@pytest.fixture
def previous_news(driver):
    driver.get('https://uks.dp.ua/pochemu-stoit-perekryt-kryshu-garazha-evroruberoidom/i197')
    yield CategoryPage(driver)

@pytest.fixture
def pagination(driver):
    driver.get('https://uks.dp.ua/gipsokartonnye-sistemy/t51/')
    yield Dashboard(driver)

@pytest.fixture
def buy_gips(driver):
    driver.get('https://uks.dp.ua/gipsokarton-knauf-diamant-titan-12-5mm/p4556/')
    print(f"Cookies: {driver.get_cookies()}")
    print(f"Cookies: {driver.add_cookie({'name': 'my_cookie', 'value': 'good luck'})}")
    print(f"Single cookies: {driver.get_cookie('my_cookie')}")
    driver.add_cookie({'name': 'tree', 'value': 'apples'})
    driver.get_cookie('tree')
    driver.execute_script('window.localStorage["weather"]="sunny"')
    print(driver.execute_script('return window.localStorage["weather"];'))
    yield Product(driver)

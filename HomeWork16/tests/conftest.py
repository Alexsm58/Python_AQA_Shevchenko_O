import pytest
from selenium.webdriver import Chrome
from HomeWork16.pages.dashboard_page import Dashboard
from HomeWork16.pages.category_page import CategoryPage
from HomeWork16.pages.products_action import ProductsAction

@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def dashboard(driver):
    driver.get('https://uks.dp.ua/')
    yield Dashboard(driver)

@pytest.fixture
def sale(driver):
    driver.get('https://uks.dp.ua/products_action/')
    yield CategoryPage(driver)

@pytest.fixture
def products_action(driver):
    driver.get('https://uks.dp.ua/products_action/')
    yield ProductsAction(driver)

@pytest.fixture
def novosti(driver):
    driver.get('https://uks.dp.ua/novosti/s5/')
    yield CategoryPage(driver)

@pytest.fixture
def previous_news(driver):
    driver.get('https://uks.dp.ua/pochemu-stoit-perekryt-kryshu-garazha-evroruberoidom/i197')
    yield CategoryPage(driver)
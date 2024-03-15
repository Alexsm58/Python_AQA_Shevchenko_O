import pytest
from selenium.webdriver import Chrome
from HomeWork16.pages.dashboard_page import Dashboard

@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def dashboard(driver):
    driver.get('https://petslike.ua/')
    yield Dashboard(driver)
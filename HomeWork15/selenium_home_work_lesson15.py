from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
def test_click_the_card():
    driver = Chrome()
    driver.get('https://akb-plus.com/ua/')
    search_lokator = '//div/a[contains(text(), "Українська")]'
    search_element = driver.find_element(by=By.XPATH, value=search_lokator)
    search_element.click()
    search_lokator = '//div[@id="search"]/input[@name="search"]'
    search_element = driver.find_element(by=By.XPATH, value=search_lokator)
    search_element.send_keys('акумулятор 90')
    search_element.send_keys(Keys.ENTER)
    time.sleep(10)

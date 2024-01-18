import webdriver # не импортировал webdriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Запуск браузера
driver = webdriver.Chrome()

# Замените "https://example.com" на URL вашего веб-сайта
driver.get('https://pin-up.ua/ru/promo/gamzix-free-spin-days')

# Найти все элементы на странице, содержащие текст латиницей
elements = driver.find_elements_by_xpath("//*[contains(translate(text(), 'абвгдезийклмнопрстуфхэ', 'ABVGDEZIJKLMNOPRSTUFHE'), 'abcdefghijklmnopqrstuvwxyz')]")

# Вывести найденные элементы
for element in elements:
    print(element.text)

# Закрыть браузер
driver.quit()
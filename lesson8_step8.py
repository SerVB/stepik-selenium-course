import os
import math
from selenium import webdriver
import time


try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    el = browser.find_element_by_name("firstname")
    el.send_keys("abc")

    el = browser.find_element_by_name("lastname")
    el.send_keys("def")

    el = browser.find_element_by_name("email")
    el.send_keys("a@example.com")

    el = browser.find_element_by_name("file")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    el.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

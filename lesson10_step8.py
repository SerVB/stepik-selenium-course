import os
import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    browser.find_element_by_id("book").click()

    button = browser.find_element_by_css_selector("#solve")
    browser.execute_script("return arguments[0].scrollIntoView();", button)

    x_element = browser.find_element_by_css_selector("span#input_value")

    WebDriverWait(browser, 1).until(
        EC.visibility_of(x_element)
    )

    time.sleep(0.2)

    x = x_element.text
    y = calc(x)

    print(browser.find_element_by_css_selector("div label span.nowrap").screenshot("tmp.png"))

    print(x, y)

    answer_element = browser.find_element_by_id("answer")
    answer_element.send_keys(y)

    # Отправляем заполненную форму
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(50)
    # закрываем браузер после всех манипуляций
    browser.quit()

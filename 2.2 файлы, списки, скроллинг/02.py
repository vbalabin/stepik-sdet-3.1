import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

"""
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1") # ищем элемент с текстом "Python"
select.select_by_visible_text("Python")
"""
mathfunc = lambda x: f'{math.log(abs(12*math.sin(int(x))))}'

link = "http://suninjuly.github.io/selects1.html"

locators = list()
locators.append
locators.append(r"span#num1")
locators.append(r"span#num2")
locators.append(r"select#dropdown")
#locators.append(r"input#robotsRule")
locators.append(r"button.btn")


try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locators.pop(0))))
    num2 = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locators.pop(0))))
    captcha = int(num1.text) + int(num2.text)

    select = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locators.pop(0))))
    select = Select(select)
    select.select_by_visible_text(str(captcha))

    button = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locators.pop(0))))
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    input()
    # закрываем браузер после всех манипуляций
    browser.quit()

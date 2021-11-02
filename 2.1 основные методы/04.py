import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

mathfunc = lambda x: f'{math.log(abs(12*math.sin(int(x))))}'

link = "http://suninjuly.github.io/math.html"
value1 = r"span#input_value"
value2 = r"input#answer"
value3 = r"input#robotCheckbox"
value4 = r"input#robotsRule"
value5 = r"button.btn"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    element_x = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, value1)))
    captcha = mathfunc(element_x.text)

    input1 = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, value2)))
    input1.send_keys(captcha)

    checkbox1 = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, value3)))
    checkbox1.click()

    radio1 = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, value4)))
    radio1.click()

    button = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, value5)))
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    input()
    # закрываем браузер после всех манипуляций
    browser.quit()
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

mathfunc = lambda x: f'{math.log(abs(12*math.sin(int(x))))}'

link = "http://suninjuly.github.io/get_attribute.html"

locators = list()
locators.append
locators.append(r"img#treasure")
locators.append(r"input#answer")
locators.append(r"input#robotCheckbox")
locators.append(r"input#robotsRule")
locators.append(r"button.btn")


try:
    browser = webdriver.Chrome()
    browser.get(link)

    chest_x = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locators.pop(0))))
    captcha = mathfunc(chest_x.get_attribute("valuex"))

    input1 = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locators.pop(0))))
    input1.send_keys(captcha)

    checkbox1 = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locators.pop(0))))
    checkbox1.click()

    radio1 = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locators.pop(0))))
    radio1.click()

    button = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locators.pop(0))))
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    input()
    # закрываем браузер после всех манипуляций
    browser.quit()
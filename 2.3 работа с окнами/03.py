import time
import math
import subprocess
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

link = "http://suninjuly.github.io/alert_accept.html"

locators = list()
locators.append
locators.append(r"button.btn")
locators.append(r"span#input_value")
locators.append(r"input#answer")
locators.append(r"button.btn")

browser = webdriver.Chrome()
browser.get(link)

try:

    button1 = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locators.pop(0))))
    button1.click()

    alert1 = browser.switch_to.alert
    alert1.accept()

    element = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locators.pop(0))))
    captcha = f'{mathfunc(element.text)}'

    input1 = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locators.pop(0))))
    input1.send_keys(str(captcha))

    button = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locators.pop(0))))
    button.click()

    alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    text = alert.text
    text = text.split(': ')[-1]
    subprocess.run(['clip.exe'], input=text.strip().encode('utf-16'), check=True)

finally:
    input()
    browser.quit()

# атрибут .text
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get( link )

    def calc( x ):
        return str(math.log( abs( 12*math.sin(int( x ) ) ) ) )
    x_element = browser.find_element( By.ID, "input_value" )
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element( By.ID, "answer" ).send_keys( y )
    checbox1 = browser.find_element( By.CSS_SELECTOR, "[type='checkbox']" ).click()
    radio1 = browser.find_element( By.ID, "robotsRule" ).click()
    submit = browser.find_element( By.CSS_SELECTOR, "[type='submit']" ).click()
finally:
    time.sleep(30)
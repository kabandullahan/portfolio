#метод get_attribute
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get( link )

    def calc( x ):
        return str( math.log( abs( 12*math.sin( int( x ) ) ) ) )
    x_element = browser.find_element( By.ID, "treasure" )
    x = x_element.get_attribute( "valuex" )
    y = calc( x )
    input1 = browser.find_element( By.CSS_SELECTOR, "[type='text']" ).send_keys( y )
    checkbox = browser.find_element( By.CSS_SELECTOR, "[type='checkbox']" ).click()
    radio = browser.find_element( By.ID, "robotsRule" ).click()
    button = browser.find_element( By.CSS_SELECTOR, "[type='submit']" ).click()

finally:
    time.sleep( 10 )


#Бронирование жилья при достижении цены $100
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"

    browser = webdriver.Chrome()
    browser.implicitly_wait(50)
    browser.get(link)

    price = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    print(price)
    button = browser.find_element_by_id("book")
    print(button)
    button.click()

    #Решаем задачу
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print("x=" + str(x))
    y = calc(x)
    print("y=" + str(y))

    input_text_field = browser.find_element_by_class_name("form-control")
    input_text_field.send_keys(y)
    print("form-control")
    
    ##button_robots_rule = browser.find_element_by_class_name("btn.btn-primary")
    button = browser.find_element_by_id("solve")
    button.click()
    print("button")

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()






import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = object


def setup():
    global driver

    driver = webdriver.Chrome('c:\\pf\\bin\\chromedriver.exe')  
    # Optional argument, if not specified will search path.
    #driver = webdriver.Chrome()

def after_tests():
    driver.quit()

def test_fields_on_form():
    driver.get('file://C:/work/git/nodejs-sky/selenium-setup/simple_page.html')
    input_field = driver.find_element_by_id("message")
    input_field.send_keys("help me!")
    submitBtn = driver.find_element_by_id("submit-button")
    time.sleep(2) # Let the user actually see something!

    submitBtn.click()
    time.sleep(3)

    alert = Alert(driver)
    alert.accept()
    time.sleep(3)

    driver.close()  # close the browser

    assert True

def test_navigation():
    driver.get('http://www.google.com/')
    time.sleep(5) # Let the user actually see something!

    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5) # Let the user actually see something!

    driver.close()  # close the browser

    after_tests()

    assert True

setup()


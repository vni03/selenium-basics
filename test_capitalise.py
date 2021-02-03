import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains

driver = object
action = object

def setup_module():
    global driver
    global action
    driver = webdriver.Chrome('c:\\pf\\bin\\chromedriver.exe')  
    driver.get('file://C:/work/selenium-basics/practice_page.html')
    action = ActionChains(driver) 

def teardown_module():
    driver.close()
    driver.quit()


def test_do_name_fields_capitalise():
    first_name = driver.find_element_by_id("firstname")
    first_name.send_keys("viktoria")
    last_name = driver.find_element_by_id("lastname")
    action.click(on_element = last_name)
    last_name.send_keys("nikolova")
    action.click(on_element = first_name)
    action.perform()


    time.sleep(3)

    result_firstname = first_name.get_attribute("value")
    expected_firstname = "Viktoria"

    result_lastname = last_name.get_attribute("value")
    expected_lastname = "Nikolova"

    assert expected_firstname == result_firstname
    assert expected_lastname == result_lastname

def test_age_field_empty():
    age = driver.find_element_by_id("age")

    expected_age = "XXX"
    result_age = age.get_attribute("innerHTML")

    assert expected_age == result_age


def test_does_date_field_show_correct_value():
    global driver
    global action

    date_of_birth = driver.find_element_by_id("birthday")
    date_of_birth.send_keys("27/08/1993")

    age = driver.find_element_by_id("age")
    expected_age = "27"
    result_age = age.get_attribute("innerHTML")


    assert expected_age == result_age
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 

driver = object
action = object

# tests are run in the order they are defined, so this test will run first
def test_before():
    global driver
    global action
    driver = webdriver.Chrome('c:\\pf\\bin\\chromedriver.exe')  
    # Optional argument, if not specified will search path.
    #driver = webdriver.Chrome()
    driver.get('file://C:/work/git/nodejs-sky/selenium-basics/practice_page.html')
    # create action chain object 
    action = ActionChains(driver) 

    assert True


def test_do_name_fields_capitalize():
    global driver
    global action

    first_name = driver.find_element_by_id("firstname")
    first_name.send_keys("samuel elijah")
    last_name = driver.find_element_by_id("lastname")

    # click the item 
    action.click(on_element = last_name) 

    last_name.send_keys("wright")
    action.click(on_element = first_name) 
    
    # perform the operation 
    action.perform() 

    expected_result = "Samuel Elijah"
    result = first_name.get_attribute("value")

    assert expected_result == result


def test_does_date_feild_show_correct_value():
    global driver
    global action

    birthday = driver.find_element_by_id("birthday")
    birthday.send_keys("08-05-1965")

    # perform the operation 
    action.perform() 

    expected_result = "55"
    age = driver.find_element_by_id("age")
    result = age.get_attribute("innerText")

    assert expected_result == result


# tests are run in the order they are defined, so this test will run last
def test_after():
    time.sleep(5)

    driver.close()

    assert True

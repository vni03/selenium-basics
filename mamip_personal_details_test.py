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

    assert expected_result == result


def test_does_date_feild_show_correct_value():
    global driver
    global action


    assert expected_result == result


# tests are run in the order they are defined, so this test will run last
def test_after():
    time.sleep(5)

    driver.close()

    assert True

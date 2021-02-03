import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

driver = object
action = object

element_id = object
def find_the_element_by_id(driver):
    element = driver.find_element_by_id("qa")
    if element:
        return element
    else:
        return False

def setup_module():
    global driver
    global action
    driver = webdriver.Chrome('c:\\pf\\bin\\chromedriver.exe')  
    driver.get('file://C:/work/selenium-basics/practice_page.html')
    action = ActionChains(driver) 

def teardown_module():
    driver.quit()

def test_redirects():
    home_location = driver.current_url
    print(home_location)

    bbc = driver.find_element_by_id("bbc")

    #go to bbc website

    action.click(on_element = bbc)
    action.perform()
    time.sleep(3)

   # bbc_expected_result = driver.bbc.get_attribute("href")
    bbc_expected_result = "https://www.bbc.com/news"

    bbc_current_location = driver.current_url.rstrip('/')
    print(bbc_current_location)

    assert bbc_expected_result == bbc_current_location
    
    driver.get(home_location)

    global element_id
    
    element_id = "qa"
    qa = WebDriverWait(driver, 1).until(find_the_element_by_id)
    qa.click()

    time.sleep(3)
    qa_current_location = driver.current_url.rstrip('/')
    print(qa_current_location)

    qa_expected_result = "https://www.qa.com"

    assert  qa_expected_result == qa_current_location


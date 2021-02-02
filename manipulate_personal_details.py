import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 

driver = webdriver.Chrome('c:\\pf\\bin\\chromedriver.exe')  
# Optional argument, if not specified will search path.
#driver = webdriver.Chrome()
driver.get('file://C:/work/git/nodejs-sky/selenium-basics/practice_page.html')
# create action chain object 
action = ActionChains(driver) 

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

driver.close()

assert expected_result == result

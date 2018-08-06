from sys_config import *
import time
from selenium.webdriver.common.keys import Keys
from keys import *

driver = webdriver.Chrome(path,chrome_options = chrome_options)
driver.get('http://www.facebook.com/login')

time.sleep(1)

driver.find_element_by_name("email").send_keys(username)
time.sleep(1)

driver.find_element_by_xpath("//input[@name= 'pass']").send_keys(password)
time.sleep(1)

driver.find_element_by_name("login").click()

requests = driver.find_element_by_name('requests')
requests.click()

accept = driver.find_elements_by_name('actions[accept]')

print('number of reqs:',len(accept))


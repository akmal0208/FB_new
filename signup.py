from sys_config import *
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(path,chrome_options = chrome_options)
driver.get('http://www.facebook.com')
time.sleep(2)
firstname = driver.find_element_by_name('firstname')
surname = driver.find_element_by_name('lastname')
mobile = driver.find_element_by_name('reg_email__')
password = driver.find_element_by_name('reg_passwd__')
female = driver.find_element_by_name('sex')
signup = driver.find_element_by_name('websubmit')
day = driver.find_element_by_name('birthday_day')


firstname.send_keys('singapore')
time.sleep(1)
surname.send_keys('travels')
time.sleep(1)
mobile.send_keys('123')
time.sleep(1)
password.send_keys('123')
time.sleep(1)
day.click()
time.sleep(1)
day.send_keys(Keys.DOWN)
day.click()
female.click()
time.sleep(1)
signup.click()





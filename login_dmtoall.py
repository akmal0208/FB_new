from sys_config import *
import time
from selenium.webdriver.common.keys import Keys
from keys import *
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(path,chrome_options = chrome_options)
driver.get('http://www.facebook.com/login')

time.sleep(1)

driver.find_element_by_name("email").send_keys(username)
time.sleep(1)

driver.find_element_by_xpath("//input[@name= 'pass']").send_keys(password)
time.sleep(1)

driver.find_element_by_name("login").click()

time.sleep(1)

driver.get('http://www.facebook.com/profile')
time.sleep(1)
friends = driver.find_element_by_xpath('//a[@data-tab-key="friends"]')
friends.click()

time.sleep(5)
# coverpic = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.coverBorder')))
actions = ActionChains(driver)
for i in range(10):
	actions.send_keys(Keys.END)
	actions.perform()
	# coverpic.send_keys('Keys.END')
	time.sleep(1.2)

all_friends_list = driver.find_elements_by_css_selector('.fsl.fwb.fcb')
friend_link_list = []

for i in all_friends_list:
	try:
		friend = i.find_element_by_xpath('.//a')
		friend_link = friend.get_attribute('href')
		friend_link_list.append(friend_link)
	except Exception as e:
		print('kuch to gadbad hai: ',e)

for i in friend_link_list:
	## AT THIS STEP THERE ARE TWO OPTIONS, EITHER ADD FRIEND OR SEND MESSAGE. CHOOSE RESPECTIVE ACCORDING TO STATUS.
	driver.get(i)
	time.sleep(3)

# counter = 0
# for i in range(0,3):
# 	driver.get('https://www.facebook.com/friends/requests/?fcref=jwl')
# 	time.sleep(3)
# # confirm_button_list = driver.find_elements_by_link_text('Confirm')
# 	confirm_button_list = driver.find_elements_by_css_selector('._42ft._4jy0._4jy3._4jy1.selected._51sy')
	
# 	for i in confirm_button_list:
# 		try:
# 			i.click()
# 			time.sleep(0.2) # too fast otherwise 
# 			counter += 1
# 		except Exception as e:
# 			print('ERROR:',e,'probably element not visible')
# 	print('clicked',counter,'buttons')
# 	# driver.refresh()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

HOST = 'https://demoqa.com/text-box'

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get(HOST)
time.sleep(2)
driver.execute_script('window.scrollBy(0,400);')

full_name = driver.find_element(By.ID, "userName")
full_name.send_keys('Johnny')

email = driver.find_element(By.ID, "userEmail")
email.send_keys('johnny@gmail.com')

cur_address = driver.find_element(By.ID, 'currentAddress')
cur_address.send_keys('141 Nepture Avenue, 2 FL, Brooklyn, New York, 11235')

perm_address = driver.find_element(By.ID, "permanentAddress")
perm_address.send_keys('same as above')

button = driver.find_element(By.ID, 'submit')
button.send_keys(Keys.ENTER)
time.sleep(2)

# driver.quit()
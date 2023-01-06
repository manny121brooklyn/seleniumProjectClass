from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


# HOST = 'https://demoqa.com/automation-practice-form'
host = 'https://www.python.org'

# chrome_options = Options()
# chrome_options.add_experimental_option('detach', True)
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()

driver.get(host)
# button = driver.find_element(By.LINK_TEXT, "GUI Development")
# driver.execute_script('arguments[0].scrollIntoView();', button)
# time.sleep(5)
driver.execute_script('window.scrollTo(0,500);')
time.sleep(5)

# state_list = 'state'
# state_input = 'react-select-3-input'
# city_list = 'city'
# city_input = 'react-select-4-input'
#
# driver.get(HOST)
# # select state = NCR
# state_select = driver.find_element(By.ID, state_input)
# drop_down_select = Select(state_select)
# drop_down_select.select_by_visible_text('NCR')
# # check if City list is enabled
# # print(f'is city list enabled before selecting city? {driver.find_element(By.ID, city_list).is_enabled()}')
# # select city = Delhi
# city_select = driver.find_element(By.ID, city_input)
# drop_down_select = Select(city_select)
# drop_down_select.select_by_index(1)


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

HOST = 'https://jqueryui.com/droppable/'

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.implicitly_wait(10)

try:
    # Input Data


    # All locators(all values are ID locators
    # source_el = 'draggable'
    source_el = "//*[@id='draggable']"
    target_el = "//*[@id='droppable']"
    # target_el = 'droppable'

    # Steps
    driver.get(HOST)
    time.sleep(5)

    # code for drag and drop starts here
    # verify drop box text before dropping, expected: 'Drop here'
    # drag and drop the object into the box
    # verify drop box text after dropping, expected: 'Dropped'

    source = driver.find_element(By.XPATH, source_el)
    target = driver.find_element(By.XPATH, target_el)

    action = ActionChains(driver)
    action.drag_and_drop(source, target).perform()
    time.sleep(5)
    print(f'Drag and drop test successfully executed')


except Exception as err:
    time.sleep(2)
    print('Python Exception: test failed with the following exception.')
    print(err)

except (NoSuchElementException, TimeoutException) as err:
    time.sleep(2)
    print('Selenium Exception: test failed with the following exception')
    print(err)

finally:
    driver.quit()
    print('Test completed')
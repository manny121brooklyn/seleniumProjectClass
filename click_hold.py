import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

HOST = "https://www.geeksforgeeks.org/"

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()

try:
    # Input Data

    # All Locators(this value is Link_text locator)
    name_locator = 'Python'

    # Steps
    driver.get('https://www.geeksforgeeks.org/')
    time.sleep(3)

    # Code for click and hold
    element = driver.find_element(By.LINK_TEXT, name_locator)
    time.sleep(3)
    action = ActionChains(driver)
    action.click_and_hold(element).perform()


except Exception as err:
    print('Python Exception: Test failed with the following exception.')
    print(err)

except (NoSuchElementException, TimedOutException) as err:
    print('Selenium Exception: test failed with the following exception.')
    print(err)

finally:
    driver.quit()




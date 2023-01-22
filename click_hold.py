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
    # click on element and hold it
    element = driver.find_element(By.LINK_TEXT, name_locator)
    time.sleep(3)
    action = ActionChains(driver)
    # action.click_and_hold(element).perform()
    # click on element and hold it, pause 5 seconds
    # action.click_and_hold(element).pause(5).perform()
    # click on element and hold it, pause for 5 seconds, and release it.
    action.click_and_hold(element).pause(5).release(on_element=element).perform()
    time.sleep(2)
    # verify web element clicked and held
    print(driver.find_element(By.LINK_TEXT, name_locator).text)
#

except Exception as err:
    print('Python Exception: Test failed with the following exception.')
    print(err)

except (NoSuchElementException, TimedOutException) as err:
    print('Selenium Exception: test failed with the following exception.')
    print(err)

finally:
    driver.quit()




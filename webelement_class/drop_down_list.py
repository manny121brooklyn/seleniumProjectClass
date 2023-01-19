import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

try:
    #Input data
    country1 = 'United States'

    #All Locators(all values are ID locators)


    #Steps
except Exception as err:
    print(err)

except (NoSuchElementException, TimeoutException) as err:
    time.sleep(2)
    print('Selenium ex')
    print(err)

finally:
    driver.quit()
    print('Test completed')
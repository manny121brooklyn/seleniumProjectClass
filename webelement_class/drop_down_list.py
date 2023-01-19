import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

HOST = 'https://www.globalsqa.com/demo-site/select-dropdown-menu/'

try:
    #Input data
    country1 = 'United States'

    #All Locators(all values are ID locators)
    country_dd_tag = 'select'
    # no id, name or xpath available, therefore we chose <select> the only identifier

    #Steps
    driver.get(HOST)
    time.sleep(2)

    # check first selected option
    drop_down_elem = driver.find_element(By.TAG_NAME, country_dd_tag)
    select_country = Select(drop_down_elem)


    # check first selected option
    print('#check frist selected option')
    print(f'First selected option: {select_country.first_selected_option.text}')
    # the above is how to get the first item from the list
    # {select_country.first_selected_option.text}')

    # select united states from the drop down list
    print('Selecting by index: 2')
    select_country.select_by_index(2)
    print(f'Selected country {select_country.all_selected_options[0].text}')
    # this is how to print out text by index, we use [0].text to get item by index.
    # you can't get text from the list, you need to loop through the list using index []

    print('selecting by value(attribute): FRA...')
    select_country.select_by_value('FRA')
    print(f'Selected country {select_country.all_selected_options[0].text}')

    print('# select Unite States from drop down list')
    select_country.select_by_visible_text('United States')
    # verify 'United states' is selected: get all selected options
    print(f'Selected country {select_country.all_selected_options[0].text}')

    time.sleep(2)
    print('Drop down test is successfully completed.')


except Exception as err:
    time.sleep(2)
    print('Python Exception: test failed with the following exception.')
    print(err)

except (NoSuchElementException, TimeoutException) as err:
    time.sleep(2)
    print('Selenium Exception: test failed with following exception.')
    print(err)

finally:
    driver.quit()
    print('Test completed.')
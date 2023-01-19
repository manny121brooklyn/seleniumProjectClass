import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

HOST = 'https://demoqa.com/alerts'

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

try:
    # Input Data
    alert_input = 'United States'

    # All locators(all values are ID locators
    alert_notify = 'alertButton'
    alert_timer = 'timerAlertButton'
    alert_confirm = 'confirmButton'
    confirm_result = 'confirmResult'
    alert_prompt = 'promtButton'
    prompt_result = 'promptResult'


    # Steps
    driver.get(HOST)
    time.sleep(5)
    # click alert 1 button, click ok button to close the alert box
    button_elem = driver.find_element(By.ID, alert_notify)
    button_elem.click()
    time.sleep(2)
    click_me = driver.switch_to.alert
    print(click_me.text)
    click_me.accept()

    # click alert 2 button, click OK button, verify ok button is clicked in the result text

    # click alert 3 button, confirm the result, verify ok button is clicked in the result text
    # button = driver.find_element(By.ID, alert_confirm)
    # button.click()
    # time.sleep(2)
    # click_me = driver.switch_to.alert
    # click_me.accept()
    # confirm_result = driver.find_element(By.ID, confirm_result)
    # print(confirm_result.text)
    # click alert 3 button, dismiss the result, verify Cancel button is clicked in the result text
    button = driver.find_element(By.ID, alert_confirm)
    button.click()
    time.sleep(2)
    click_me = driver.switch_to.alert
    click_me.dismiss()
    confirm_result = driver.find_element(By.ID, confirm_result)
    print(confirm_result.text)
    # click alert 4 button, input the alert_input message, verify alert_input message in result text
    button = driver.find_element(By.ID, alert_prompt)
    button.send_keys(alert_input)
    button.click()
    time.sleep(2)
    click_me = driver.switch_to.alert
    click_me.dismiss()
    confirm_result = driver.find_element(By.ID, confirm_result)
    print(confirm_result.text)
    # click alert 4 button, input the alert_input, click OK button, verify alert_input message in the result text
    # click alert 4 button, input the alert_input, dismiss the alert, verify alert_input message not in the result text



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
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

HOST = 'https://demoqa.com/alerts'

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.maximize_window()

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

    print('# click alert 1 button, click ok button to close the alert box')
    driver.find_element(By.ID, alert_notify).click()
    time.sleep(2)
    alert = driver.switch_to.alert
    print(f"Text on the alert: '{alert.text}'")
    alert.accept()
    print(f'..........................................................')


    print('# click alert 2 button, click OK button, verify ok button is clicked in the result text')
    try:
        driver.find_element(By.ID, alert_timer).click()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept()
        # print(f'Text on the alert: {alert.text}')
    except Exception as err:
        print(err)
        print('no alert')
    print(f'..........................................................')


    print('# click alert 3 button, confirm the result, verify ok button is clicked in the result text')
    driver.find_element(By.ID, alert_confirm).click()
    time.sleep(2)
    alert = driver.switch_to.alert
    print(f'Text on alert:{alert.text}')
    alert.accept()
    result_msg = driver.find_element(By.ID, confirm_result).text
    print(f"Result message: '{result_msg}'")
    print(f'..........................................................')


    print('# click alert 3 button, dismiss the result, verify Cancel button is clicked in the result text')
    driver.find_element(By.ID, alert_confirm).click()
    time.sleep(2)
    click_me = driver.switch_to.alert
    print(f'Text on alert:{alert.text}')
    click_me.dismiss()
    result_msg = driver.find_element(By.ID, confirm_result)
    print(f"Message on alert: '{result_msg.text}'")
    print(f'..........................................................')

    print('# click alert 4 button, input the alert_input, click OK button, verify alert_input message in the result text')
    driver.find_element(By.ID, alert_prompt).click()
    time.sleep(2)
    alert = driver.switch_to.alert
    print(f"Text on the alert: '{alert.text}'")
    alert.send_keys(alert_input)
    alert.accept()
    result_msg = driver.find_element(By.ID, prompt_result)
    print(f"Result message: '{result_msg.text}'")
    print(f'..........................................................')
    time.sleep(3)


    print('# click alert 4 button, input the alert_input, dismiss the alert, verify alert_input message not in the result text')
    driver.find_element(By.ID, alert_prompt).click()
    time.sleep(2)
    alert = driver.switch_to.alert
    print(f"Text on the alert: '{alert.text}'")
    # alert.send_keys(alert_input)
    alert.dismiss()
    # result_msg = driver.find_element(By.ID, prompt_result)
    # print(f"Result message: '{result_msg.text}'")
    print(f'..........................................................')
    time.sleep(3)

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
    print('Alert Test completed')
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


HOST = 'https://jqueryui.com/resources/demos/droppable/default.html'
screenshot_dir = '../screenshots/'

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.implicitly_wait(10)

try:
    # Input Data

    # All locators(all values are ID locators
    draggable_id = 'draggable'
    droppable_id = 'droppable'

    # Steps
    driver.get(HOST)
    time.sleep(1)
    driver.save_screenshot(screenshot_dir+ 'dragdrop.png')

    # code for drag and drop starts here
    print("# verify drop box text before dropping, expected: 'Drop here'")
    drag_obj = driver.find_element(By.ID, draggable_id)
    drop_obj = driver.find_element(By.ID, droppable_id)
    print(f"Text in drop box, before: '{drop_obj.text}'")
    assert drop_obj.text == 'Drop here', "Drop box text verification, before drop action, failed"
    driver.save_screenshot(screenshot_dir+ 'dragdrop2-before.png')

    print('# drag and drop the object into the box')
    action = ActionChains(driver)
    action.drag_and_drop(drag_obj, drop_obj).perform()
    # time.sleep(2)
    # action.click_and_hold(source).release(target).perform()
    # action.click_and_hold(source).pause(2).release(target).perform()
    print(" # verify drop box text after dropping, expected: 'Dropped!'")
    print(f"Text in drop box, after drop: '{drop_obj.text}'")
    assert drop_obj.text == 'Dropped!', "Drop box text verification, after drop action, failed"
    driver.save_screenshot(screenshot_dir+ 'dragdrop3_after.png')

    # time.sleep(5)
    print(f'Drag and drop test successfully executed')


except (FileNotFoundError, ZeroDivisionError) as err:
    time.sleep(2)
    print('Python Exception: test failed with the following exception.')
    print(err)
    driver.save_screenshot(screenshot_dir + 'dragdrop4.png')

except Exception as err:
    time.sleep(2)
    print('Selenium Exception: test failed with the following exception')
    print(err)
    driver.save_screenshot(screenshot_dir+'dragdrop5.png')

finally:
    driver.quit()
    print('Test completed')
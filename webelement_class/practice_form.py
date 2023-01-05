from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


HOST = 'https://demoqa.com/automation-practice-form'

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()

try:
    # All locators:
    fn_input = 'firstName'
    ln_input = 'lastName'
    email_input = 'userEmail'
    gender_male_xpath = "//input[@id='gender-radio-1']/.."
    mobile_number_input = 'userNumber'
    date_of_birth_input = 'dateOfBirthInput'
    hobbies_sp_xpath = "//*[@id='hobbies-checkbox-1']/.."
    hobbies_reading_xpath = 'hobbies-checkbox-2'
    upload_pic_input = 'uploadPicture'
    address_textarea = 'currentAddress'
    state_list = 'state'
    state_input = 'react-select-3-input'
    city_list = 'city'
    city_input = 'react-select-4-input'
    submit_button = 'submit'
    confirmation_msg = 'example-modal-sizes-title-lg'
    close_cm_button = 'closeLargeModal'

    # Steps
    driver.get(HOST)
# enter first_name = 'John', last_name='Doe', enter email address 'jdoe@gmail.com
    first_name = 'John'
    last_name = 'Doe'
    email = 'jdoe@gmail.com'
    driver.find_element(By.ID, fn_input).send_keys(first_name)
    driver.find_element(By.ID, ln_input).send_keys(last_name)
    driver.find_element(By.ID, email_input).send_keys(email)

# select radio button Gender = 'Male'
    driver.find_element(By.XPATH, gender_male_xpath).click()
# Enter mobile number 987654321
    mobile_number = '9876543210'
    driver.find_element(By.ID, mobile_number_input).send_keys(mobile_number)
# enter dateOfBirth = 27 Nov 2008
#     date_of_birth = '16 Sep 2008'
    # driver.find_element(By.ID, date_of_birth_input).clear()
    # driver.find_element(By.ID, date_of_birth_input).send_keys(date_of_birth)
# enter subjects = 'selenium forms testing'
# select checkboxes, select Sports, Reading
    driver.find_element(By.XPATH, hobbies_sp_xpath).click()
    driver.find_element(By.XPATH, hobbies_reading_xpath).click()
# (optional) upload picture
# enter message in text_area = '2906 Shell Road, 12224'
    address = '2906 Shell Road, 12224'
    driver.find_element(By.ID, address_textarea).send_keys(address)
# check if State list is enabled
    print(f'is State list enabled before selecting state? {driver.find_element(By.ID,state_list).is_enabled()}')
# select state = NCR
    driver.find_element(By.ID, state_input).send_keys('NCR')
#     state_select = driver.find_element(By.ID, state_input)
#     drop_down_select = Select(state_select)
#     drop_down_select.select_by_visible_text('NCR')
# check if City list is enabled
    print(f'is city list enabled before selecting city? {driver.find_element(By.ID, city_list).is_enabled()}')
# select city = Delhi
    driver.find_element(By.ID, city_input).send_keys('Delhi')
#     city_select = driver.find_element(By.ID, city_input)
#     drop_down_select = Select(city_select)
#     drop_down_select.select_by_index(1)
# check if Gender = Male is selected
    print(f'is gender male selected? {driver.find_element(By.XPATH, gender_male_xpath).is_selected()}')
# check if Sports hobbies is selected
    print(f'is Sports check box selected? {driver.find_element(By.XPATH, hobbies_sp_xpath).is_selected()}')
# click submit
    driver.find_element(By.ID, submit_button).click()
# veryfy Thanks for submitting the form message
    print(driver.find_element(By.ID, confirmation_msg).text)
    print(f'is Confirmation message displayed?{driver.find_element(By.ID, confirmation_msg).is_displayed()}')
    # click on Pop up message to close
    driver.find_element(By.ID, close_cm_button).click()
    time.sleep(10)

# except Exception as err:
#  print('any error')
#
finally:
    print('done')






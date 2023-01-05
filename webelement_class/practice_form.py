from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options


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
    gender_male = 'gender-radio-1'
    mobile_number_input = 'userNumber'
    date_of_birth_input = 'dateOfBirthInput'
    hobbies_sp = 'hobbies-checkbox-1'
    hobbies_reading = 'hobbies-checkbox-2'
    upload_pic_input = 'uploadPicture'
    address_textarea = 'currentAddress'
    city_list = 'react-select-3-input'
    state_list = 'react-select-4-input'
    submit_button = 'submit'
    confirmation_msg = 'example-modal-sizes-title-lg'
    close_cm_button = 'closeLargeModal'

    # Steps
    driver.get(HOST)
# enter first_name = 'John', last_name='Doe', enter email address 'jdoe@gmail.com
# select radio button Gender = 'Male'
# Enter mobile number 987654321
# enter dateOfBirth = 27 Nov 2008
# enter subjects = 'selenium forms testing'
# select checkboxes, select Sports, Reading
# (optional) upload picture
# enter message in text_area = ' 2906 Shell Road, 12224'
# check if City list is enabled
# select state = NCR
# check if City list is enabled
# select city = Delhi
# check if Gender = Male is selected
# check if Sports hobbies is selected
# click submit
# veryfy Thanks for submitting the form message


    first_name = driver.find_element()


# https://www.udemy.com/course/the-complete-python-course/learn/lecture/15206664#overview

import time

#implicit wait

import  time

#time.sleep(5) # 5 seconds
# this is risky as what you are expecting could take less than 5 secs, so you are just adding more time execution without needing it


from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support.ui import  Select

TAG_SEARCH_AREA = "sb_form_q"
JUST_ID = By.ID, TAG_SEARCH_AREA
CSS_TAG_SELECTOR = "input#sb_form_q"

#WebDriverWait(chrome_driver,10).until(
#    expected_conditions.presence_of_all_elements_located
#        (By.CSS_SELECTOR, TAG_SEARCH_AREA)
#)
# this will wait until i get an answer from this selector, max wait is 10 sec

chrome = webdriver.Chrome(executable_path="D:\Alex\chromedriver_win32\chromedriver")
chrome.get('https://www.bing.com/')

# explicit wait
chrome.implicitly_wait(10) # seconds
#its not that recomended to use this

inputElement = chrome.find_element_by_id("sb_form_q")
inputElement.send_keys("Toto is the best")
inputElement.submit()



# https://www.udemy.com/course/the-complete-python-course/learn/lecture/15206664#overview
# using By is recomended in finding elements.

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.support.ui import  Select

TAG_SEARCH_AREA = "sb_form_q"
JUST_ID = By.ID, TAG_SEARCH_AREA
CSS_TAG_SELECTOR = "input#sb_form_q"

# this will search in Bing
chrome = webdriver.Chrome(executable_path="D:\Alex\chromedriver_win32\chromedriver")
chrome.get('https://www.bing.com/')
#inputElement = chrome.find_element_by_id("sb_form_q")
#inputElement.send_keys("Toto is the best")
#inputElement.submit()

# Others ways to select an element is wuth
#inputElement = chrome.find_element_by_id(TAG_SEARCH_AREA)
#inputElement.send_keys("Toto is the best")
#inputElement.submit()

# OR using this
#inputElement = chrome.find_element(By.ID, TAG_SEARCH_AREA)
#inputElement.send_keys("Toto is the best")
#inputElement.submit()

# OR this solution that si recomended
#inputElement = chrome.find_element(*JUST_ID) # this will unpack the 2 values of the tupple and give them as arguments
#inputElement.send_keys("Toto is the best")
#inputElement.submit()

# OR using the css selector
#inputElement = chrome.find_element_by_css_selector(CSS_TAG_SELECTOR)
inputElement = chrome.find_element(By.CSS_SELECTOR, CSS_TAG_SELECTOR)
inputElement.send_keys("Toto is the best")
inputElement.submit()
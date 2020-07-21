
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/15206666#overview
# This is better for a dropdown that will receive values based on another dropdown
# Its better to check he tutorial, as the website used in it is not available at the moment.
# And in my examples i just check an already available element, i don't have a dinamic dropdown.

from selenium import webdriver
from selenium.webdriver.support.ui import  Select

# these are needed for the Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

TAG_SEARCH_AREA = "sb_form_q"

chrome = webdriver.Chrome(executable_path="D:\Alex\chromedriver_win32\chromedriver")
chrome.get('https://www.bing.com/')

WebDriverWait(chrome,10).until(
    expected_conditions.presence_of_all_elements_located
        (By.ID, TAG_SEARCH_AREA) # the expected_condition module needs to have 2 arguments : By and the locator
)
# this will wait up up 10 secs until the ID is foudn in the page. But it will not check if the searched element is also visible in the Page.
# This is a mix between implicit and explicit wait mode.

inputElement = chrome.find_element_by_id(TAG_SEARCH_AREA)
inputElement.send_keys("Toto is the best")
inputElement.submit()


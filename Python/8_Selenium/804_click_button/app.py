from selenium import webdriver
from selenium.webdriver.support.ui import  Select

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/15206658#overview
# https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=USD

chrome = webdriver.Chrome(executable_path="D:\Alex\chromedriver_win32\chromedriver")
chrome.get('https://www.ubaldi.com/18/tv-ultra-hd-4k--pl1084.php')

element = chrome.find_element_by_css_selector('span.ta-btn')
element.click()

element2 = chrome.find_element_by_xpath()



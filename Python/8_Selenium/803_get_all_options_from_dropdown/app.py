from selenium import webdriver
from selenium.webdriver.support.ui import  Select

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/15206656#overview
# https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=USD

chrome = webdriver.Chrome(executable_path="D:\Alex\chromedriver_win32\chromedriver")
chrome.get('https://www.ubaldi.com/18/tv-ultra-hd-4k--pl1084.php')

element = chrome.find_element_by_css_selector('select#tri')
select1 =  Select(element)
values = [option.text.strip() for option in select1.options] # this will get all values from a dropdown list
print ("Tags : [{}]".format(" | ".join(values))) # this will join several string values, concatinated with | symbol
selected_value = input ('Enter your value :_')
select_value = select1.select_by_visible_text(selected_value)


from selenium import webdriver
from selenium.webdriver.support.ui import  Select

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/15206654#overview
# https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=USD

chrome = webdriver.Chrome(executable_path="D:\Alex\chromedriver_win32\chromedriver")
chrome.get('https://www.ubaldi.com/18/tv-ultra-hd-4k--pl1084.php')

element = chrome.find_element_by_css_selector('select#tri') # we use elemenT as we are looking just for one and not all that will match
# we have identified the dropdown by using a css selector with the select tag name and the name atribute value : tri
# <select id ='tri' name='tri'>
select1 =  Select(element)
Select(element).select_by_visible_text('Meilleures notes')
# we have selected a harcoded value from a dropdown
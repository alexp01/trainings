from selenium import webdriver
from selenium.webdriver.support.ui import  Select

# Examples how to find elements with Selenium
# https://www.techbeamers.com/locate-elements-selenium-python/

# 1. Locate Element by Name
# will select the search area and insert a search value
def get_by_name():
    chrome = webdriver.Chrome(executable_path="D:\Alex\chromedriver_win32\chromedriver")
    chrome.get('https://www.google.com/')
    chrome.maximize_window()
    inputElement = chrome.find_element_by_name("q")
    inputElement.send_keys("Toto is the best")
    inputElement.submit()

# 2. Locate Element by ID
def get_by_id():
    chrome = webdriver.Chrome(executable_path="D:\Alex\chromedriver_win32\chromedriver")
    chrome.get('https://www.bing.com/')
    inputElement = chrome.find_element_by_id("sb_form_q")
    inputElement.send_keys("Toto is the best")
    inputElement.submit()

# 3. Locate Element by Link Text
def get_by_text():
    chrome = webdriver.Chrome(executable_path="D:\Alex\chromedriver_win32\chromedriver")
    chrome.get('https://www.google.com/')
    chrome.maximize_window()
    inputElement = chrome.find_element_by_name("q")
    inputElement.send_keys("Toto")
    inputElement.submit()
    elem = chrome.find_element_by_link_text("YouTube")
    elem.click()

# 4. Locate Element by Partial Link Text
def get_by_partial_text():
    chrome = webdriver.Chrome(executable_path="D:\Alex\chromedriver_win32\chromedriver")
    chrome.get('https://www.google.com/')
    chrome.maximize_window()
    inputElement = chrome.find_element_by_name("q")
    inputElement.send_keys("Toto")
    inputElement.submit()
    elem = chrome.find_element_by_partial_link_text("YouTu")
    elem.click()

# 5. Locate Element by XPath
def get_by_xpath():
    chrome = webdriver.Chrome(executable_path="D:\Alex\chromedriver_win32\chromedriver")
    chrome.get('https://www.bing.com/')
    chrome.maximize_window()
    inputElement = chrome.find_element_by_xpath("//form[@class='sb_form hassbi']/input[@id='sb_form_q']")
    inputElement.send_keys("Toto")
    inputElement.submit()
    elem = chrome.find_element_by_xpath("//span[@class='bm_details_overlay']/a[1]")
    elem.click()

#6. Locate Element by CSS Selector
def get_by_css():
    chrome = webdriver.Chrome(executable_path="D:\Alex\chromedriver_win32\chromedriver")
    chrome.get('https://www.bing.com/')
    chrome.maximize_window()
    inputElement = chrome.find_element_by_css_selector('form input.sb_form_q')
    inputElement.send_keys("Toto")
    inputElement.submit()
    elem = chrome.find_element_by_css_selector('div.mc_vtvc_title')
    elem.click()

# 7. Locate Element by Tagname
def get_by_tag_name():
    chrome = webdriver.Chrome(executable_path="D:\Alex\chromedriver_win32\chromedriver")
    chrome.get('https://www.bing.com/')
    chrome.maximize_window()
    inputElement = chrome.find_element_by_tag_name('input')
    inputElement.send_keys("Toto")
    inputElement.submit()
    elem = chrome.find_element_by_tag_name('h1')
    elem.click()

# 8. Locate Element by Classname
def get_by_class_name():
    chrome = webdriver.Chrome(executable_path="D:\Alex\chromedriver_win32\chromedriver")
    chrome.get('https://www.bing.com/')
    chrome.maximize_window()
    inputElement = chrome.find_element_by_class_name('sb_form_q')
    inputElement.send_keys("Toto")
    inputElement.submit()
    elem = chrome.find_element_by_class_name('mc_vtvc_htc')
    elem.click()

print("""
1. Locate Element by Name
2. Locate Element by ID
3. Locate Element by Link Text
4. Locate Element by Partial Link Text
5. Locate Element by XPath
6. Locate Element by CSS Selector
7. Locate Element by Tagname
8. Locate Element by Classname
""")
option = input('What kind of search do you want to perform from 1-8:_')
if option == '1':
    get_by_name()
elif option == '2':
    get_by_id()
elif option == '3':
    get_by_text()
elif option == '4':
    get_by_partial_text()
elif option == '5':
    get_by_xpath()
elif option == '6':
    get_by_css()
elif option == '7':
    get_by_tag_name()
elif option == '8':
    get_by_class_name()

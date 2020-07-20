from selenium import webdriver
from pages.quotes_page import QuotePage

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/15206648#questions

chrome = webdriver.Chrome(executable_path="D:\Alex\chromedriver_win32\chromedriver")
chrome.get('http://quotes.toscrape.com')
page = QuotePage(chrome)

for quote in page.quotes:
    print(quote)

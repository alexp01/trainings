from pages.quotes_page import QuotePage
from bs4 import BeautifulSoup
import requests

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477898#questions
# http://quotes.toscrape.com/

page = requests.get('http://quotes.toscrape.com/').content # this will get the full content of the webpage in html
page_content = QuotePage(page) # this will parse the html in an Object

for page in page_content.quotes: # page_content.quotes will return a list of objects of type QuoteParser, where self.parent is a quote block
    print(page) # page is now an element of that list of objects of type QuoteParser. As it has the dunder repr method, it will print that when we want to print the Object QuoteParser
    print(page.content) # as page is an QuoteParser objects, we can have access to its methods as parameters as they are @property type functions

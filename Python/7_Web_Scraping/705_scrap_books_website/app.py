from bs4 import BeautifulSoup
import requests

import logging

from pages.books_page import BookPage
from locators.books_page_locators import BookPageLocators

MAIN_PAGE = 'http://books.toscrape.com/'

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]:%(message)s',
    datefmt = '%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename = 'logs.txt'
)
logger = logging.getLogger('scraping')

# in the training they just do a for in range of 50, as there are 50 pages. They also read teh 50 from html. Its a faster and shorter solution.
# my implementation is come complex. but it covers the case when the URL of different pages will change.

def get_all_pages():
    list_of_all_pages = []
    page_content = requests.get(MAIN_PAGE).content
    soup = BeautifulSoup(page_content, 'html.parser')
    locator = BookPageLocators.NEXT_BOOK
    next_page_url = soup.select_one(locator).attrs['href'][10:]
    while next_page_url:
        list_of_all_pages.append(next_page_url)
        page_content = requests.get(MAIN_PAGE+ 'catalogue/' + next_page_url).content
        soup = BeautifulSoup(page_content, 'html.parser')
        try:
            next_page_url = soup.select_one(locator).attrs['href']
        except AttributeError:
            break
    logger.info('We got all pages url. tags')
    return list_of_all_pages


page_content = requests.get('http://books.toscrape.com/').content
all_pages_url = get_all_pages()
print (all_pages_url)

first_page = 0
books = []

# Now a go into every page and parse the books. Each book tag will be added to the books variable
for pages in all_pages_url:
    if first_page == 0:
        page_content = requests.get(MAIN_PAGE).content
        first_page = 1
    else:
        page_content = requests.get(MAIN_PAGE + 'catalogue/' + pages).content
    page = BookPage(page_content)
    books_in_1_page = page.books
    for book in books_in_1_page:
        books.append(book)
logger.info('Creating BookPage objects from each book in all pages')


# The bellow solution is the ones where you read only the first page
#page_content = requests.get(MAIN_PAGE).content
#page_content = requests.get(MAIN_PAGE).content
#page = BookPage(page_content)
#books = page.books
#for book in books:
#    print(book)



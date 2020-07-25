from bs4 import BeautifulSoup
import requests
import time

from pages.books_page import BookPage
from locators.books_page_locators import BookPageLocators

MAIN_PAGE = 'http://books.toscrape.com/'

books = []

for x in range(1, 50):
    page_content = requests.get(MAIN_PAGE + 'catalogue/page-' + str(x) + '.html').content
    page = BookPage(page_content)
    books_in_1_page = page.books
    for book in books_in_1_page:
        books.append(book)




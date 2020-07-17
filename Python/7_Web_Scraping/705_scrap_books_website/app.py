from bs4 import BeautifulSoup
import requests

from pages.books_page import BookPage
from locators.books_page_locators import BookPageLocators

MAIN_PAGE = 'http://books.toscrape.com/'

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
    return list_of_all_pages

page_content = requests.get('http://books.toscrape.com/').content
all_pages_url = get_all_pages()
print (all_pages_url)

object_with_all_book_in_all_pages = []

for pages in all_pages_url:
    page_content = requests.get(MAIN_PAGE + 'catalogue/' + pages).content
    print (MAIN_PAGE + 'catalogue/' + pages)
    page = BookPage(page_content)
    books_in_1_page = page.books
    for book in books_in_1_page:
        print (book)
    object_with_all_book_in_all_pages.append(books_in_1_page)
    #print(object_with_all_book_in_all_pages)

#books = object_with_all_book_in_all_pages

#page_content = requests.get(MAIN_PAGE).content
#page_content = requests.get(MAIN_PAGE).content
#page = BookPage(page_content)
#books = page.books
#for book in books:
    print(book)



from bs4 import BeautifulSoup

from locators.books_page_locators import BookPageLocators
from parsers.book import BookParser

class BookPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page,'html.parser')

    @property
    def books(self):
        locator = BookPageLocators.BOOK
        book_tags = self.soup.select(locator) # this will identify a single book tag
        return [BookParser(e) for e in book_tags] # for all books tag this will return an object that contains elements from the book tag, like name, price, starst etc.


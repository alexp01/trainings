from locators.books_locator import BooksLocators

class BookParser:
    """
    will receive a tag for a book and return tags for elements (name, price, availability and star rating) of each book
    """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Book: {self.name} / Price {self.price}/ Rating {self.star[0]}'

    @property
    def name(self):
        locator = BooksLocators.NAME
        return self.parent.select_one(locator).attrs['title']

    @property
    def price(self):
        locator = BooksLocators.PRICE
        return self.parent.select_one(locator).string

    @property
    def star(self):
        locator = BooksLocators.STARS
        full_rating = self.parent.select_one(locator).attrs['class']
        return [e for e in full_rating if e != 'star-rating']

#    @property
#    def stock(self):
#        locator = BooksLocators.STOCK
#        return self.parent.select_one(locator).string
from locators.books_locator import BooksLocators

class BookParser:
    """
    will receive a tag for a book and return tags for elements (name, price, availability and star rating) of each book
    """

    Ratings = {
        'One' : 1,
        'Two': 2,
        'Three': 4,
        'Four': 5,
        'Five': 6
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        #return f'Book: {self.name} / Price {self.price}/ Rating {self.star} / {self.url}' # the url is not necesarry
        return f'Book: {self.name}  Price {self.price} Rating {self.star}'

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
        rating_string = [e for e in full_rating if e != 'star-rating']
        return BookParser.Ratings.get(rating_string[0]) # in case nothing will match it will return none. To avoid you cna give a defualt return value to teh get : get(rating_string[0], default 9)

    @property
    def url(self):
        locator = BooksLocators.LINK
        return self.parent.select_one(locator).attrs['href']

#    @property
#    def stock(self):
#        locator = BooksLocators.STOCK
#        return self.parent.select_one(locator).string
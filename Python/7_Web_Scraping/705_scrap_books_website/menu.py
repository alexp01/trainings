
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477964#questions
# http://books.toscrape.com/

from app import books
# this will run the app file until the books variable is used, including the var value atribution

import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]:%(message)s',
    datefmt = '%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename = 'logs.txt'
)
logger = logging.getLogger('books')

logger.info('This is a info type message')
logger.warning('This is a warning')

MENU = """ Select one of the falowings:
- 'b' to look at 5 star books
- 'c' to see the cheepest 5 books
- 'n' to just get the next available book from the catalog
- 'q' to exit
"""

for y in
    generator_list = (x for x in books)

def give_next_book():
    (next(generator_list))

def print_best_5_books():
    best_books = sorted(books, key=lambda x: x.star) # this will sort the list of books by their rating
    # we limit the size of this list to just 5 elements.
    for book in best_books[-5:]: # this is a way to get the last elements as the sorting is done ascending
        # another way to order descending is : best_books = sorted(books, key=lambda x: x.star * -1) : this will sort ascending as it starts from -6 to -1. But the end results are in decending order by star rating.
        print(book)

def print_5_stars_books():
    best_books = sorted(books, key=lambda x: x.star)
    for book in best_books:
        if book.star == 5:
            print(book)

def print_cheepest_5_books():
    cheep_books = sorted(books, key=lambda x: x.price)[-5:]
    for book in cheep_books:
        print(book)

def print_best_books_sorted_also_by_price():
    cheep_books = sorted(books, key=lambda x: ( x.star * -1, x.price)) #this will sort first by star rating, and each category of star, it will be sorted by price ascending
    for book in cheep_books:
        print(book)

#print_best_5_books()
#print_cheepest_5_books()
#print_best_books_sorted_also_by_price()

generator = 0
def show_menu():
    get_user_option = input (MENU)
    while get_user_option != 'q':
        if get_user_option == 'c':
            print_cheepest_5_books()
        elif get_user_option == 'b':
            print_5_stars_books()
        elif get_user_option == 'n':
            give_next_book()
        get_user_option = input(MENU)

show_menu()


#logger.info('This is a info type message')
#logger.warning('This is a warning')
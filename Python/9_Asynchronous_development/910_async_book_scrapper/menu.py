
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477964#questions
# http://books.toscrape.com/

from app import books
# this will run the app file until the books variable is used, including the var value atribution

MENU = """ Select one of the falowings:
- 'b' to look at 5 star books
- 'c' to see the cheepest 5 books
- 'n' print next 5 books
- 'q' to exit
"""

generator_list = (x for x in books)

def print_next_book(): # i used a generator just for this function, so i can benefit from the next function
    print (next(generator_list))
    print (next(generator_list))
    print (next(generator_list))
    print (next(generator_list))
    print (next(generator_list))

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
    cheep_books = sorted(books, key=lambda x: x.price)
    for book in cheep_books[:5]:
        print(book)

def print_best_books_sorted_also_by_price():
    cheep_books = sorted(books, key=lambda x: ( x.star * -1, x.price)) #this will sort first by star rating, and each category of star, it will be sorted by price ascending
    for book in cheep_books:
        print(book)

#print_best_5_books()
#print_cheepest_5_books()
#print_best_books_sorted_also_by_price()

user_choise = {
    'c' : print_cheepest_5_books,
    'b' : print_5_stars_books,
    'n' : print_next_book
}

generator = 0
def show_menu():
    get_user_option = input (MENU)
    while get_user_option != 'q':
        if get_user_option in ('c', 'b', 'n'):
            user_choise[get_user_option]()
        get_user_option = input(MENU)

show_menu()

#from utils.database import create_db

# The scope of this project is to store books in a file, and have different functionalities like add, remove, list, mark as read etc.
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445314#questions/11460302
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445318#questions/11460302

book = []
book_menu_options = """
MENU :
- q quit and go back to main menu
- a add a book
- r remove a book
- l list all books
- m mark a book as read
_"""
main_menu_options = """
Please type an option:
- 1 to load the list of books from DB
- 2 to update the DB with recent changes
- o for operations
- q to quit
"""

def menu():
    global book
    main_menu_option = input(main_menu_options)
    while main_menu_option != 'q':
        if main_menu_option == 'o':
            menu_option = input(book_menu_options)
            while menu_option != 'q':
                if menu_option == 'a':
                    name, author = input('Please give the name and author, separated by , :_').split(',')
                    add_a_book(name, author)
                if menu_option == 'l':
                    list_all_book()
                if menu_option == 'r':
                    name, author = input('Please give the name and author, separated by , :_').split(',')
                    temp_book = delete_a_book(name,author)
                    book = temp_book
                if menu_option == 'm':
                    name = input('Please give the name of the book:_')
                    mark_as_read(name)
                menu_option = input(book_menu_options)
        elif main_menu_option == '1':
            write_in_list_from_file()
        elif main_menu_option == '2':
            update_file_from_list()
        main_menu_option = input(main_menu_options)

def write_in_list_from_file():
    database_file = open('database.txt', 'r')
    database_content = database_file.readlines()
    database_file.close()
    lines = [line.strip() for line in database_content[0:]]
    for line in lines:
        a, b, c = line.split(',')
        book.append(dict([('name',a),('author',b),('read',c)]))
    print (book)

def update_file_from_list():
    database_file2 = open('database.txt', 'w')
    database_file2.writelines((lines['name']+','+lines['author']+','+lines['read']+'\n') for lines in book)
    database_file2.close()

def add_a_book(name, author):
    book.append(dict([('name',name),('author',author),('read',False)]))

def delete_a_book(name,author):
    global book
    temp_book = [x for x in book if x['name'] != name and x['name'] != author]
    #book = [book1 for book1 in book if book1['name'] != name and book1['author'] != author]
    return temp_book

def list_all_book():
    for line in book:
        read = 'YES' if line['read'] else 'NO' # if line[read] is TRUE then the read var will get the 'YES' value
        print(f"{line['name']} by {line['author']}, read : {read}")

def mark_as_read(name):
    global book
    for x in book:
        if x['name'] == name:
            x['read'] = True

menu()
#


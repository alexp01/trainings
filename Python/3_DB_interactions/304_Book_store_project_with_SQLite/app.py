from main_logic import read_from_file, mark_as_read, add_a_book, delete_a_book, create_db

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445368#questions/11460302

book_menu_options = """
MENU :
- q quit and go back to main menu
- a add a book
- r remove a book
- l list all books
- m mark a book as read
_"""

def menu():
    #print(check_if_file_exists()) # if i call this it will delete the content of the existing txt file. Don't know why yet as i don't write on it.
    create_db()
    menu_option = input(book_menu_options)
    while menu_option != 'q':
        if menu_option == 'a':
            name, author = input('Please give the name and author, separated by , :_').split(',')
            add_a_book(name,author)
        elif menu_option == 'l':
            books = read_from_file()
            for book in books:
                read = 'YES' if book['read'] else 'NO' # we do not have to compare it with == 1 as 1 is seen as true by Python
                print(f"Book: '{book['name']}', by '{book['author']}', read = {read}")
        elif menu_option == 'r':
            name = input('Please give the name :_')
            delete_a_book(name)
        elif menu_option == 'm':
            name = input('Please give the name of the book:_')
            mark_as_read(name)
        else:
            print('Unknown command')
        menu_option = input(book_menu_options)

menu()



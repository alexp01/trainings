from main_logic import read_from_file, mark_as_read, add_a_book, delete_a_book

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445320#questions/11460302

book_menu_options = """
MENU :
- q quit and go back to main menu
- a add a book
- r remove a book
- l list all books
- m mark a book as read
_"""

def menu():
    menu_option = input(book_menu_options)
    while menu_option != 'q':
        if menu_option == 'a':
            name, author = input('Please give the name and author, separated by , :_').split(',')
            add_a_book(name,author)
        elif menu_option == 'l':
            books = read_from_file()
            for book in books:
                read = 'YES' if book['read'] == '1' else 'NO'
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



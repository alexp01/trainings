"""
API with logic for file storage in SQLite DB
"""

import sqlite3

def create_db():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE BOOKS (NAME text primary key, AUTHOR text, READ integer)')
    cursor.execute('INSERT INTO BOOKS VALUES ('Book1', 'Author1', 0)')
    cursor.execute('SELECT * FROM BOOKS')
    connection.commit()

    connection.close()

def check_if_file_exists():
    with open(file_to_store, 'w'): # this will create the file in case it does not exist
        pass

def read_from_file():
     with open(file_to_store, 'r') as file:
        books = json.load(file)
    return books

def add_a_book(name,author):
    books = read_from_file()
    books.append(dict([('name', name), ('author', author), ('read', '0')]))
    # We can skip the dict and just add a dict as an list element like : {'name' = name, 'author' = author, 'read' = '0' }
    write_to_file(books)

def mark_as_read(name):
    books = read_from_file()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    write_to_file(books)

def delete_a_book(name):
    books = read_from_file()
    books = [book for book in books if book['name'] != name]
    write_to_file(books)

def write_to_file(books):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('sadsad')
    #connection.commit()
    connection.close()

    with open(file_to_store, 'w') as file:
        json.dump(books,file)


"""
API with logic for file storage in SQLite DB
"""

import sqlite3

def create_db():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS BOOKS(NAME text primary key, AUTHOR text, READ integer)')
    connection.commit()
    connection.close()

def read_from_file():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM BOOKS')
    books = [{'name' : row[0], 'author' : row[1], 'read' : row[2]} for row in cursor.fetchall()]
    print (books)
    connection.close()
    return books

def add_a_book(name,author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    #cursor.execute(f'INSERT INTO BOOKS VALUES("{name}","{author}", 0)')
    # by doing the above method, SQLITE will validate that the inserted variable don't contain anything dangerous like DROP TABLE BOOKS etc...
    cursor.execute(f'INSERT INTO BOOKS VALUES(?,?, 0)', (name,author))
    connection.commit()
    connection.close()

def mark_as_read(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute(f'UPDATE BOOKS SET READ = 1 WHERE NAME = ?', (name,) )
    connection.commit()
    connection.close()

def delete_a_book(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM BOOKS WHERE NAME = ?', (name,))
    connection.commit()
    connection.close()
"""
API with logic for file storage in SQLite DB
"""

from database_connection import DatabaseConnection:

def create_db():
    with DatabaseConnection('data.db') in connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS BOOKS(NAME text primary key, AUTHOR text, READ integer)')

def read_from_file():
    with DatabaseConnection('data.db') in connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM BOOKS')
        books = [{'name' : row[0], 'author' : row[1], 'read' : row[2]} for row in cursor.fetchall()]
        print (books)
    return books

def add_a_book(name,author):
    with DatabaseConnection('data.db') in connection:
        cursor = connection.cursor()
        #cursor.execute(f'INSERT INTO BOOKS VALUES("{name}","{author}", 0)')
        # by doing the above method, SQLITE will validate that the inserted variable don't contain anything dangerous like DROP TABLE BOOKS etc...
        cursor.execute(f'INSERT INTO BOOKS VALUES(?,?, 0)', (name,author))

def mark_as_read(name):
    with DatabaseConnection('data.db') in connection:
        cursor = connection.cursor()
        cursor.execute(f'UPDATE BOOKS SET READ = 1 WHERE NAME = ?', (name,) )

def delete_a_book(name):
    with DatabaseConnection('data.db') in connection:
        cursor = connection.cursor()
        cursor.execute(f'DELETE FROM BOOKS WHERE NAME = ?', (name,))
    c
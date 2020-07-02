"""
API with logic for file storage
"""

file_to_store = 'database.txt'
print (file_to_store)

def read_from_file():
    with open(file_to_store, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
    books = [{'name' : line[0],'author' : line[1], 'read' : line[2]}  for line in lines]
    return books

def add_a_book(name,author):
    with open(file_to_store, 'a') as file: # to Append we use 'a'
        file.write(name+','+author+','+'0\n')

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
    with open(file_to_store, 'w') as file:
        for book in books:
            file.write(book['name']+','+book['author']+','+book['read']+'\n')


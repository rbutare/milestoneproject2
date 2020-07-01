"""
Concerned with storing and retrieving books from  a list
- 'a' to add a new book
-'l' to list all books
-'r' to mark a book as read
-'d' to delete a book
-'q' to quit
"""
import _sqlite3
from collections import OrderedDict
from typing import Dict, Union


def create_book_table():
    connection = _sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

    connection.commit()

    connection.close()


def get_all_books():
    connection = _sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books = [{"name": row[0], "author": row[1], "read": row[2]} for row in cursor.fetchall()]
    connection.close()
    return books


def a(name, author):
    connection = _sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))

    connection.commit()

    connection.close()


def l(books):
    books = get_all_books()
    read = "yes" if books['read'] else "no"
    print(f"{books['name']} written by {books['author']} read: {read}")


def r(book_name):
    connection = _sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET read="1" WHERE name=?', (book_name,))
    connection.commit()
    connection.close()


def d(book):
    connection = _sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE name=?', (book,))
    connection.commit()
    connection.close()

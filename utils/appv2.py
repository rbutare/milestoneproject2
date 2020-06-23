"""
Concerned with storing and retrieving books from  a list
- 'a' to add a new book
-'l' to list all books
-'r' to mark a book as read
-'d' to delete a book
-'q' to quit
"""
import csv
books = []


def save_to_csv:
    with open("library.csv","w") as lib:
        fieldnames = ['name', 'author', 'read']
        writer = csv.DictWriter(lib, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(books)

def a():
    books.append(dict(
        name=input("Enter book name:"),
        author=input("Enter book author:"),
        read=False
    ))
    save_to_csv()


def l():
    print(f'Your library has {len(books)} books:')
    for elem in books:
        print(f"{elem['name']} by {elem['author']}" f"{'(was read)' if elem['read'] == True else '(not read)'}")


def r():
    user_input = input("What title are you reading?:")
    global books
    for book in books:
        if book['name'] == user_input:
            book['read'] = True
            save_to_csv()


def d():
    user_input = input("What title would like to delete:")
    global books
    books = [book for book in books if book['name'] != user_input]
    save_to_csv()

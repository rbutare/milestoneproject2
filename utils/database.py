"""
Concerned with storing and retrieving books from  a list
- 'a' to add a new book
-'l' to list all books
-'r' to mark a book as read
-'d' to delete a book
-'q' to quit
"""
books = []


def a():
    books.append(dict(
        name=input("Enter book name:"),
        author=input("Enter book author:"),
        read=False
    ))


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


def d():
    user_input = input("What title would like to delete:")
    global books
    books = [book for book in books if book['name'] != user_input]

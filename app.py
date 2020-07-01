from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
-'l' to list all books
-'r' to mark a book as read
-'d' to delete a book
-'q' to quit
Your choice:"""


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != "q":
        if user_input == "a":
            name = input("Enter book name:")
            author = input("Enter book author:")
            database.a(name, author)
        elif user_input == "r":
            user_input = input("What title are you reading?: ")
            database.r(user_input)
        elif user_input == "l":
            books = database.get_all_books()
            for book in books:
                database.l(book)

        elif user_input == "d":
            user_input = input("What title would like to delete: ")
            database.d(user_input)
        elif user_input == "q":
            break
        else:
            print("Unknown command. Please try again!")
        user_input = input(USER_CHOICE)


menu()

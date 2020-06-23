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
    user_input = input(USER_CHOICE)
    while user_input != "q":
        if user_input == "a":
            database.a()
            database.save_to_csv()
            user_input = input(USER_CHOICE)
        elif user_input == "r":
            database.r()
            database.save_to_csv()
            user_input = input(USER_CHOICE)
        elif user_input == "l":
            database.l()
            user_input = input(USER_CHOICE)
        elif user_input == "d":
            database.d()
            database.save_to_csv()
            user_input = input(USER_CHOICE)
        elif user_input == "q":
            break
        else:
            print("Unknown command. Please try again!")
            user_input = input(USER_CHOICE)


menu()

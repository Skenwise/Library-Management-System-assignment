from DS_module import LMS_hastable
from system_module_class import User
from system_module_class import Book
from system_module_class import Library

# This is the main program for our Library Management System

print('Welcome to the Zcas Library Management System \n')

library = Library()

register = False

while register is False:
    authentification = input('\nEnter (1) to login or (2) to register: ')
    if authentification =='1':
        user_id = int(input("Enter your user ID: "))
        email = input("Enter your email address: ")
        register = library.is_register(user_id, email)
        print(register)
    elif authentification == '2':
        username = input("Enter your name: ")
        age = int(input("Enter your age: "))
        profession = input("Enter your profession: ")
        email = input("Enter your email address: ")
        library.register_new_user(username, age, profession, email)
        register = True
        print("Now you can continue\n")
    else:
        print("Wrong number entered!/Choose between 1 or 2!")

while True:
    print("\nOPERATION")
    print("-------------\n")
    print("1. Find a user in the library \n2. Display all the users in the library \n3. Add a book to the library \n4. Display all the book in the library \n5. Find a book in the library \n6. Borrow a book \n7. Check if a book is available \n8. Display recent library transaction \n9. return book \n10. Quit \n")
    choice = input("Choose the operation you want to execute: ")

    if choice == '1':
        user_id = int(input("Enter the ID of the user you want to find: "))
        user_found = library.find_user_library(user_id)
        print(user_found)

    elif choice == '2':
        library.display_list_of_user_library()

    elif choice == '3':
        bookTitle = input("Enter the tilte of the book: ")
        ISBN = input("Enter the ISBN code: ")
        library.add_book_to_library(bookTitle, ISBN)

    elif choice == '4':
        library.display_book_in_library()

    elif choice == '5':
        option = input("Do you have the ISBN of the book to find(yes/no): ")
        option.lower()
        if option == 'yes':
            ISBN = input("Enter the ISBN of the book: ")
            book_found = library.find_book_in_library(ISBN)
            print(book_found)

        elif option == 'no':
            print("This are the categories in which you can do your search: ")
            print("1. Title \n2. Author \n3. Year of publication \n4. editor")
            option1 = input("Enter the category for your search: ")

            if option1 == '1':
                search_key = "title"
            elif option1 == '2':
                search_key = "author"
            elif option1 == '3':
                search_key = "editor"
            else:
                print("This category is not available")

            search_value = input("Enter the value of the book in that category: ")
            book_found = library.library_binary_search(search_key, search_value)
            print(book_found)

        else:
            print("Wrong input enter yes or not!")

    elif choice == '6':
        user_id = int(input("Enter your user_id: "))
        email = input("Enter your email address: ")
        ISBN = (input("Enter the ISBN of the book: "))
        library.borrow_book(ISBN, user_id, email)

    elif choice == '7':
        ISBN = input("Enter the ISBN of the book: ")
        library.check_for_book_availability(ISBN)

    elif choice == '8':
        library.recent_book_transaction()

    elif choice == '9':
        ISBN = input("Enter the ISBN of the book: ")
        user_id = int(input("Enter your user ID: "))
        email = input("Enter your email address:  ")
        library.return_book(ISBN, user_id, email)

    elif choice == '10':
        break 

    elif choice == '11':
        user_id = int(input("Enter your user ID: "))
        library.is_register(user_id)
    else:
        print("Wrong number Entered! Choose between the available operations")

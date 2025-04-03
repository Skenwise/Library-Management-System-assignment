# this module contains different class for the different object use in our Library Management System

from DS_module import LMS_hastable
from DS_module import Stack
from algorithm import Algorithms
import random
from datetime import datetime
from database import db

# this class contains all action taken by a user in our system and the way he interact with it
class User:
    def __init__(self, name, age, profession, email):
        self.name = name
        self.age = age
        self.profession = profession
        self.email = email
        self.ID = random.randrange(1, 100, 1)
        self.register_user = [[] for _ in range(100)]

    def __str__(self):
        return f'User(name: {self.name}, Age: {self.age}, profession: {self.profession} and ID: {self.ID})'

# this class define different properties of a book and behavior
class Book:
    def __init__(self, title, ISBN):
        self.title = title
        self.ISBN = ISBN
        self.author = None
        self.year_published = None
        self.editor = None
        self.genre = None
        self.publisher = None
        self.language = None
        self.available = True
        self.borrower_id = None
        self.due_date = None
        self.list_of_book = LMS_hastable()

    def __repr__(self):
        return f"Book(book: {self.title}, by Author: {self.author}, Written in: {self.year_published}, ISBN: {self.ISBN})"

    def get_book_information(self):
        return f'Book(title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}\n Year Published: {self.year_published}, Editor: {self.editor}, Genre: {self.genre})'


    def add_book_information(self):
        print("TO REGISTER THE BOOK, ENTER IT DIFFERENT INFORMATION: ")
        self.author = input("Enter the name of the author: ")
        self.year_published = input("Enter the name of the year the book was Published: ")
        self.editor = input("Enter the name of the editor of the book: ")
        self.genre = input("Enter the name of the genre of the book: ")
        self.publisher = input("Enter the name of the publisher of the book: ")
        self.language = input("Enter the name of the language in which the book was written: ")

# this class handle library basic operation 

class Library:
    def __init__(self):
        self.name = "Zcas Library"
        self.capacity = 1000
        self.library_book = LMS_hastable()
        self.transaction = Stack()
        self.algorithm = Algorithms()
        self.category = 'title'
        self.register_user = [{} for _ in range(100)]
        self.database_connection = db.connect()

    def register_new_user(self, name, age, profession, email):
        user = User(name, age, profession, email)
        print(f'Your ID is : {user.ID}')
        self.register_user.insert(user.ID, ({'user ID': user.ID,'username': user.name}))
        if self.database_connection:
            cursor = self.database_connection.cursor()
            query = """
            INSERT INTO users(user_id, username, profession, age, email)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (user.ID, name, profession, age, email))
            self.database_connection.commit()
            print("Query executed!")
            cursor.close()

        print("The user has been successfully registered ! ")

    def is_register(self, user_id, email):
        filtered_library_users = [user for user in self.register_user if "user ID" in user]

        cursor = self.database_connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE email = %s AND user_id = %s", (email, user_id))
        return cursor.fetchone()[0] > 0 
        
        if not cursor.fetchone()[0] > 0:
            for user in filtered_library_users:
                print("stage of the for loop")
                if  user['user ID'] == user_id:
                    print("User register in the system")
                    print("if s")
                    return True

                else:
                    print('User not register')
                    print("please register")
                    return False

    def find_user_library(self, user_id):
        return self.register_user[user_id]

    def display_list_of_user_library(self):
        cursor = self.database_connection.cursor(dictionary=True)
        cursor.execute("SELECT user_id, username FROM users")
        database_library_user = []

        filtered_library_users = [user for user in self.register_user if "user ID" in user]
        database_library_user.extend(cursor.fetchall())
        cursor.close()

        print("Current user in the system")
        print(filtered_library_users)

        print("user in the database")
        print(database_library_user)

    def add_book_to_library(self, bookTitle, ISBN):
        book = Book(bookTitle, ISBN)
        book.add_book_information()
        self.library_book.insert_book(ISBN, book)
        print("Book has been added to the Library successfully. ")

    def display_book_in_library(self):
        self.library_book.display_list_of_book()

    def find_book_in_library(self, ISBN):
        book = self.library_book.find_book(ISBN)
        return book 

    def borrow_book(self, ISBN, user_id):
        book = self.find_book_in_library(ISBN)
        if self.is_register(user_id):
            user = self.find_user_library(user_id)
        time = datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S")

        if self.check_for_book_availability(ISBN):
            book['book'].available = False
            self.add_book_transaction(book, user, time)
            book['book'].borrower_id = user['user ID']
            print(f'{user['username']} has borrowed {book['book'].title}, {book['book'].ISBN}')
        else:
            print("Can't borrow this book/ Not Available")

    def check_for_book_availability(self, ISBN):
        book = self.find_book_in_library(ISBN)
        if book['book'].available:
            print("This book is available")
            return True
        else:
            print("This book is not available ")
            return False

    def add_book_transaction(self, book, user, time):
        message = {'borrowed book': book['book'].title, 'book code': book['book'].ISBN,'borower': user['username'], 'borrower_id': user['user ID'], 'borrowed on the ': time}
        
        self.transaction.push(message)

    def recent_book_transaction(self):
        self.transaction.print_stack()

    def sorting_library_book(self, category):
        filtered_library_book = [book for book in self.library_book if "book" in book]
        return self.algorithm.merge_sort(filtered_library_book, category)

    def library_binary_search(self, search_key, search_value):
        filtered_library_book = self.sorting_library_book(search_key)
        return self.algorithm.binary_search(filtered_library_book, search_key, search_value)




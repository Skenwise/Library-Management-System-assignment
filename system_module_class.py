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
        self.ISBN = int(ISBN)
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
        return f"Book(book: {self.title}, by Author: {self.author}, Written in: {self.year_published}, ISBN: {str(self.ISBN)})"

    def get_book_information(self):
        return f'Book(title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}\n Year Published: {self.year_published}, Editor: {self.editor}, Genre: {self.genre})'


    def add_book_information(self):
        print("TO REGISTER THE BOOK, ENTER IT DIFFERENT INFORMATION: ")
        self.author = input("Enter the name of the author: ")
        self.year_published = int(input("Enter the name of the year the book was Published: "))
        self.editor = input("Enter the name of the editor of the book: ")
        self.genre = input("Enter the name of the genre of the book: ")
        self.publisher = input("Enter the name of the publisher of the book: ")
        self.language = input("Enter the name of the language in which the book was written: ")

# this class handle library basic operation 

class Library:
    def __init__(self):
        self.name = "Zcas Library"
        self.capacity = 1009
        self.library_book = LMS_hastable()
        self.transaction = Stack()
        self.algorithm = Algorithms()
        self.category = 'title'
        self.register_user = [{} for _ in range(100)]
        self.database_connection = db.connect()
        self.load_book_from_database()
        self.load_user_from_database()
        self.load_transaction_from_database()

    def register_new_user(self, name, age, profession, email):
        user = User(name, age, profession, email)
        print(f'Your ID is : {user.ID}')
        self.register_user[user.ID] = {'user ID': user.ID, 'username': user.name}
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

    def load_user_from_database(self):
        cursor = self.database_connection.cursor()
        cursor.execute("SELECT user_id, username FROM users")
        users = cursor.fetchall()

        for user in users:
            user_id, username = user
            self.register_user[user_id] = {'user ID': user_id, 'username': username}
        cursor.close()

    def find_user_library(self, user_id):
        return self.register_user[user_id]

    def display_list_of_user_library(self):
        cursor = self.database_connection.cursor(dictionary=True)
        cursor.execute("SELECT user_id, username FROM users")
        database_library_user = []

        filtered_library_users = [user for user in self.register_user if "user ID" in user]
        database_library_user.extend(cursor.fetchall())
        cursor.close()
        for user in database_library_user:
            print(user)

    def add_book_to_library(self, bookTitle, ISBN):
        book = Book(bookTitle, ISBN)
        book.add_book_information()
        self.library_book.insert_book(ISBN, book)

        cursor = self.database_connection.cursor()
        
        cursor.execute(""" INSERT INTO books(isbn, title, year_published, editor, genre, publisher, language, available, author) VALUES (%s, %s, %s, %s, %s , %s, %s, %s, %s)""", (book.ISBN, book.title, book.year_published, book.editor, book.genre, book.publisher, book.language, book.available, book.author))
        
        self.database_connection.commit()
        cursor.close()
        print("Book added to the database")
        print("Book has been added to the Library successfully. ")

    def load_book_from_database(self):
        cursor = self.database_connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM books ")

        for row in cursor.fetchall():
            book = Book(title=row['title'], ISBN=str(row['isbn']))

            book.author = row['author']
            book.year_published = row['year_published']
            book.editor = row['editor']
            book.genre = row['genre']
            book.publisher = row['publisher']
            book.language = row['language']
            book.available = bool(row['available'])
            book.borrower_id = row['borrower_id']

            self.library_book.insert_book(book.ISBN, book)

    def display_book_in_library(self):
        self.library_book.display_list_of_book()

    def find_book_in_library(self, ISBN):
        ISBN = int(ISBN)
        book = self.library_book.find_book(ISBN)
        return book 

    def borrow_book(self, ISBN, user_id, email):
        book = self.find_book_in_library(ISBN)
        if self.is_register(user_id, email):
            user = self.find_user_library(user_id)
        time = datetime.now()

        if self.check_for_book_availability(ISBN):
            book['book'].available = False
            self.add_book_transaction(book, user, time)
            book['book'].borrower_id = user['user ID']
            print(f'{user['username']} has borrowed {book['book'].title}, {book['book'].ISBN}')

            # operation on the database

            cursor = self.database_connection.cursor()
            cursor.execute("UPDATE books SET available = FALSE, borrower_id = %s WHERE isbn = %s", (user_id, ISBN))
            print("Database change")
            self.database_connection.commit()

        else:
            print("Can't borrow this book/ Not Available")

    def return_book(self, ISBN, user_id, email):
        ISBN = int(ISBN)
        book = self.find_book_in_library(ISBN)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if not self.is_register(user_id, email):
            print("User not register ")
            return
        
        state = book['book'].available
        user = book['book'].borrower_id
        print(f"{state} and {user}")

        if not book['book'].available and book['book'].borrower_id == user_id:
            book['book'].available = True
            book['book'].borrower_id = None
            
            # operation on the database

            cursor = self.database_connection.cursor()
            cursor.execute("UPDATE books SET available = TRUE WHERE isbn = %s", (ISBN,))

            cursor.execute("""
                UPDATE transactions
                SET return_date = %s
                WHERE book_code = %s
                AND borrower_id = %s
                ORDER BY transaction_date DESC
                LIMIT 1
            """, (current_time, ISBN, user_id))

            self.database_connection.commit()

            return_message = {
                'returned book': book['book'].title,
                'book_code': ISBN,
                'returned by': self.find_user_library(user_id)['username'],
                'returned on': current_time
            } 
            self.transaction.push(return_message)

            print(f'{book['book'].title} (ISBN: {ISBN}, has been successfully returned)')
        else:
            print("Book can't be return!")

    def check_for_book_availability(self, ISBN):
        book = self.find_book_in_library(ISBN)
        if book['book'].available:
            print("This book is available")
            return True
        else:
            print("This book is not available ")
            return False

    def add_book_transaction(self, book, user, time):
        message = {'borrowed book': book['book'].title, 'book code': book['book'].ISBN, 'borrower': user['username'], 'borrower_id': user['user ID'], 'borrowed on the ': time}
        
        self.transaction.push(message)

        cursor = self.database_connection.cursor()
        cursor.execute("""
            INSERT INTO transactions (book_code, borrower_id, borrowed_book, borrower_name, transaction_date)
            VALUES (%s, %s, %s, %s, %s)
        """, (book['book'].ISBN, user['user ID'], book['book'].title, user['username'], time.strftime('%Y-%m-%d %H:%M:%S') ))
        self.database_connection.commit()
        cursor.close()

    def load_transaction_from_database(self):
        cursor = self.database_connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT book_code, borrower_id, borrowed_book, borrower_name, transaction_date, return_date
            FROM transactions
            ORDER BY transaction_date DESC 
        """)

        for row in cursor.fetchall():
            transaction_date = datetime.strptime(str(row['transaction_date']), '%Y-%m-%d %H:%M:%S')
            if row['return_date'] is not None:
                return_date = datetime.strptime(str(row['return_date']), '%Y-%m-%d %H:%M:%S')
            else:
                return_date = None

            transaction_data = {
                'borrowed book': row['borrowed_book'],
                'book code': row['book_code'],
                'borrower': row['borrower_name'],
                'borrower id': row['borrower_id'],
                'borrowed on': transaction_date.strftime("%A, %Y-%m-%d %H:%M:%S"),
                'returned on': return_date.strftime("%A, %Y-%m-%d %H:%M:%S") if return_date is not None else 'None'
            }

            self.transaction.push(transaction_data)
        cursor.close()

    def recent_book_transaction(self):
        self.transaction.print_stack()

    def sorting_library_book(self, category):
        filtered_library_book = [book for book in self.library_book if "book" in book]
        return self.algorithm.merge_sort(filtered_library_book, category)

    def library_binary_search(self, search_key, search_value):
        filtered_library_book = self.sorting_library_book(search_key)
        return self.algorithm.binary_search(filtered_library_book, search_key, search_value)




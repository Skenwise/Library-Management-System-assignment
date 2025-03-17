# this module contains different class for the different object use in our Library Management System

from DS_module import LMS_hastable
import random

# this class contains all action taken by a user in our system and the way he interact with it
class User:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession
        self.ID = random.randrange(1, 100, 1)
        self.register_user = [[] for _ in range(100)]
        self.list_of_book = LMS_hastable()

    def __str__(self):
        return f'User(name: {self.name}, Age: {self.age}, profession: {self.profession} and ID: {self.ID})'
    
    def register_new_user(self):
        print(f'Your ID is : {self.ID}')
        self.register_user.insert(self.ID, ([self.ID, self.name]))
        return "The user has been successfully registered ! "


    def is_register(self):
        ID = int(input("Enter your ID: "))
        name = input("Enter your name: ")
        for user in self.register_user:
            if  ID in user or name in user:
                print("User register in the system")
                return True
        else:
            print('User not register')
            return False

    def borrow_book(self):
        return False

    def look_for_a_book(self):
        return False

    def buy_a_book(self):
        return False


# this class define different properties of a book and behavior
class Book:
    def __init__(self, title):
        self.title = title
        self.ISBN = None
        self.author = None
        self.year_published = None
        self.editor = None
        self.genre = None
        self.publisher = None
        self.language = None
        self.availability = None
        self.borrowe_id = None
        self.due_date = None


    def __str__(self):
        return f'Book(title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}\n Year Published: {self.year_published}, Editor: {self.editor}, Genre: {self.genre})'


    def add_book_information(self, title):
        print("TO REGISTER THE BOOK, ENTER IT DIFFERENT INFORMATION: ")
        self.author = input("Enter the name of the author: ")
        self.year_published = input("Enter the name of the year the book was Published: ")
        self.editor = input("Enter the name of the editor of the book: ")
        self.genre = input("Enter the name of the genre of the book: ")
        self.publisher = input("Enter the name of the publisher of the book: ")
        self.language = input("Enter the name of the language in which the book was written: ")
  
# this class handle library basic operation 

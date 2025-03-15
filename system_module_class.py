# this module contains different class for the different object use in our Library Management System

import random

# this class contains all action taken by a user in our system and the way he interact with it
class User:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession
        self.ID = random.randrange(1, 10000, 1)
        self.register_user = {}

    def is_register(self, ID):
        if  ID in register_user:
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
        self.name = title
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


    def add_book_information(self, title):
        print("TO REGISTER THE BOOK, ENTER IT DIFFERENT INFORMATION: ")
        

    

# this class handle library basic operation 

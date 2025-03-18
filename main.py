from DS_module import LMS_hastable
from system_module_class import User
from system_module_class import Book

# implementation of th inheritance principle

userName = input("Enter your name: ")
age = int(input("Enter your age: "))
profession = input("Enter your profession: ")

user1 = User(userName, age, profession)
user1.register_new_user()
table = LMS_hastable()
bookTitle = input("Enter the title of the book: ")
ISBN = input("Enter ISBN: ")

book = Book(bookTitle)
book.add_book_to_library(bookTitle, ISBN)


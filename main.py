from DS_module import LMS_hastable
from system_module_class import User
from system_module_class import Book

# implementation of th inheritance principle

userName = input("Enter your name: ")
age = int(input("Enter your age: "))
profession = input("Enter your profession: ")
bookTitle = input("Enter the title of your book: ")

user1 = User(userName, age, profession)
table = LMS_hastable()
book = Book(bookTitle) 

ISBN = input("Enter the ISBN of your book: ")
capacity = int(input("Enter the capacity of the table: "))
table_capacity = table.set_table_capacity(capacity)
index = table.hashFunction(ISBN)
print(index)
print(book)
print(user1)

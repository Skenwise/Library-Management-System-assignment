from DS_module import LMS_hastable
from system_module_class import User
from system_module_class import Book

# implementation of th inheritance principle

userName = input("Enter your name: ")
age = int(input("Enter your age: "))
profession = input("Enter your profession: ")

user1 = User(userName, age, profession)
user1.register_new_user()
user1.is_register()
table = LMS_hastable()



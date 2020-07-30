from database import Database
from admin import Admin
from user import User

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9583298#overview

# the Saveable is almost a 100% Interface as it forced the subclasses user and admin to have to_dict method.
# it also contains extra common subclasses functionalities like the option to save in DB with the save method. Because of this is not a 100% interface class

a = Admin('Tom', '1234', 5)
b = User('Dana', '4321')

users = [a, b]

for user in users:
    user.save()

for user in users:
    print(Database.find(lambda x : x['username'] == user.username))

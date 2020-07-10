
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477762#questions


from collections import namedtuple

account = ('balance', 1238.67)
# you use this to simulate a class that contains 2 self variable. Its a shorter way to defining a new type that is a tuple, it has a name, and 2 variables.
Account = namedtuple('Account', ['name', 'amount'])

account = Account('savings', 23567.45)

print(account.name)

print(account.name)
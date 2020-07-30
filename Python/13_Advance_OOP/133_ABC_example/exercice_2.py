
# https://www.udemy.com/course/the-complete-python-course/learn/quiz/4427874#overview

from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    def hungry(self):
        print(f'I want to eat {self.get_favourite_food()}!')

    @abstractmethod
    def get_favourite_food(self):
        pass

    def __repr__(self):
        return (f'This is the print for Animal class')

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    @classmethod # if this in not a class methond, and i have self instead of cls parameter, it still works. Not sure why we need this method to be classmethod
    def get_favourite_food(cls):
        return 'ribs'

    def __repr__(self):
        return (f'This is the print for Dog class, name {self.name}')

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    @classmethod
    def get_favourite_food(cls):
        return 'fish'

a = Dog('Tim')
a.hungry()
print(a) # will use the Dog class repr dunder

b= Cat('Miau')
b.hungry()
print(b) # as it does not have a repr dunder it will use the one from Animal class
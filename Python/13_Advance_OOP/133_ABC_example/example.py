
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9583284#overview

from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    def walk(self):
        print ('Walking...')

    @abstractmethod # this will force/check that all classes tha twill inherit Animal will have this method defined also
    def num_legs(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 4

class Monkey(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 2

#a = Animal() # this will not work anymore as it contains abstract methods that are there as a rule and not to be used direcly anymore
#print(a.num_legs())

dog = Dog('Billy')
print(dog.num_legs())

dog = Monkey('Jimmy')
print(dog.num_legs())

# OR

animals = [Dog('Tom'), Monkey('Timmy')]
for a in animals:
    print (isinstance(a, Animal))# a in an instance of Animal but contains also the functionalities from either Dog or Monkey classes
    print(a.num_legs())
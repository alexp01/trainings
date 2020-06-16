# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9417826#overview

class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)

# you use a static method when you don't need the full class content buut just that method. You don't also need the self properties also.
class Boo:
    @staticmethod
    def hi():
        print (f'This is a metode that does not depend on the class or self, and does not need paramaters')

first_class = Foo()
first_class.hi()

second_class = Boo()
second_class.hi()
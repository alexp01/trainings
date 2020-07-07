
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445604#questions

class Generate100Numbers: # This is called a Iterator class, and its behaving identically as a Generator
    def __init__(self):
        self.number = 1

    def __next__(self):
        if self.number <= 4:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

my_gen = Generate100Numbers()

print(my_gen.number)
print(next(my_gen)) # this prints 1 as we first return the number and then we increment it
# print (my_gen.__next__()) # this is identical to : print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

# An Iterator can not be used for ;
# for i in my_gen , as this will give an error
# or sum(my_gen) or list(my_gen)

# Not all Iterators are generators, as your next method can return an element from a list, for example and iterate through its elements
# Example:

class Give5valuesFromList: # this is also an Iterator but not an generator
    def __init__(self):
        self.list = [0, 1, 2, 3, 4]
        self.i = 0

    def __next__(self):
        if self.i < len(self.list):
            current = self.list[i]
            self.i += 1
            return current
        else:
            raise StopIteration()

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445610#questions

class Generate100numbers:
    def __init__(self):
        self.number = 1

    def __next__(self):
        if self.number <= 100:
            number = self.number
            self.number += 1
            return number
        else:
            raise StopIteration()

    def __iter__(self):
        return self

nr = Generate100numbers()

print (sum(nr))

for i in nr: # this will not print anything, as the class already runned once until 100, because of the sum function, that will use the iter dunder method to loop 100 types in the next dunder class
    print(i)

# this will work as we call again the class and we reinitialize self.number = 1
for i in Generate100numbers():
    print(i)

my_numbers = [x for x in [1,2,3,4,5]]
print (my_numbers) # the var contains a copy of that list

my_generator_numbers = (x for x in [1,2,3,4,5]) # This is not a tuples with list variables, but a generator
# we can call this a : generator comprehension
print (next(my_generator_numbers)) # that why i can do next(var)
# this var does not have a copy of that list, but it can acces each value one by one

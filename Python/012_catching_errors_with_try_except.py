# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445260#questions

class Car:
    def __init__(self, model, type):
        self.model = model
        self.type = type

    def __repr__(self):
        return (f' Car:{self.type}, Model:{self.model}')

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'The parameter that you gave if of type: {car.__class__.__name__}. Please give a Cars object type')
        self.cars.append(car)

ford = Garage()
fiesta = Car('fiesta', 'ford')

#ford.add_car(fiesta)
#print (ford.cars[0])

try:
    ford.add_car('Fiesta')
except TypeError:
    print('We catched a TypeError so the program will stop here, and will not raise the Error from add_car')
# We prefer to catch and antipicipate a posible error, so that the used will not see that error when the code will run
except ValueError:
    print('Something is not good')
finally:
    print (f'The garage now has {len(ford)} cars')
# 'finally' will always execute even if we catch or not any errors.

# example
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
class Cars:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return (f'The car {self.model} was build by {self.make}')

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_cars(self, car):
        if not isinstance(car, Cars): # isinstance is comparing to see if what you give as the variable car is of type Cars, that is an object. If car is not an object the ocndition is false
            raise TypeError(f"Tried to add a '{car.__class__.__name__}' to the Garage, but you can only add car objects")
            # the car.__class__ is Cars , the name of the class. And then __name__ will give you the type of that class name, in our case a string.
        self.cars.append(car)
            # This list will contain on each position a Car object of Cars class.

ford = Garage()

# ford.add_cars('Fiesta')
# this will raise the typeError as you give the add_cars a str and not a Car class object

car = Cars('Ford', 'Fiesta')
ford.add_cars(car)

car = Cars('Ford', 'Focus')
ford.add_cars(car)

# now it works as you give to add_cars an object of Cars class typpe
print(ford.cars[0])
print(ford.cars[1])
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445250#questions#

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_cars(self):
        raise NotImplementedError ('This function was not yet finished')

ford = Garage()
ford.cars.append('Focus')

print(ford.cars[0])

ford.add_cars()
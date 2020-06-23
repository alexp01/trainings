
# https://www.udemy.com/course/the-complete-python-course/learn/quiz/4902660#overview

# All class should hav a repr and str functions


movies = ['Matrix', 'Tarzan']
print (movies.__class__)

print ('Hello'.__class__)

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self):
        return f'\nThe cars name is : {self.cars}'

    def __str__(self):
        return f'\nWe have {len(self)} in total'

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
ford.cars.append('Ka')

print (ford.cars)
print(len(ford))

for car in ford:
    print(car)

# here we use the str function
print(ford)

# scope: To +,-,* and \ by just using the sum method.
# https://www.udemy.com/course/the-complete-python-course/learn/quiz/4424524#questions/11460302
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/10185706#questions/11460302

from Addition import Addition

class Calcultor_class:

    def __init__(self, operation, a, b):
        self.operation = operation
        self.value1 = int(a)
        self.value2 = int(b)
        self.total = 0

    def __repr__(self):
        if self.operation == 'a':
            self.Add_op()
            return (f'Your Adition results i {self.value1} + {self.value2} = {self.total}\n')
        elif self.operation == 'm':
            self.multi_op()
            return (f'Your Multiplication result is {self.value1} * {self.value2} = {self.total}\n')
        elif self.operation == 's':
            self.subs_op()
            return (f'Your Division result is {self.value1} - {self.value2} = {self.total}\n')
        elif self.operation == 'd':
            if self.value2 == 0:
                return ('You have to give a non zero integer number')
            else:
                self.division_op()
                return (f'Your Division result is {self.value1} \ {self.value2} = {self.total}\n')

    def Add_op(self):
        self.total = Addition_operation.add(self.value1, self.value2)
        print (self.total)

    def multi_op(self):
        self.total = self.value1
        for i in range(1, self.value2):
            self.total = self.total + Addition_operation.add(0, self.value1)
            i += 1

    def subs_op(self):
        for i in range(0, self.value1):
            if Addition_operation.add(self.value2, i) == self.value1:
                self.total = i
            i += 1

    def division_op(self):
        division_by = 0
        for i in range(0, self.value1+1):
            division_by = Addition_operation.add(division_by, self.value2)
            if division_by <= self.value1:
                i += 1
            else:
                break
            self.total = i

option = 'a'
while option != 'q':
    option = input (""" Please give an operation
    a for Addition
    s for Substraction
    m for Multiplication
    d for Devision    
    -> To Exit please press : q
    Operation : _""")

    if option == 'q':
        print('\n You left the Calculator')
        quit()

    Addition_operation = Addition()

    a, b = input ("Please give 2 numbers, devided by comma, and no spaces:_").split(',')
    call_calculator = Calcultor_class(option, a, b)
    print (call_calculator)




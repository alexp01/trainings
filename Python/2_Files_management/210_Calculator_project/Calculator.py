from Addition import Addition

class Calcultor_class:

    def __init__(self, operation, a, b):
        self.operation = operation
        self.value1 = a
        self.value2 = b
        self.total = 0

    def Add_op():
        self.total = Addition_operation.add(self.value1, self.value2)
        print (self.total)

    def __repr__(self):
        if self.operation == 'a':
            return (f'Your Adition results is {self.value1} + {self.value2} = {self.total}\n')


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
    print (Addition_operation.add(3,4))

    a, b = input ("Please give 2 numbers, devided by comma, and no spaces").split(',')
    call_calculator = Calcultor_class(option, a, b)
    print (call_calculator)




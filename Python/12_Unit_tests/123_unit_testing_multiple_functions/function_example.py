from typing import Union

def calculate(devidend: Union[int, float], division: Union[int,float]): # the values that each parameter takes is either a int or a float
    if division == 0:
        raise ValueError('You can not devide by zero')
    return devidend / division

def multiply(*args: Union[int,float]):
    if len(args) == 0:
        raise ValueError('At least 1 argument must be given')
    total = 1
    for arg in args:
        total *= arg
    return total
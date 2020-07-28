
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9490872#overview

tuple1 = (1, 3, 4, 5, 7, 9)

def sum_all(a1, a2, a3, a4, a5, a6):
    return print(a1+a2+a3+a4+a5+a6)

sum_all(*tuple1)# this will uppack tuples1 and give it as arguments to the sum_all parameters

dict1 = {'a1': 1, 'a2': 3, 'a3': 3, 'a4': 4, 'a5': 5, 'a6': 6}

def sum_all2(a1, a2, a3, a4, a5, a6):
    return print(a1+a2+a3+a4+a5+a6)

sum_all2(**dict1) # this will unpack the dict and give the values of each elements as arguments
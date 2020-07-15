
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/18514856#questions

def print_hello():
    print('Hello')

def main_func(func):
    print ('before the func call')
    func()
    print ('after')

# main_func(5) - it does not work as 5 is not a function
main_func(lambda : 5) # this works as the arguments is a function with no parameters, and that returns 5

# main_func(print_hello()) # this will not work as funct() will return None, as its the default return value

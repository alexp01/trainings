import functools

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9490860#overview
# a better solution for the issues that are documented bellow can be seed in example3.py

users = {'name' : 'Pepe', 'right': 'admin'}

def check_user_permission(func):
    """
    This is the doc for the decorator
    """
    @functools.wraps(func) # this will just keep the name and others(like doc comments) from the origina lmy_function funct that is wrapped in this secure_func function
    def secure_func():
        if users.get('right') == 'admin':
         return func()
    return secure_func

@check_user_permission
def my_function():
    """
    This is the doc for my_function
    """
    return 'Admin pass is Toto'

@check_user_permission
def another():
    pass

my_secure_function = check_user_permission(my_function)
print (my_secure_function())

print(my_function.__name__) # this will now print the good func name
print(another.__name__) # this will now print the good func name, af secure_func is a wrapper only for my_function


print(my_function.__doc__) # this will now print the good func name
print(check_user_permission.__doc__) # this will print the good doc comment from my_function
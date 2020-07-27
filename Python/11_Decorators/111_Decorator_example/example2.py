
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9490860#overview

users = {'name' : 'Pepe', 'right': 'admin'}

def check_user_permission(func):
    """
    This is the doc for the decorator
    """
    def secure_func():
        if users.get('right') == 'admin':
         return func()
    return secure_func

@check_user_permission # with this you 'hide' this function, as it actually called by your decorator above. my_function is replaced in a way by secure_funct
def my_function(): # you will not have access to this function independently, but only thru your decorator
    """
    This is the doc for my_function
    """
    return 'Admin pass is Toto'

@check_user_permission
def another():
    pass

my_secure_function = check_user_permission(my_function)
print (my_secure_function())

print(my_function.__name__) # will print secure func
print(my_function.__name__) # will print secure func also
# this might be a problem both of this function point to the same funct inside the decorator
# even if they do completly different things

print(my_function.__doc__) # this will not print nothing, as it hidden and will be replaced by secure_func
print(check_user_permission.__doc__) # this will print the doc comments from the decorator function
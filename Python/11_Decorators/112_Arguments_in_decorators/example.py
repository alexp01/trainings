import functools

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9490868#overview
# this solution works for the my_function func but not for the another func. We need mo more generic solution for our decorator

users = {'name' : 'Pepe', 'right': 'admin'}

def check_user_permission(func):
    @functools.wraps(func)
    def secure_func(level): # our wrapper in the decorator accepts now the my_function argument and it givesi t bank in the return also
        if users.get('right') == 'admin':
         return func(level)
    return secure_func

@check_user_permission
def my_function(level):
    return f'Admin for  pass for {level} is Toto'

@check_user_permission
def another():
    pass

my_secure_function = check_user_permission(my_function)
print (my_secure_function(3))

# but it will not work for the onother function, as that one foes not have parameters
#my_secure_function2 = check_user_permission(another)
#print (my_secure_function2(3))
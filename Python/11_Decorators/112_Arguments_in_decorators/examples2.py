import functools

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9490870?start=225#overview

users = {'name' : 'Pepe', 'right': 'admin'}

def user_has_permision(access_level):
    def check_user_permission(func):
        @functools.wraps(func)
        def secure_func(level): # our wrapper in the decorator accepts now the my_function argument and it givesi t bank in the return also
            if users.get('right') == 'admin':
             return func(level)
        return secure_func
    return check_user_permission

@user_has_permision('admin')
def my_function(level):
    return f'Admin for  pass for {level} is Toto'

my_function = user_has_permision('admin')(my_function)
print(my_function())

# ANother way to call it is:
#check_user_permission = user_has_permision('admin')
#my_function = user_has_permision(my_function)
#print (my_function('movies'))
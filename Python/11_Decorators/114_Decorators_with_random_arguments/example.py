import functools

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9490874#overview

users = {'name' : 'Pepe', 'right': 'admin'}

def user_has_permision(access_level):
    def check_user_permission(func):
        @functools.wraps(func)
        def secure_func(*args, **kwargs): # our wrapper in the decorator accepts now the my_function argument and it givesi t bank in the return also
            if users.get('right') == 'admin':
             return func(*args, **kwargs)
        return secure_func
    return check_user_permission

@user_has_permision
def my_function(level):
    return f'Admin for  pass for {level} is Toto'

@user_has_permision
def another():
    pass

print(my_function('movies'))
print(another())


# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9490858#overview
# A decorator is a function that is running inside another function and return a function

users = {'name' : 'Pepe', 'right': 'admin'}

#def check_user_permission(func): # this is a Decorator, a simpler implementation
#    if users.get('right') == 'admin':
#        return func
#    raise RuntimeError

#the new way of writing decorators:
def check_user_permission(func): # this is a Decorator#    def secure_func():
    def secure_func():
        if users.get('right') == 'admin':
         return func() # we now return the return of my_function
    return secure_func # because we return a function we still need to do print (my_secure_function()) with () for the called func

def my_function(): # This solution is not the best as you can just run this function independently and have access to the admin pass
    return 'Admin pass is Toto'

my_secure_function = check_user_permission(my_function)
print (my_secure_function())
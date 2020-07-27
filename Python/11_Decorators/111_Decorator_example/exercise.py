
# https://www.udemy.com/course/the-complete-python-course/learn/quiz/4427866#overview

users = {'name' : 'Pepe', 'right': 'admin'}

def check_user_permission(func):
    def secure_func():
        if users.get('right') == 'admin':
            return func()
        else:
            raise PermissionError ('You are not the admin to perform deletion')
    return secure_func

def delete_table():
    return 'Performs Table deletion '

my_secure_function = check_user_permission(delete_table)
print (my_secure_function())
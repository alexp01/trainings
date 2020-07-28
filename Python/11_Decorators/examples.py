
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9490872#overview

x = {'a': 1, 'b': 3, 'c': 6}

def sum_all(a,b,c):
    return a+b+c
print(sum_all(b = 2, c = 1, a = 4))
#OR:

print(sum_all(**x))

# another example:
def show_dict_content(**kwargs): # will take any number of keyword name arguments
    for k,v in kwargs.items():
        print (f'For {k} we have {v}.')

show_dict_content(username='Toto', user_id='1234')

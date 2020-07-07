
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445618#questions

def starts_with_r(friend):
    return friend.startswith('R')

friends = ['Rolf', 'Anna', 'Roul', 'John', 'Robin']
start_with_r_variable = filter(starts_with_r, friends) # function that returns True/False

print ('Output of first solution: ')
print (next(start_with_r_variable))
print (next(start_with_r_variable))
print (next(start_with_r_variable))
#print (next(start_with_r_variable)) # This will give a StopIteration, as there are no more values in the Iterator

# All above is equivalent to :

start_with_r_variable_2 = filter(lambda x : x.startswith('R'), friends)
print ('Output of second solution: ')
print (next(start_with_r_variable_2))
print (next(start_with_r_variable_2))
print (next(start_with_r_variable_2))
#print (next(start_with_r_variable_2))

# Also this is identical :

start_with_r_variable_3 = (f for f in friends if f.startswith('R'))

start_with_r_variable_3 = filter(lambda x : x.startswith('R'), friends)
print ('Output of third solution: ')
print (next(start_with_r_variable_3))
print (next(start_with_r_variable_3))
print (next(start_with_r_variable_3))
#print (next(start_with_r_variable_3))

# Also this is identical :

def my_custom_function(func, iterable):
    for i in iterable:
        if func(i):
            yield i

start_with_r_variable_4 = my_custom_function(lambda x : x.startswith('R'), friends)
print ('Output of forth solution: ')
print (next(start_with_r_variable_4))
print (next(start_with_r_variable_4))
print (next(start_with_r_variable_4))


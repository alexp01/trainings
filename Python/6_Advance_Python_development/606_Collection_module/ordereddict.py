
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477762#questions

from collections import OrderedDict # this metod starts with big O

dict1 = OrderedDict() # this will keep the add order in the Dict
#dict1 = {}
dict1['Anna'] = 17
dict1['Tom'] = 18
dict1['Bob'] = 16
# Whats strange is that even without that OrderedDict the order is still the creation order.
print (dict1)

dict1.move_to_end('Tom')
print (dict1)

dict1.move_to_end('Bob', last=False) # with last=false as a parameter, we actually revers teh order, and add it to the start of the list
print (dict1)

dict1.popitem() # removed 1 element from the end
print (dict1)

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477736#questions

friends = [{'name' : 'John', 'age': 34}]
print (id(friends))
friends[0]['age'] = 40 # behind this happens : x.__additem__(self,age) and this will not create something new in the memory
print (id(friends))

friends3 = [{'name' : 'John', 'age': 34}]
print (id(friends))
# even if the value content is the same as friends3, it is seen as a different value and stores in another memory location

# Mutable means that the value stores in memory can be updated and still keep its memory possition
# Most of the elements are mutable, besides int, float, tuples and strings

x = 6
print (id(x))
x += 1 # behind this happens : x.__add__(self,1) and this will create something new in the memory
print (id(x))
# the stored value 6 can not be updated as its already stored as a 6
# int is not a mutable element

friends2 = ['John', 'Anna']
print (id(friends2))
friends2.append('Rick')
print (id(friends2))
# lists are mutable


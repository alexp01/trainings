
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477762#questions

from collections import Counter

# How to use Counter method:
temperature = [20.5, 23.0, 27.5, 19.0, 20.5, 33.0]
how_many_of_temp = Counter(temperature)
print (how_many_of_temp[20.5]) #

# another example:
dict1 = {'hello' : 3, 'hi' : 10}
print(Counter(dict1)['hi']) # Its not actually useful in dict case, as you can just acces it without the Counter method. like : dict['hi']




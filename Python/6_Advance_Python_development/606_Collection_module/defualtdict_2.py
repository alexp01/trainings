
# # https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477762#questions

from collections import  defaultdict

friends = ['Tom', 'Bob', 'Anna']

working_place_for_friend = [('Bob', 'IBM'), ('Bill', 'Apple')]

# I want to have something like:
# dict_of_friend_and_work_place = [{'Bob' : 'IBM'}, {'Bill': 'Apple'}]

default_work_place = 'Freelancer'
dict_of_friend_and_work_place = defaultdict(lambda : default_work_place) # we can not just give the string as default parameter as the defaultdict needs a function as first argument

for friend in working_place_for_friend:
    dict_of_friend_and_work_place[friend[0]] = friend[1]

print (dict_of_friend_and_work_place)
print (dict_of_friend_and_work_place['Bob'])
print (dict_of_friend_and_work_place[friends[1]]) # this is Bob, that exists in the Dict as a key
print (dict_of_friend_and_work_place[friends[0]]) # this is Tom that does not exist as key in my Dict
# as Tom does not exist in the Dict, when we aceess the key Tom, we assign it to the Dict but as value we give the default Dict vaue : Freelancer

print (dict_of_friend_and_work_place)
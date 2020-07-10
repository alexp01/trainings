
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477762#questions

from collections import defaultdict

places_lived = [
    ('Smith', 'London'),
    ('Anna', 'London'),
    ('Anna', 'Berlin'),
    ('Bob', 'Paris')
]

dict_of_lived_places = {}
for line in places_lived:
    if line[0] not in dict_of_lived_places:
        dict_of_lived_places[line[0]] = []
    dict_of_lived_places[line[0]].append(line[1])

print(dict_of_lived_places)

# To avoid assigning an empty list inside the for you can do :

dict_of_lived_places2 = defaultdict(list) # this returns [], an empty list
for line in places_lived:
    dict_of_lived_places2[line[0]].append(line[1]) # in case we want to append to a non existing list, we will get as default the empty list, that can be used to append an a list element

#dict_of_lived_places2.default_factory = None

print(dict_of_lived_places2)
print(dict_of_lived_places2['Anna'])
print(dict_of_lived_places2['Tom']) # this not give an error, as it will have [] as default value

# to get an error for Tom you have to do this:
# dict_of_lived_places2.default_factory = None
# print(dict_of_lived_places2['Tom'])
# This Time you will get a keyerror as tha tkey does not exist in that list

# dict_of_lived_places2.default_factory = int ... you can overwrite the defalt element to something else, like a int 
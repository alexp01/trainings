
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445286#questions

import json

file = open('data_json.txt', 'r')
json_content = json.load(file)
file.close()

print (json_content["friends"][0])
print (json_content["friends"][0]["age"])
print (json_content)

cars= [
    {'type' : 'Skoda', 'price' : '24000'},
    {'type' : 'Fiat', 'price' : '15000'}
]

# this will take a dict as input and add it as json in a file
file2 = open('car_json.txt', 'w')
json.dump(cars, file2)
file2.close()

with open('car_json.txt', 'w') as f:
    json.dump(cars, f)

string1 = '[{"name" : "Fiat", "price" : "20"}]'
# this string that contains a dictionary type format will be transformed into a json type
json_type_string = json.loads(string1)
print(json_type_string[0]["price"])

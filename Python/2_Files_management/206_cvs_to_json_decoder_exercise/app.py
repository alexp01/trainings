
# https://www.udemy.com/course/the-complete-python-course/learn/quiz/4415674#questions
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9968572#questions

import json

cvs_file = open('cvs_data.txt', 'r')
cvs_content = cvs_file.readlines()
cvs_file.close()
lines = [line.strip() for line in cvs_content]

dict1 = []
for line in lines:
    line_content = [go_big.capitalize() for go_big in line.split(',')]
    dict_keys = ['Country', 'Capital', 'Population']
    dict1.append(dict(zip(dict_keys, line_content)))
print (dict1)

json_file = open ('json_data.txt', 'w')
json.dump(dict1, json_file)
json_file.close()

# This is the solution from the training: Its much simpler and better
#import json
#
#json_list = []  # store the converted json data for each line
#csv_file = open('csv_file.txt', 'r')
#
#for line in csv_file.readlines():
#    club, city, country = line.strip().split(',')  # first get rid of the \n and then split with ','
#    data = {
#        'club': club,
#        'city': city,
#        'country': country
#    }
#    json_list.append(data)
#
#csv_file.close()

#json_file = open('json_file.txt', 'w')
#json.dump(json_list, json_file)  # write json data to a file
#json_file.close()

# https://www.udemy.com/course/the-complete-python-course/learn/quiz/4415674#questions

import json

cvs_file = open('cvs_data.txt', 'r')
cvs_content = cvs_file.readlines()
lines = [line.strip() for line in cvs_content]

for x in range(0,len(lines)-1):
    line = lines.split(',')
    x += 1

print (cvs_content)
print(lines)
cvs_file.close()
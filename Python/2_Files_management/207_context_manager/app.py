
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445292#questions

import json

with open('data.txt', 'r') as file:
    text = file.readlines()
    print(text)

# with is called a context manager. If some functions are defined in a particular way they can be used with "with" and this will execute something at the end of the block. In our case a close file.
# so the "with" has predefined already the execution of file close at the end of the block
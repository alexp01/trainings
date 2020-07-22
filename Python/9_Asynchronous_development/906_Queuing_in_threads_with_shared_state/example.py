
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9489768#overview

from threading import  Thread

counter = 0

def generate_numbers():
    global counter
    counter += 1
    print (f'The counter value is {counter}')
    print('------------')

# The case that contains the issue:
for x in range(10):
    generate_numbers()
    t = Thread(target=generate_numbers)
    t.start()

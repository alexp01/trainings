
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9489764#overview
# Example to show that different threads with shared state can be dangerous in particular cases
# the global variable is our shared state in this example

import time
import random
from threading import  Thread

counter = 0

def generate_numbers():
    global counter
    counter += 1
    time.sleep(random.random())
    print (f'The counter value is {counter}')
    time.sleep(random.random())
    print('------------')

# this code executes well, as its fast. The time it takes for the for loop to execute again, the thread that calls the function will already be done
# so you will sea 10 times the 2 prints from the function
#for x in range(10):
    #t = Thread(target=generate_numbers)
    #t.start()

# even the above example can cause issues, if the computer will run others things in paralele with the execution of this code


# The case that contains the issue:
for x in range(10):
    generate_numbers()
    t = Thread(target=generate_numbers)
    time.sleep(random.random())
    t.start()
# the printed lines will not fallow the rule from above
# due to the sleep we have several threads that start to execute the function, but they are blocked for a while by the sleep. They they re-run and increment with +1 2 times, and then they print

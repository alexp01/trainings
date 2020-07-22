
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9489744#overview
# threads runned in paralel are usefull when 1 of them waits for something, like user input. The time that is lost in waiting can be given to the other function instead
# having 2 complex function, in paralele threads, is not usefull as they will take even more time, due to the constant switch and status storage

import time
from threading import Thread

def ask_user(): # its duration depends on how fast te user value is inserted, so min 1-2 secs
    start = time.time()
    get_user = input('Give a user name:_')
    print(f'Hello : {get_user}')
    print(f'The ask_user function took : {time.time() - start}')


def complex_calculation(): # it takes 8 secs
    start = time.time()
    print('Starting complex_calculation function')
    complex_calc = [x**2 for x in range(30000000)]
    print(f'The complex_calculation function took : {time.time() - start}')


start = time.time()
ask_user()
complex_calculation()
print(f'The main single Thread that executes the 2 functions took : {time.time()-start}') # both function take 14 secs

thread2 = Thread(target=complex_calculation)
thread3 = Thread(target=ask_user)

start = time.time()
thread2.start()
thread3.start()

thread2.join() # this is call a blocking operation
thread3.join() # they will make the main thread wait, that calls each function, until thread 2 and 3 will finish
# What i don't understand is the fact that the threads 2 and 3 will start only after the thread 1 is finished, as python runs line by line.

print(f'Running 2 threads in paralele each for 1 function took : {time.time()-start}') # instead of 14 now it takes 12 secs



#Give a user name:_a
#Hello : a
#The ask_user function took : 1.3730871677398682
#Starting complex_calculation function
#The complex_calculation function took : 12.613326787948608
#The main single Thread that executes the 2 functions took : 14.35991621017456
#Starting complex_calculation function
#Give a user name:_a
#Hello : a
#The ask_user function took : 0.9234542846679688
#The complex_calculation function took : 12.27024531364441
#Running 2 threads in paralele each for 1 function took : 12.648319005966187



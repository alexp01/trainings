
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9489754#overview
# this does not work for me. After i start the process, the sk_name is called twice. No idea why.
# Even the code from the training is behaving like this. But in the training it seems to work.
# it might be related to the windowos OS comment i added below. The person from the training was using a MAC

import time
from multiprocessing import Process

def ask_user():
    start = time.time()
    get_user = input('Give a user name:_')
    print(f'Hello : {get_user}')
    print(f'The ask_user function took : {time.time() - start}')


def complex_calculation():
    start = time.time()
    print('Starting complex_calculation function')
    complex_calc = [x**2 for x in range(20000000)]
    print(f'The complex_calculation function took : {time.time() - start}')

#this will be run in the main thread
start = time.time()
ask_user()
complex_calculation()
print(f'The main single Thread that executes the 2 functions took : {time.time()-start}')

# this will run that function is a new process with 1 thread
process = Process(target=complex_calculation)
if __name__ == "__main__": # this is just if you run the code on windows
    process.start()
    start = time.time()
    #this will still use the initail main thread
    ask_user()
    process.join() # this will wait until the process will finish

print(f'Running 2 threads in paralele each for 1 function took : {time.time()-start}')





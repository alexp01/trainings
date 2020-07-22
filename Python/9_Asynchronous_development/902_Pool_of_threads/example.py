
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9489748#overview

import time
from concurrent.futures import ThreadPoolExecutor

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


start = time.time()
ask_user()
complex_calculation()
print(f'The main single Thread that executes the 2 functions took : {time.time()-start}')

start = time.time()

with ThreadPoolExecutor(max_workers=5) as pool: # this will alocate 2 empty threads
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)

print(f'Running 2 threads in paralele each for 1 function took : {time.time()-start}')





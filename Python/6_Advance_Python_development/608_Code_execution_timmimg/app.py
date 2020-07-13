
import time



def power_of(limit):
    return [x**2 for x in range(limit)]
# Example 1
#time_now = time.time()
#power_of(5000000)
#time_after = time.time()
#print (time_after-time_now)

# Example 2
def calculate_run_time(func):
    time_now = time.time()
    func()
    time_after = time.time()
    return time_after-time_now

print (calculate_run_time(lambda : power_of(500000)))

import timeit

print (timeit.timeit("[x**2 for x in range(5)]")) # This is a bit faster than map function, but you get all the elements and you don't have the function next()
print (timeit.timeit("list(map(lambda x: x**2, range(5)))")) # you use this only of other languages are used in your team, as list is found in other languages, and its easier to understand
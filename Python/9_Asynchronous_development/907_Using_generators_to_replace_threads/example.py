
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9489774#overview

def countdown_list_generator(n):
    while n > 0:
        yield n
        n -= 1

tasks = [countdown_list_generator(20), countdown_list_generator(5) , countdown_list_generator(35)]

while tasks: # its True while there are still values inside the list
    task = tasks[0] # we get the first element of the list
    tasks.remove(task) # we remove the first element from the list
    try:
        x = next(task) # we get the first next element of the selected list element
        print(x) # we print it out
        tasks.append(task) # and we append the element back to the list, that has previously executed the next function
    # when the element is appended back, as its a generator, it will remember its status and the last number it generated untill it is called again
    except StopIteration: # when we reach the lower limit of the counter per element we do not add that element again to the list
        print ('task finished')

# this will simulate the way threads work, for a common function, but using generators instead

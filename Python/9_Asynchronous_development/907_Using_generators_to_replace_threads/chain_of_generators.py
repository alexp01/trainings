
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9489776#overview

from collections import deque

# Solution from training with Deque
#list_of_frinds = deque(('Rolf', 'Anthony', 'Bill', 'Philip'))
#def get_next_friend():
#    yield from list_of_frinds # this will just get the next value from the Deque

#My solution
list_of_frinds = ['Rolf', 'Anthony', 'Bill', 'Philip']
count = 0
def get_next_friend():
    global count
    while count < len(list_of_frinds):
        yield  list_of_frinds[count]
        count += 1
# Deque solution is simpler indeed

def print_next_friend(g): # the parameter is a genetaror with friends names
    while True: # this will not run for ever as the yield will stop it until the function is called again
        try:
            name = next(g)
            yield f'Friend : {name}'
        except StopIteration:
            pass # does nothing

g = get_next_friend()
friend = print_next_friend(g)

print(next(friend))
print(next(friend))
print(next(friend))
print(next(friend))
print(next(friend))
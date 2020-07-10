
# https://www.udemy.com/course/the-complete-python-course/learn/quiz/4427862#questions

from collections import defaultdict, OrderedDict, namedtuple, deque

def task4(arg_deque: deque):
    """
    - Manipulate the `arg_deque` in any order you preferred to achieve the following effect:
        -- remove last element in `deque`
        -- move the fist (left most) element to the end (right most)
        -- add an element `Zack`, a string, to the start (left)
    """
    # you code starts here:
    print(arg_deque)
    arg_deque.pop()
    print(arg_deque)
    temp_var = arg_deque[0]
    arg_deque.popleft()
    arg_deque.append(temp_var) # i could have already added the pop element into the append, like the training examples.
    print(arg_deque)
    arg_deque.appendleft('Zack')
    print(arg_deque)
    return arg_deque

var1 = deque(('Tom', 'Billy', 'Richard', 'Anna', 'Timy'))

var1 = task4(var1)
print(var1)


# Training solution:

"""
def task4(arg_deque: deque):
    arg_deque.pop()     # remove last element
    arg_deque.append(arg_deque.popleft())   # remove first element and append it to last
    arg_deque.appendleft('Zack')    # add Zack to start
"""
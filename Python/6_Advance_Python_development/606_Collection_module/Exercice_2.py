
# https://www.udemy.com/course/the-complete-python-course/learn/quiz/4427862#questions

from collections import defaultdict, OrderedDict, namedtuple, deque

def task2(arg_od: OrderedDict):
    """
    - takes in an OrderedDict `arg_od`
    - Remove the first and last entry in `arg_od`.
    - Move the entry with key name `Bob` to the end of `arg_od`.
    - Move the entry with key name `Dan` to the start of `arg_od`.
    - You may assume that `arg_od` would always contain the keys `Bob` and `Dan`,
        and they won't be the first or last entry initially.
    """
    # you code starts here:
    arg_od.popitem()
    arg_od.popitem(last=False) # Its suficinet that this arguments is just False, and not last=False
    arg_od.move_to_end('Bob')
    arg_od.move_to_end('Dan', last=False)
    return arg_od

var1 = OrderedDict()
var1['Anna'] = 23
var1['Richard'] = 34
var1['Bob'] = 13
var1['Dan'] = 8
var1['Tom'] = 103
var1['Dana'] = 8
var1['Billy'] = 103
print(var1)

task2(var1)
print(var1)

# Training solution:
"""
def task2(arg_od: OrderedDict):
    arg_od.popitem()
    arg_od.popitem(False)
    # remember to remove start and end before moving Bob and Dan, otherwise they will be removed instead
    arg_od.move_to_end('Bob')
    arg_od.move_to_end('Dan', False)
"""
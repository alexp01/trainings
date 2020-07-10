
# https://www.udemy.com/course/the-complete-python-course/learn/quiz/4427862#questions

from collections import defaultdict, OrderedDict, namedtuple, deque

def task1(username: str, userlocation : str) -> defaultdict:
    """
    - create a `defaultdict` object, and its default value would be set to the string `Unknown`.
    - Add an entry with key name `Alan` and its value being `Manchester`.
    - Return the `defaultdict` object you created.
    """
    # you code starts here:
    local_variable = defaultdict(list)
    local_variable.default_factory = 'Unknown'
    local_variable[username] = userlocation
    return local_variable

call_task1 = task1('Alan','Manchester')
print(call_task1)
# My code is not good
# I forgot to use : (lambda: 'Unknown') in order to overwrite the default dict returned value.


# Training solution:
"""
def task1() -> defaultdict:
    dd = defaultdict(lambda: 'Unknown')
    dd['Alan'] = 'Manchester'
    return dd
"""


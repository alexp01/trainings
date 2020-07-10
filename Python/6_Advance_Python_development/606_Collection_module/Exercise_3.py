
# https://www.udemy.com/course/the-complete-python-course/learn/quiz/4427862#questions

from collections import defaultdict, OrderedDict, namedtuple, deque

def task3(name: str, club: str) -> namedtuple:
    """
    - create a `namedtuple` with type `Player`, and it will have two fields, `name` and `club`.
    - create a `Player` `namedtuple` instance that has the `name` and `club` field set by the given arguments.
    - return the `Player` `namedtuple` instance you created.
    """
    # you code starts here:
    local_var1 = namedtuple('Player', ['name', 'club'])
    local_var1.name = name
    local_var1.club = club
    return local_var1

var1 = namedtuple('Player', ['name', 'club'])
var1 = task3('John','club1')
print (var1.name, var1.club)

# Training solution:

"""
def task3(name: str, club: str) -> namedtuple:
    Player = namedtuple('Player', ['name', 'club'])
    player = Player(name, club)
    return player

"""
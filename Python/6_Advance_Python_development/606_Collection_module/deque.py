
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477762#questions

# A queue can accept new elements on one side and remove elements from the other end
# a deque is a Double Deck Queue: it can inser/give elements from the 2 sides
# Deque is a list with access on bith sides

# A stack can accept/give on the top part only

from collections import deque

friends = deque(('Tom', 'Anna', 'Bob'))
friends.append('Billy')
print(friends)
friends.appendleft('Richard')
print(friends)
friends.pop()
print(friends)
friends.popleft()
print(friends)
from collections import deque
from types import coroutine

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9489780#overview

friends = deque(('Anna', 'Bob', 'Tommy', 'Billy', 'Dana'))

@coroutine # this will mark this function as a courutine type
def friend_upper():
    while friends: # runs untill there are no more values inside the deque
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} : {friend}')

# Instead of running this:
#def great():
#    yield from g

# You can run this:
async def greet(g):
    print('Starting...')
    await g # this will wait until friend_upper will finish its while loop. So when there are no more friends in the deque
    print('Ending...')

greeter = greet(friend_upper())
greeter.send(None) # this will stop the greet fct right before the yield
greeter.send('Helo') # this will rerun the greet fct from the yield position, giving it the value Hello, that will be passed to greeting and then pushed to friend_upper fct for its yield also
print ('Now you can execute another functionality as the others are stopped')
greeter.send('Now you reactivate the previous runned software , Hello friend : ')
print('Now you can execute another functionality as the others are stopped')
greeter.send('Now you reactivate the previous runned software , Hello friend : ')

# You you run only what's above you will never print Ending ...
# As the geet fct will not quit the await line until frind_upper will finish all friends and will raise the StopIterration error

print ('Now you can execute another functionality as the others are stopped')
greeter.send('Now you reactivate the previous runned software , Hello friend : ')
print('Now you can execute another functionality as the others are stopped')
greeter.send('Now you reactivate the previous runned software , Hello friend : ')
print ('Now you can execute another functionality as the others are stopped')
greeter.send('Now you reactivate the previous runned software , Hello friend : ')

# Now it will print the Ending ... form greet fct


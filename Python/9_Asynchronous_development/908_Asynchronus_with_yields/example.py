from collections import deque

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9489778#overview##
# Its a great example of simulation asynchronus execution in Python using just yields

friends = deque(('Anna', 'Bob', 'Tommy', 'Billy', 'Dana'))

def friend_upper():
    while friends: # runs untill there are no more values inside the deque
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} : {friend}')

def greet(g):
    g.send(None) # we also activate the friend_upper function, and this will stop just before executing yield
    # This will only execute 1, as for every yield value sent by using greeter.send(xxx), you run another loop of the while. You do not run the function entirely
    while True:
        greeting = yield
        g.send(greeting)

# great function can be also written as :
#def great():
#    yield from g
# But its a bid complex as syntax and does not provide a lot of info about what it does

greeter = greet(friend_upper())
greeter.send(None) # this will stop the greet fct right before the yield
greeter.send('Helo') # this will rerun the greet fct from the yield position, giving it the value Hello, that will be passed to greeting and then pushed to friend_upper fct for its yield also
print ('Now you can execute another functionality as the others are stopped')
greeter.send('Now you reactivate the previous runned software , Hello friend : ')
print('Now you can execute another functionality as the others are stopped')
greeter.send('Now you reactivate the previous runned software , Hello friend : ')
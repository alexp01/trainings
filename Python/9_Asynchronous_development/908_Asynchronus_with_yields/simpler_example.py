
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9489778#overview##

def greet():
    friend = yield
    print(f'Hello : {friend}')

g = greet()
g.send(None) # priming the generator. It will activate the genarator and stop the function at the yield part as it does not have a value yet. It will be none curently.
g.send('Adam') # this will restart the function at the yield line, so friends will now have the value from yield

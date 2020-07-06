
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445596#questions

# yield can be used to temporary stop a function, so that you can coninue it afterwards

def get_100_numbers() -> int:
    i = 0
    while i < 100:
        yield i
        i +=1

# yield is like a return, but it will also remember inside the function the last execution point and the values
# so when it reaches yield it will return i, and when its called again by next(variable), it will continue with i = I=1, and then run the while again

x = get_100_numbers()
print (x)
print (next(x)) # this will call again the function and it will continue from where it was stopped -> when i = 0
print (next(x)) # this will call again the function and it will continue from where it was stopped -> when i = 1

print(list(x)) # this will execute the function until it reaches the limit
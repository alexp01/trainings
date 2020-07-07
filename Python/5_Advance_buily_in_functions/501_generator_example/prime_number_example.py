
# https://www.udemy.com/course/the-complete-python-course/learn/quiz/4902696#questions

def get_prime(bound: int) -> None:
    for x in range (2, bound):
        for y in range (2, x):
            if x % y == 0:
                break
        else:
            yield (x)
        # the else in for is executed if the for executed without encountering any break and reach the end of the for limit

prime_number = get_prime(20)
print (prime_number)
print (next(prime_number))
print (next(prime_number))
print (next(prime_number))

print (list(prime_number))
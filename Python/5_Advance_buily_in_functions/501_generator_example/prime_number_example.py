
# https://www.udemy.com/course/the-complete-python-course/learn/quiz/4902696#questions

def get_prime(bound: int) -> None:
    for x in range (2, bound):
        prime_b = False
        for y in range (2, x):
            if x % y == 0:
                prime_b = True
        if not prime_b:
            yield (x)

prime_number = get_prime(20)
print (prime_number)
print (next(prime_number))
print (next(prime_number))
print (next(prime_number))

print (list(prime_number))
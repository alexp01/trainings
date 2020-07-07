
# https://www.udemy.com/course/the-complete-python-course/learn/quiz/4902698#questions

class GenPrime:
    def __init__(self, bound):
        self.number = 3
        self.bound = bound

    def __next__(self):
        if self.number < self.bound:
            for y in range(2, self.number):
                if self.number % y == 0:
                    self.number += 1
                    break
            else:
                self.number += 1
                return self.number-1

var_prime = GenPrime(20)

for x in range(20):
    a= next(var_prime)
    if a != None:
        print (a)

# trainer solution
#    class PrimeGenerator:
#        def __init__(self, stop):
#            self.stop = stop
#            self.start = 2
#
#        def __next__(self):
#            for n in range(self.start, self.stop):  # always search from current start (inclusive) to stop (exclusive)
#                for x in range(2, n):
#                    if n % x == 0:  # not prime
#                        break
#                else:  # n is prime, because we've gone through the entire loop without having a non-prime situation
#                    self.start = n + 1  # next time we need to start from n + 1, otherwise we will be trapped on n
#                    return n  # return n for this round
#            raise StopIteration()  # this is what tells Python we've reached the end of the generator

# https://www.udemy.com/course/the-complete-python-course/learn/quiz/4425480#overview

from salary import Salary
from promotable import Promotable

class Employee(Salary, Promotable):
    def __init__(self, rate: float):
        self.rate = rate # hourly salary

    def weekly_salary(self) -> float:
        return self.calculate(35) # for a 35 h working week

rolf = Employee(15.0)
print(rolf.weekly_salary()) # will print 35*15
rolf.promote(5.0) # will make the rate = 15+5
print(rolf.weekly_salary()) # will print 35*20

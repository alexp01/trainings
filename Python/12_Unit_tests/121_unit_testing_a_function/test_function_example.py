
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/15207106#overview

from unittest import TestCase
from function_example import  calculate

class Test_my_function(TestCase):
    def test_calculate(self):
        dividend = 15
        divisor = 3
        expected_result = 5.0
        self.assertEqual(calculate(dividend,divisor), expected_result)
        # a better solution in case the division has multiple decimals is the falowings :
        #self.assertAlmostEqual(calculate(dividend, divisor), expected_result, delta = 0,00001) # the delta value is the admited diference during the comparison

    def test_nagative_values(self):
        dividend = 15
        divisor = -3
        expected_result = -5.0
        self.assertEqual(calculate(dividend,divisor), expected_result)

    def test_zero_value(self):
        dividend = 0
        divisor = 3
        expected_result = 0.0
        self.assertEqual(calculate(dividend,divisor), expected_result)

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/15207110#overview

from unittest import TestCase
from function_example import  calculate, multiply

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

    def test_error_for_zero_devision(self):
        with self.assertRaises(ValueError):
            calculate(5,0)
        # an equivalent of the top 2 lines would be:
        #self.assertRaises(ValueError, lambda : calculate(5,0)) # as argument you give the Error that must be raised by calling calculate, and a callable thing, so thats why you give a lambda and not directly the calculate func, as calling it will just give the results as argument

    def test_multiply_function_error_raised(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_single_value(self):
        expected = 5
        self.assertEqual(multiply(expected), expected)

    def test_multiply_by_zero(self):
        expected = 0
        self.assertEqual(multiply(expected), expected)

    def test_multiply_working_case(self):
        expected = 30
        inputs = (2,3,5)
        self.assertEqual(multiply(*inputs), expected)

    def test_multiply_working_case_with_zero(self):
        expected = 0
        inputs = (2,0,5)
        self.assertEqual(multiply(*inputs), expected)

    def test_multiply_2_negativ_values(self):
        expected = 30
        inputs = (2,-3,-5)
        self.assertEqual(multiply(*inputs), expected)

    def test_multiply_floats(self):
        expected = 30.0
        inputs = (2.0,3.0,5.0)
        self.assertEqual(multiply(*inputs), expected)
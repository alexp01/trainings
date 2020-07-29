
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/15207114#overview
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/15207116#overview

from unittest import TestCase
from class_example import Printer, PrinterError

class TestPrinter(TestCase):
    def setUp(self): # this will reinitialise the self.printer values for every function execution from bellow
        self.printer = Printer(pages_per_s=2.0, capacity=300)
    # In other words it will always have capacity = 300

    # Another solution that is not recommended is to have this code:
    #@classmethod
    #def setUpClass(cls):
    #    cls.printer = Printer(pages_per_s=2.0, capacity=300)
    # this will remember the last capacity changes. But this will make your unit tests dependend one to the others. And this is not good.

    def test_print_within_capacity(self):
        self.printer.print(25)

    def test_error_raised(self):
        with self.assertRaises(PrinterError):
            self.printer.print(301)

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
        message = self.printer.print(25)
        self.assertEqual(f"Printed 25 pages in 12.50 seconds.", message)

    def test_error_raised(self):
        with self.assertRaises(PrinterError):
            self.printer.print(301)

    def test_print_exact_capacity(self):
        self.printer.print(self.printer._capacity) # to print all the capacity pages
        self.assertEqual(self.printer._capacity, 0)

    def test_printer_speed(self):
        pages = 10
        expected = "Printed 10 pages in 5.00 seconds."
        self.assertEqual(self.printer.print(pages), expected)

    def test_spped_with_2_decimals(self):
        fast_printer = Printer(pages_per_s=3.0, capacity=300)
        expected = "Printed 11 pages in 3.67 seconds."
        pages = 11
        result = fast_printer.print(pages)
        self.assertEqual(result, expected)

    def test_multiple_prints(self):
        self.printer.print(200)
        self.printer.print(75)
        self.printer.print(25)

    def test_multiple_prints_with_error(self):
        self.printer.print(200)
        self.printer.print(75)
        self.printer.print(25)

        with self.assertRaises(PrinterError):
            self.printer.print(1)

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/15207114#overview

from unittest import TestCase
from example_class import printer, printerError


class Test_my_example(TestCase):
    def check_if_printer_works(self):
        printer_module = printer(capacity = 300, pages_per_s = 2.0)
        message = printer.print_pages(25)
        self.assertEqual(f"Printed 25 pages in 12.50 seconds", message)

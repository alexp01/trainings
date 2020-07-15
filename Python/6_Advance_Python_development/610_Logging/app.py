
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477778#questions

# This is an example of logs in the Console

import logging
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]:%(message)s', level=logging.DEBUG)
logger = logging.getLogger('test_logger')

logger.info('This is a info type message')
logger.warning('This is a warning')

# By default only the warning abobe warnings are stores (including the warnings ones)
# by doing a loggin.basicConfig with level=logging.DEBUG you can update this level
# The levels based on their importance:
"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""
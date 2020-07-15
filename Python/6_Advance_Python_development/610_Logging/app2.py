
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477778#questions

# This is an example of logs in Log files. The content is appended not overwritten

import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]:%(message)s',
    datefmt = '%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename = 'logs.txt'
)
logger = logging.getLogger('books')

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

logger = logging.getLogger('books.database') # this is a child of the books log

logger.error('This is an error type message')
logger.critical('This is a critical message')
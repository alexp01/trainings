
# https://www.udemy.com/course/the-complete-python-course/learn/quiz/4425468#questions

import re
"""
Our definition of a secure filename is:
- The filename must start with an English letters or a number (a-zA-Z0-9).
- The filename can **only** contain English letters, numbers and symbols among these four: `-_()`.
- The filename must end with a proper file extension among `.jpg`, `.jpeg`, `.png` and `.gif`
"""

def is_filename_safe(filename):
    regex = '[A-z0-9\-\(\)\_]+.(jpg|jpeg|png|gif)'
    return re.match(regex, filename) is not None

print (is_filename_safe('asjhfda89YT()hfadf.png'))
from pages.common.log import *
import glob
import os


folder_path = os.path.dirname(os.path.abspath(__file__))
files_path = os.path.join(folder_path, '*')
files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
print (files[0]) #latest file

import Scenario01
import Scenario03
import Scenario04
import Scenario05
import Scenario06

logging.info('### All tests are PASSED')

file = open(files[0], 'r')
file_content = file.read()

print(file_content)



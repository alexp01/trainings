
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445296?start=30#questions

#from util.common.second_import import func2
from util.first_import import func1, show
# These will give me an error, in the training it works

# importing the entire module works on the other hand
#import util.common.second_import
import util.first_import
# we do not need to import in app.py the second_import.py, as its already imported by first_import.py

print ('We executed main app.py ', __name__)
func1()
#func2()
# i do not manage to access this method from a module : func2

# the name printed is __main_-as this is the way python sees this main app that was first run.
# the same print in second_import.py script will print the path of that py file.


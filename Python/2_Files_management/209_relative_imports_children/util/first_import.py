#import util.common.second_import
from util.common.second_import import func2

def show():
    print('i want to run this function only if i execute only the module first_import, and not if i run it from app.py')

def func1():
    print('We have imported and runned util.first_import.py ', __name__)

print ('when imported the module first_import.py is executed also')

if __name__ == '__main__':
    show()
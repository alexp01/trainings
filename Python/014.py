
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/10057990#questions

def power_of_two():
    error_var = 0
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was not a number')
        error_var = 1
        return 0
    finally :
        n_square = n ** 2
        return n_square

# if the expection is run, so we have an error, we ignore the return 0 from the except block and we execute the finally block
# if finally would not have a return, and teh except block is executed, it wil lreturn 0

#    try:
#        n = float(user_input)
#        n_square = n ** 2
#        return n_square
#    except ValueError:
#        print('Your input was not a number')
#        error_var = 1
#        return 0
#
#    We should always put all the operations in the try block, and in case it will fail it will display the error and return something, zero in our case.

#    Important to remember:
# Else will only execute if the Try was succesful, and no error was raised.
# the Finally block is to be used just to close something, as a conclusion. As it might be that it will not always execute (example, finally does not have a return, but Except will, and we raise that error from the except.)

print (power_of_two())

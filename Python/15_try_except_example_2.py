
# https://www.udemy.com/course/the-complete-python-course/learn/quiz/4902676#questions

def Game():
    continue_value = True
    while continue_value:
        answer = input('Please give a number:_')
        try:
            if int(answer) % 2 == 0:
                print (f'The number {answer} is even')
            else:
                print (f'The number {answer} is odd')
        except ValueError:
            print ('Error: Please give a integer value')
            continue_value = False
        else:
            continue_value = False


user_choise = 'y'
while user_choise == 'y':
    Game()
    user_choise = input ('Do You want to continue? y/n : _')
print ('Goodbye')

# Training solution:
#def interact():
#    while True:
#        try:
#            user_input = int(input('Please input an integer:'))  # try to turn user input into an integer
#        except ValueError:
#            print('Please input an integer only.')  # print a message if user didn't input an integer
#        else:
#            print('{} is {}.'.format(user_input, 'even' if user_input % 2 == 0 else 'odd'))  # print even/odd if the user input an integer
#        finally:  # regardless of the previous input being valid or not
#            user_input = input('Do you want to play again? (y/N):')  # ask if the user wants to play again
#            if user_input != 'y':  # quit if the user didn't input `y`
#                print('Goodbye.')
#                break  # break the while loop to quit

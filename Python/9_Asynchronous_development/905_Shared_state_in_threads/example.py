import time

counter = 0

def generate_numbers():
    global counter
    counter += 1
    print (f'The counter value is {counter}')
    print('------------')

for x in range(10):
    generate_numbers()

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477742#questions

# Example 1: dictionary

friends = {'John' : 3, 'Anna': 16}

def last_seen(friends_dict, friend):
    print(id(friends_dict[friend])) # ID2 as an element inside a Dict has anotehr ID, based on its content, in our case a int
    friends_dict[friend] = 0
    if (friends is friends_dict): # to compare the id of 2 elements we use : is
        print ('True')
    print(id(friends_dict[friend])) # ID3, as int as non mutable, dict[John] == 0 so it will contain the id of 0

print(id(friends)) # ID1
last_seen(friends,'John')
print(id(friends['John'])) # ID3, as its value is 0 it will point to the same id, as ist value was not changed again
print(id(friends)) # ID1 as friends is always a label of that dict content

# Example 2: int is non mutable
print('Example 2')
x = 2

def change_x(number):
    number = number +1
    print(id(number)) # ID2 as now the number is differnet, 3, so its stored in another location than 2

print(id(x)) # ID1
change_x(x)
print(id(x)) # ID1

# Example 3: list
print('Example 3')

numbers = [2, 6, 4]
print(id(numbers)) #ID1
numbers += [1, 9]
print(id(numbers)) #ID1 as its dpoing a __iadd__ method that tries to keep the same location
numbers = numbers + [3, 7]
print(id(numbers)) # ID2 as its doing a __add__ that will alocate a new location for the value
numbers = [4, 6] + [3, 7]
print(id(numbers)) # ID3 a its a completly new value and location
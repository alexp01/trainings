
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9790248#overview

import time

# list1 = range(1000000)
# sorting the list
#list1.sort()

list1 = []

for x in range(0,1000000):
    list1.append(x)

# It does not work in python to update the item used in the loop
#for x in range(0,len(list1)):
#    for y in range(x,len(list1)):
#        if list1[x] > list1[y]:
#            smaller_than_selected = y
#    temp1 = list[y]
#    list[y] = list[x]
#    list[x] = temp1

search_for = 99999

# sequencial seach
initial_time = time.time()

for x in range(0,len(list1)):
    if list1[x] == search_for:
        print(f'We found 99999 after {x} loops')

print(f'Sequencial search took {time.time()-initial_time}')

# binary search
initial_time = time.time()

first_elem = 0
last_elem = len(list1)
middle_val = last_elem // 2
continue_bol = True
iteration = 1
temp_list = list1
while continue_bol:
    if temp_list[middle_val] == search_for:
        print(f'Binary search found 99999 after {iteration} loops ')
        break
    else:
        iteration += 1
        if temp_list[middle_val] < search_for:
            first_elem = middle_val
        else:
            last_elem = middle_val
        #print(first_elem, last_elem)
        temp_list = temp_list[first_elem:last_elem]
        first_elem = 0
        last_elem = len(temp_list)
        middle_val = last_elem // 2
        # print(temp_list[0], temp_list[middle_val], temp_list[last_elem-1])

print(f'Binary search took {time.time()-initial_time}')
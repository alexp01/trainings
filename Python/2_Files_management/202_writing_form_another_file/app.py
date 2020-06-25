
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445282#questions

file1 = open('friends.txt', 'r')
file1_content = [line.strip() for line in file1.readlines()]
# variable.strip( will eliminate any spaces or \n from a string. before and after that string)
# Its easier to use strip that doing it like i did bellow
#for x in range(0, len(file1_content)-1):
#    file1_content[x] = file1_content[x][:-1]
file1_content_set = set(file1_content)
name = input ('please give 3 names separated by a comma:_').split(',')
name_set = set(name)
file1.close()

file2 = open('close_friends.txt', 'w')
# Its better to use sets and intersection function, than the below code.
#for x in range(0, len(name)):
#    if name[x] in file1_content:
#        file2.write("\n" + name[x])
# On the other hand you still have to use a for to add each Set element into the file. So you will use a for in the end
intersection_set = name_set.intersection(file1_content_set)
for x in intersection_set:
    print(f"We've found a friend : {x}")
    file2.write(x + '\n')
file2.close()

file2 = open('close_friends.txt', 'r')
file2_content = file2.read()
print (f'All known friens were added to the close_frinds.txt file. Content:\n{file2_content}')
file2.close()

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445282#questions

file1 = open('friends.txt', 'r')
file1_content = file1.readlines()

for x in range(0, len(file1_content)-1):
    file1_content[x] = file1_content[x][:-1]

name1 = input ('please give the name of the first friend:_')
name2 = input ('please give the name of the second friend:_')
name3 = input ('please give the name of the third friend:_')

file2 = open('close_friends.txt', 'w')

if name1 in file1_content:
    file2. write("\n" + name1 + "\n")
if name2 in file1_content:
    file2. write(name2 + "\n")
if name3 in file1_content:
    file2. write(name3 + "\n")

file2.close()

file2 = open('close_friends.txt', 'r')
file2_content = file2.read()

print (file1_content)
print (f'All known friens were added to the close_frinds.txt file. Content: {file2_content}')

file1.close()
file2.close()
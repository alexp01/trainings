
#https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445280?start=0#questions

file = open('data.txt', 'r')
file_content = file.read()

print(file_content)

file.close()

value_to_add = input ('Please give a string that you want to add to your file:_')
# openning a file with w mode, will delete the initial content of this file and overwrite it with an ew value.
file2 = open('data.txt', 'w')
file2.write(value_to_add)

file2.close()
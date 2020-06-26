
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445292#questions

#import first_library
# this works when we have the file in the same folder. You can benefit from the entire content fo that file
# when you call a function you une the [file_name].[function_name]
# or you can just import some functions and not the entire file

from utils.first_library import write_to_file, read_from_file

print (read_from_file('data.txt'))
write_to_file('This is the text to write', 'data.txt')

# the utils folder is called a package. In some older python versions, it needs to have inside a __init_-.py file
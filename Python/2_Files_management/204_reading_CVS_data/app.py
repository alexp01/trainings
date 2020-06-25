
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445284#questions

csv_file = open('data_csv.txt', 'r')
csv_content = csv_file.readlines()
csv_file.close()
lines = [line.strip() for line in csv_content[1:]]

for line in lines:
    data = line.split(',')
    name = data[0].title() # will make every word in this string with Upper case
    age = data[1]
    univ = data[2].title()
    degree = data[3].capitalize() # will make only the first word in the string with capital letters
    print (f'{name} is {age}, studying {degree} at {univ}')

build_a_csv_file = ','.join(["Rolf", "23", "oxford", "Arts"])
print (build_a_csv_file)
# This is how you build a cvs type of variable, by joining a Set 
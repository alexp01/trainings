
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/15167558#questions

import re

str1 = 'fafdsfdfdsfds@Gmail.fr'
#expression = '[A-z\.]+@[A-z]+.[A-z]+'
expression = '[a-z]+'
matches = re.findall(expression, str1)
print (matches)
print (f' Domain is : {matches[1]}.{matches[2]})')

str2 = 'Price: $13,543.87'
expression2 = 'Price: \$([0-9,]*\.[0-9]*)' # ading () will allow us to match 2 things
matches2 = re.search(expression2, str2)
print (matches2[0])
print (matches2[1])

price_with_no_comma = matches2[1].replace(',', '')
price = float(price_with_no_comma)
print(price)
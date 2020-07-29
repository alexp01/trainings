from database import Database
from admin import Admin

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9583280?start=0#overview
# in this example we see a tipical inheritage admin -> user, but also admin-> Saveable, that is not a typical inheritage. We do it to reuse a piece of repeating  logic

a = Admin('Tom', '1234', 5)
#print(a)

a.save()

print(Database.find(lambda x : x['username'] == 'Tom'))
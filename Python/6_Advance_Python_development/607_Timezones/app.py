
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477766#questions
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477768#questions

from datetime import datetime,timezone, timedelta

now = datetime.now(timezone.utc)
print(now)
tomorrow = now + timedelta(days=2)
print(tomorrow)

print(now.strftime('%d-%m-%Y, %H:%M:%S')) # strf is string format

user_date = input('Please give a date YYYY-MM-DD:_')
user_date = datetime.strptime(user_date, '%Y-%m-%d') # strp is string parse time
print(user_date)
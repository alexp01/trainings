
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477756#questions

account = {'savings' : 4500, 'balance' : 2300}

def update_account(account_type : str, value : int):
    account[account_type] += value

Multiple_values = [
    ('savings', -800),
    ('savings', 2000),
    ('balance', -100),
    ('savings', -1300),
    ('balance', 4000),
    ('savings', 200),
]

for t in Multiple_values:
    update_account(t[0], t[1])

for v in Multiple_values:
    update_account(*v) # this will takes all element of that tuple and give them as arguments to the function
# if there are 3 element in 1 line, it will give 3 arguments to the function

print(account)

for t in Multiple_values:
    update_account(account_type =t[0], value=t[1]) # Its recomended to put the parameters name in the argumenst also, so its easier to read

print(account)



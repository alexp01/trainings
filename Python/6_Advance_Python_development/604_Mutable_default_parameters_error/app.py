from typing import List

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477754#questions

def update_account_details(name: str, account_owner : str, account_users: List = []):
    print(id(account_users))
    account_users.append(account_owner)
    return {
            'account_name' : name,
            'account_owner' : account_owner,
            'account_users' : account_users
            }

print(update_account_details('Account2345', 'John'))
print(update_account_details('Account2345', 'Rick')) # Normally you would expenct that the users element contains only Rick
# as you called the function and teh default value for account_users is []
# But lists are mutable elements, so actually you use the [] memory location, and you just add new values into it by keeping the same location
# thats why we should never use mutable default values, but non mutable ones like int, float, tuples and str

# Important : the default parameters of a functions are assigned when a function is defined not when its called.
# Thats why it the List has values [] assigned, before we actually called the function

# To fix the above issues you could do:

def update_account_details2(name: str, account_owner : str, account_users: List ):
    print(id(account_users))
    account_users.append(account_owner)
    return {
            'account_name' : name,
            'account_owner' : account_owner,
            'account_users' : account_users
            }

print('Example 2 ->')
print(update_account_details2('Account2345', 'John', []))
print(update_account_details2('Account2345', 'Rick', []))

# this will contain only Rick in the account_users List, after the second call of that function
# What its strange is that the id number is the same. Even if i assigned 2 different [] Lists. They should be stored in different locations.

# Or this solution:

def update_account_details2(name: str, account_owner : str, account_users = None ):
    if not account_users:
        account_users = []
    print(id(account_users))
    account_users.append(account_owner)
    return {
            'account_name' : name,
            'account_owner' : account_owner,
            'account_users' : account_users
            }
print('Example 3 ->')
# print(update_account_details2('Account2345', 'John', ['Anna']))
print(update_account_details2('Account2345', 'John'))
print(update_account_details2('Account2345', 'Rick'))

# after each call of the function in the account_users there is just 1 element.
# Again the id is the same and i do not know why
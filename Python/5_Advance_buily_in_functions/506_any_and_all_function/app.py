
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9445626#questions

friends =[
    {
        'name' : 'John',
        'town' : 'Lille'
    },
    {
        'name' : 'Anna',
        'town' : 'Toulon'
    }
        ]
near_friends_town = input ('Please give your current town location ot check in your friend list:_')
near_by_friends = [f for f in friends if f['town'] == near_friends_town]

print (near_by_friends)

# If you just want to know if you have at least 1 value in your list, then you can do any function
# it will check each value to see if its True : bool(list[element])
near_by_friends_2 = any(near_by_friends)
print (near_by_friends_2)

# all function will check if all elements are equal to True
near_by_friends_3 = all(near_by_friends)
print (near_by_friends_3)

print (all([0,1,2,3,4])) # This will print False as bool[0] = false
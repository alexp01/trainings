
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477756#questions

users = [
    {
        'user_name' : 'alex',
        'pass_val' : 'admin'
    },
    {
        'user_name' : 'john',
        'pass_val' : 'admin'
    }
        ]

class map_users:
    def __init__(self, user_name : str, pass_val : str):
        self.user_name = user_name
        self.pass_val = pass_val

    @classmethod
    def fromdict(cls, data):
        return cls(data['user_name'], data['pass_val'])

    def __repr__(self):
        return (f'{self.user_name} {self.pass_val}')

# This is one way to do it
#user_objects = map(map_users.fromdict, users)

#This is another way. It will generate a list of object
#user_objects = [map_users(data['user_name'], data['pass_val']) for data in users]

#This is another way. by giving the papameter names in arguments
#user_objects = [map_users(user_name = data['user_name'], pass_val = data['pass_val']) for data in users]

# This is the bext way using dict unpacking:
user_objects = [map_users(**v) for v in users]

print(user_objects[0])
print(user_objects[1])


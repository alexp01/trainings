from user import User
from saveable import Saveable

class Admin(User, Saveable):
    def __init__(self,username, password, level):
        super(Admin, self).__init__(username, password)
        self.level = level

    def __repr__(self):
        return f'Admin {self.username}, access {self.level}'

    def to_dict(self):
        return {
            'username' : self.username,
            'password' : self.password,
            'level' : self.level
        }

    # self.save will be searched in Admin
    # then in Users
    # then in Saveable, where it will be found

    # self.save() used self.to_dict

    # self.to_dict() will be searched for in Admin, where it will be found

"""
app -> admin(to_dict) -> User
                      -> Saveable(to_dict) # when you call self.to_dict from Saveable it will use the to_dict from Admin
    -> store
"""
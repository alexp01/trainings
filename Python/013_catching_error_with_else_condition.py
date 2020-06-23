class User:
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.user_score = 0

def check_if_email_needs_to_be_sent(user_info):
    try:
        user_info.score = calculate_score(user_info.data)
    except KeyError:
        print (f'You want to access a key that does not exist')
        #raise
        # If you put raise when you catch the error also, you show the error in the stacktrace. The error details.
    else:
        if user_info.score > 500:
            send_notification_to_user()
    # the except will always execute and if it does not, it will execute the else. So as long as no error in encounter we notifi the user, if its score is bigger than a value.
    # In this way we do not notify the user until we acumulate sufficient info to actually benefit from a notification.
    # User case: the GSM consumption of a user

def calculate_score(user_data):
    return user_data['clicks']*5 + user_data['hints']*2

def send_notification_to_user(user_name):
    print ('This will simulate an email that is sent to the user')

#user_1 = User('John_First', {'clicks': 20, 'hints':10})
#check_if_email_needs_to_be_sent(user_1)

user_2 = User('John_First', {'click': 20, 'hints':10})
check_if_email_needs_to_be_sent(user_2)
# I called the function with click and not clicks, and when we calculate the scoare we can not find the dict key 'sclick' so we raise the KeyError
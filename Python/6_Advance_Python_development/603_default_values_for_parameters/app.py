
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9477748#questions

credit= {
    'account' : 1600,
    'savings' :3700
}

# the parameters without a defaut value must be last
def change_amount(value: float, name: str = 'account') -> float:
    credit[name] += value
    return (credit[name])

print(change_amount(500))

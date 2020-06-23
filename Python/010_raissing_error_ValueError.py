
def count_from_0_to_n(n):
    if n < 0:
        raise ValueError('You provided a negative int, please give a number above 0')
    for x in range(0,n+1):
        print (x)

count_from_0_to_n(-7)
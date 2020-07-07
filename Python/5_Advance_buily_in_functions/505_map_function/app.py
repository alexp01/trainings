friends = ['Rolf', 'Anna', 'Roul', 'John', 'Robin']

# version with map
lower_friedns_1 = map(lambda x: x.lower(), friends)
#print(next(lower_friedns_1)) # it does not work as this generator is not iterable
print(lower_friedns_1)

# better version, identical to maps : generator comprehension
lower_friends_2 = (f.lower() for f in friends)
#print(lower_friends_2)
print(next(lower_friends_2))

# similar to maps but it will store it in a list, and this is not a generator. So there is no next method
lower_friends_3 = [f.lower() for f in friends]
#print(next(lower_friends_3)) # this does not work as its not a generator to have next
print(lower_friends_3)

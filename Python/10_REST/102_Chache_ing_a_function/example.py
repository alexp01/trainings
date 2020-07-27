
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/15206680#overview
# We will cash the func that will fetch the rates for 1 h as we know that the rates are changed every hour

from cachetools import cached, TTLCache

ID = 'eba75954dd37497589f03a547d07b89b'

client = OpenExchangeClient(ID)
usd_amount = 100

start_time = time.time()
EUR_amount = client.convert(usd_amount, 'USD', 'EUR')
print (EUR_amount)
print (f'1 func call took: {time.time() - start_time}')

start_time = time.time()
EUR_amount = client.convert(usd_amount, 'USD', 'EUR')
print (EUR_amount)
print (f'2 func call took: {time.time() - start_time}')

start_time = time.time()
EUR_amount = client.convert(usd_amount, 'USD', 'EUR')
print (EUR_amount)
print (f'3 func call took: {time.time() - start_time}')
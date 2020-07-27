from tools import OpenExchangeClient
import time

# https://www.udemy.com/course/the-complete-python-course/learn/lecture/15206674#overview
# https://docs.openexchangerates.org/docs/latest-json

import requests

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

#print(f'The amount of 100 EUR in USD is : {EUR_amount}')


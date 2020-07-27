
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/15206674#overview
# https://docs.openexchangerates.org/docs/latest-json

import requests

ID = 'eba75954dd37497589f03a547d07b89b'
ENDPOINT = 'https://openexchangerates.org/api/latest.json'

response = requests.get(f"{ENDPOINT}?app_id={ID}") # this will fetch the json repsonse into a python Dictionary
print (response) # will print response [200]
#print (response.json()["rates"]) # print all values from rates elements inside the json

exchange_rate_EUR = response.json()["rates"]['EUR'] # gers the EUR exchange rate with dollars
print(f'Exchange rate EUR-USD is : {exchange_rate_EUR}')

amount = 100
print(f'The amount of 100 EUR in USD is : {amount*exchange_rate_EUR}')


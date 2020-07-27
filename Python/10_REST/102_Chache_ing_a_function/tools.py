import requests
import functools

class OpenExchangeClient:

    ENDPOINT = 'https://openexchangerates.org/api/latest.json'

    def __init__(self, ID):
        self.ID = ID

    @property
    @functools.lru_cache(maxsize=2, ttl= 900) # this will use a cash to give the same response, and every 900 secs it will execute the function again to fetch the new rates
    def connect(self):
        return requests.get(f"{self.ENDPOINT}?app_id={self.ID}").json() # we give back the json in Dict format

    def convert(self, amount, from_cur, to_cur):
        exchange_rate_EUR = self.connect["rates"][to_cur]
        return (f"{from_cur} {amount} is {to_cur} {exchange_rate_EUR*amount}")

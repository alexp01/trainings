import requests
import functools

class OpenExchangeClient:

    ENDPOINT = 'https://openexchangerates.org/api/latest.json'

    def __init__(self, ID):
        self.ID = ID

    @property
    @functools.lru_cache(maxsize=2) # this will use a cash to not call the funct all the time as the response is the same
    def connect(self):
        return requests.get(f"{self.ENDPOINT}?app_id={self.ID}").json() # we give back the json in Dict format

    def convert(self, amount, from_cur, to_cur):
        exchange_rate_EUR = self.connect["rates"][to_cur]
        return (f"{from_cur} {amount} is {to_cur} {exchange_rate_EUR*amount}")

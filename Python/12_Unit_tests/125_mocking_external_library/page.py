
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/15207118#overview

import requests

class PageRequester:
    def __init__(self, url):
        self.url = url

    def get(self):
        return requests.get(self.url).content


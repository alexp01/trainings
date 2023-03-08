import requests
import logging

'''
Scenario details:
 - It will execute some GET's and parse some reponses with some 'fake' checks just to practice parsing and logging.
 - All REST execution will be added in logs with body, response and Endpoint.
 - For POST it will fetch the body from a separate file with the name of the endpoint.
'''

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]:%(message)s',
    datefmt = '%d-%m-%Y %H:%M:%S',
    level=logging.INFO,
    filename = 'logs.txt',
    filemode = "w"
)
logger = logging.getLogger('test_logger')

# GET
r = requests.get('https://dummyjson.com/products')
logging.info(' ### GET ### : https://jsonplaceholder.typicode.com/posts')
logging.info(' ENDPOINT : posts')

logging.info(' Reponse: ' + str(r.status_code))
logging.info(' Reponse body: ' + str(r.json()))


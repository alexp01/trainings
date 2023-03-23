# https://dummyjson.com/docs

import requests
import logging
import xlsxwriter
import datetime
import json

'''
Scenario details:
 - It will execute some GET's and parse some reponses with some 'fake' checks just to practice parsing and logging.
 - All REST execution will be added in logs with body, response and Endpoint.
 - For POST it will fetch the body from a separate file with the name of the endpoint.
 - Logs are created with details about each ENDPOINT and their verifications.
 - An XLS report will be also generated with a simpler format.
'''

class MyException(Exception):
    pass

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]:%(message)s',
    datefmt = '%d-%m-%Y %H:%M:%S',
    level=logging.INFO,
    filename = datetime.datetime.today().strftime('%Y-%m-%d') + '_logs.txt',
    filemode = "w"
)
logger = logging.getLogger('test_logger')

#This file will generate an xls at the end of the execution

workbook = xlsxwriter.Workbook(datetime.datetime.today().strftime('%Y-%m-%d') + '.xlsx')
worksheet = workbook.add_worksheet()
xls_format = { "Type" : "A",
              "EndPoint" : "B",
              "Status" : "C",
              "Verifications" : "D"}
index = 1
for key,value in xls_format.items():
    worksheet.write(value + str(index), key)

# GET https://dummyjson.com/products
# This will get all products available in DB
URL = 'https://dummyjson.com'
endpoint = '/products'
r = requests.get(URL + endpoint)
logging.info('### 1 ########################################')
logging.info('   ### GET ### : ' + URL + endpoint)
logging.info('   ENDPOINT : ' + endpoint)
#Verify Responsse status code = 200
assert r.status_code == 200, f'The Reponse status code: {r.status_code} is not the expected 200 value.'
logging.info('   Reponse: ' + str(r.status_code))
logging.info('   Reponse body: ' + str(r.json()))
logging.info('   Reponse headers : ')
for key,value in r.headers.items():
    logging.info('      ' + key + ' : ' + value)
logging.info('   End of reponse headers.')

response_json = r.json()

#Checks
# 1. How many products are received, compared to a known value.
expected_number_of_products = 30
logging.info('   Verifications:')
logging.info('   # 1. How many products are received, compared to a known value.')
assert expected_number_of_products == len(response_json["products"]), f'The available products number of {len(response_json["products"])} is not the expected number of products : {str(expected_number_of_products)}.'
logging.info(f'   The response products number {len(response_json["products"])} is the same as the expected total number of products : {str(expected_number_of_products)}.')
# 2. How many smartphones are in the response, in Product/Categories, compared to a known value.
total_smartphones = 0
expected_number_of_smartphones = 5
for value in response_json["products"]:
    if value["category"] == "smartphones":
        total_smartphones += 1
logging.info('   # 2. How many smartphones are as value in Product/Categories.')
assert expected_number_of_smartphones == total_smartphones, f'The returned smartphones number :{total_smartphones} is not the expected number total of smartphones : {str(expected_number_of_smartphones)}.'
logging.info(f'   The available smartphones number of {total_smartphones} is the same as the expected total number of smartphones : {expected_number_of_smartphones}.')
# 3. All Product/Categories="Laptops" have Product/Price < 2000.
price_to_compare = 2000
laptop_more_expensive_ID = []
total_laptops = 0
for value in response_json["products"]:
    if value["category"] == "laptops":
        total_laptops += 1
        if value["price"] >= price_to_compare:
            laptop_more_expensive_ID.append(value["id"])
logging.info('   # 3. All Product/Categories="Laptops" have Product/Price < 2000.')
assert not(len(laptop_more_expensive_ID)), f'There is/are {len(laptop_more_expensive_ID)} laptops with ID_value/s :{laptop_more_expensive_ID}, that cost more than {price_to_compare}.'
#print(bool(laptop_more_expensive))
logging.info(f'   All {total_laptops} laptops will cost less than the expectec value : {price_to_compare}.')
# 4. All Products keys have a value.
for j_object in response_json["products"]:
    for key,value in j_object.items():
        if not value:
            raise MyException(f'In product/id : "{j_object["id"]}", have found a key value that is empty : "{key}"')
index += 1
worksheet.write(xls_format["Type"] + str(index), 'GET')
worksheet.write(xls_format["EndPoint"] + str(index), URL+endpoint)
worksheet.write(xls_format["Status"] + str(index), r.status_code)
worksheet.write(xls_format["Verifications"] + str(index), 'OK')



# Do a POST where the response is always hardcoded to 201 and there is no real Update in DB
logging.info('### 2 ########################################')
URL = 'https://jsonplaceholder.typicode.com'
endpoint = '/posts'
logging.info('   ### POST ### : ' + URL + endpoint)
logging.info('   ENDPOINT : ' + endpoint)
response_json = r.json()
file = open('Bodies/products_add_normal_body.txt', 'r')
payload = json.load(file)
r = requests.post(url=URL + endpoint,
                    timeout=10,
                    json=payload)
logging.info('   Reponse headers : ')
for key,value in r.headers.items():
    logging.info('      ' + key + ' : ' + value)
logging.info('   End of reponse headers.')
#Verify Responsse status code = 201
assert r.status_code == 201, f'The Reponse status code: {r.status_code} is not the expected 201 value.'
logging.info('   POST payload: ')
logging.info('   ' + str(payload))
logging.info('   Reponse: ' + str(r.status_code))
index += 1
worksheet.write(xls_format["Type"] + str(index), 'POST')
worksheet.write(xls_format["EndPoint"] + str(index), URL+endpoint)
worksheet.write(xls_format["Status"] + str(index), r.status_code)
worksheet.write(xls_format["Verifications"] + str(index), 'OK')

workbook.close()


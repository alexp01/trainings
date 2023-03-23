# In this exemple we call a SOAP and we do some parsing in the response.
# As the response is limited I will create Exemple02 with a bigger xml content but there i use another library to parse.
# I have created exemple03 to parse with BeautifulSoup

import requests
from bs4 import BeautifulSoup

# SOAP request URL
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

# structured XML
payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
            <soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
                <soap:Body>
                    <CountryIntPhoneCode xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
                        <sCountryISOCode>FR</sCountryISOCode>
                    </CountryIntPhoneCode>
                </soap:Body>
            </soap:Envelope>"""
# headers
headers = {
    'Content-Type': 'text/xml; charset=utf-8'
}
# POST request
response = requests.request("POST", url, headers=headers, data=payload)

# prints the response
print(response.text)
print(response)

#Response exemple
''' 
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <m:CountryIntPhoneCodeResponse xmlns:m="http://www.oorsprong.org/websamples.countryinfo">
      <m:CountryIntPhoneCodeResult>33</m:CountryIntPhoneCodeResult>
    </m:CountryIntPhoneCodeResponse>
  </soap:Body>
</soap:Envelope>
<Response [200]>
'''

#Parsing the xml response
# Exemple found in https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/
Bs_data = BeautifulSoup(response.text, "xml")

print('### First xml parse and display of result')

# Finding all instances of tag
# `CountryIntPhoneCodeResponse`
# In case there are more than one tags `CountryIntPhoneCodeResponse` then all of them will be found and their content stored in a variable
tag_value = Bs_data.find_all('CountryIntPhoneCodeResponse')

print(tag_value)

# The tag_value will just print the tag content for 'CountryIntPhoneCodeResponse'
# Only 1 instance of this tag was found.
'''
[<m:CountryIntPhoneCodeResponse xmlns:m="http://www.oorsprong.org/websamples.countryinfo">
<m:CountryIntPhoneCodeResult>33</m:CountryIntPhoneCodeResult>
</m:CountryIntPhoneCodeResponse>]
'''

print('### Second xml parse and display of result')
tag_value = Bs_data.find_all('CountryIntPhoneCodeResult')
print(tag_value)
# The tag_value will just print the tag content for 'CountryIntPhoneCodeResult'
# Only 1 instance of this tag was found.
'''
[<m:CountryIntPhoneCodeResult>33</m:CountryIntPhoneCodeResult>]
'''

print('eee')
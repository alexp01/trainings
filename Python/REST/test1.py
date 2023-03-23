import requests

# Do a Get and check some things in the response json converted to dict.
r = requests.get('https://jsonplaceholder.typicode.com/posts')
print("### This is the first GET Type")
print(r.status_code) # get the response status code
print(r.text) # get the body response

json_converted_to_dict = r.json()

for dict_object in json_converted_to_dict:
    if dict_object['userId'] == 5 :
        print (dict_object)

# Do a POST where the response is always hardcoded to 201 and there is no real Update in DB
payload = {
    "title": "new type of iPhone",
    "description": "An apple mobile which is nothing like apple",
    "price": 999,
    "discountPercentage": 11.96,
    "rating": 4.69,
    "stock": 94,
    "brand": "Apple",
    "category": "smartphones",
    "thumbnail": "https://i.dummyjson.com/data/products/1/thumbnail.jpg",
    "images": [
            "https://i.dummyjson.com/data/products/1/1.jpg",
            "https://i.dummyjson.com/data/products/1/2.jpg",
            ]
  }
res = requests.post(url="https://jsonplaceholder.typicode.com/posts",
                    timeout=10,
                    json=payload)


# Another way to call a GET
r2 = requests.request("GET", 'https://jsonplaceholder.typicode.com/posts', timeout=10)
print("### This is the second GET Type")
print(r2.status_code)
print(r2.text)

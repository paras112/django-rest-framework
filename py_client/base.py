import requests
endpoint="http://httpbin.org/anything"
response=requests.get(endpoint)
# print(response.text) #printing json
print(response.json())
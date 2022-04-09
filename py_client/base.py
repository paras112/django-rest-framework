import requests
# endpoint="http://httpbin.org/anything"
endpoint="http://localhost:8000/"
response=requests.get(endpoint)
# print(response.text) #printing json
print(response.json())
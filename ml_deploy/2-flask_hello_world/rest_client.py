import json
import requests

url = 'http://127.0.0.1:5000/hello_world'

data = {'model':'knn'}
request_data = json.dumps(data)
response = requests.post(url,request_data)
print (response.text)


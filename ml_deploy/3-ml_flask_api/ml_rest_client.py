import json
import requests

url = 'http://127.0.0.1:8005/model'

request_data = json.dumps({'age': 42, 'salary':50000})
response = requests.post(url,request_data)
response
output_dict = json.dumps(response.text)

with open("output.json", "w") as file:
    file.write(output_dict)


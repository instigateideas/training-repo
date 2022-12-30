import json
import requests

url = 'http://127.0.0.1:8005/nlp_model'

data = {"sample": "the hotel food was too good and tasty"}
request_data = json.dumps(data)
response = requests.post(url,request_data)
print(response.text)


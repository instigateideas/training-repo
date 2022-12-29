import json
import requests

url = 'http://127.0.0.1:5000/model'

data = {"Pclass": 2, "Sex": 1, "Age": 24, "SibSp": 1, "Fare": 8.12}
request_data = json.dumps(data)
response = requests.post(url,request_data)
print(response.text)


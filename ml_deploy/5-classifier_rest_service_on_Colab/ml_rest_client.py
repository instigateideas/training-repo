import json
import requests

url = 'http://8537-35-186-160-155.ngrok.io/predict/'

request_data = json.dumps({'age':40,'salary':20000})
response = requests.post(url, request_data)
print (response.text)




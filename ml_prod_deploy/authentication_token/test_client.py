import json
import requests

host = "http://127.0.0.1:5000"

def register_user(name, password):
    headers = {"Content-Type": "application/json"}
    request_data = json.dumps({"name": name, "password": password})
    register_url = f"{host}/register"
    response = requests.post(url=register_url, data=request_data, headers=headers)
    msg = json.loads(response.text)
    print(msg["message"])

def list_users():
    list_register_url = f"{host}/users"
    response = requests.get(url=list_register_url)
    msg = json.loads(response.text)

    print("Registered users are: ")
    for num, user in enumerate(msg["users"]):
        print(f"{num}. {user['name']}")
  
def login_to_api(username, password):
    login_url = f"{host}/login"
    response = requests.get(url=login_url,auth=(username, password))
    msg = json.loads(response.text)
    print("Successfully Logged in..")

    return msg["token"]

def get_prediction(data, token):
    request_data = json.dumps(data)
    headers = {"Content-Type": "application/json", "x-access-tokens": token}
    predict_url = f"{host}/predict"
    response = requests.post(url=predict_url,data=request_data, headers=headers)
    pred_resp = json.loads(response.text)
    prediction = pred_resp["prediction"]
    print(f"Prediction is {prediction}")

    return prediction    


data = {"Sepal_Length": 5, "Sepal_Width": 4, "Petal_Length": 1.3, "Petal_Width": 0.3}
# register_user(name="mrx", password="Yah@1245")
# list_users()
token = login_to_api(username="anthony", password="Read@123")
prediction = get_prediction(data=data, token=token)


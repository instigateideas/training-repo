from flask import Flask, request
import pickle
from tensorflow.keras.models import load_model
import numpy as np

local_scaler = pickle.load(open('sc.pickle','rb'))
cust_model = load_model('consumer_behavior_model/1/')

app = Flask(__name__)

@app.route('/model',methods=['POST'])
def hello_world():
    request_data = request.get_json(force=True)
    age = request_data['age']
    salary = request_data['salary']
    predicted_output = cust_model.predict(local_scaler.transform(np.array([[age, salary]])))[:,1]

    return "The prediction is {}".format(predicted_output)

if __name__ == "__main__":
    app.run(port=8005, debug=True)


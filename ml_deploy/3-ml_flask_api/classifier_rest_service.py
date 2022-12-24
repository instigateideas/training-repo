from flask import Flask, request
import pickle
import numpy as np
from flask import jsonify

local_classifier = pickle.load(open('classifier.pickle','rb'))
local_scaler = pickle.load(open('sc.pickle','rb'))

app = Flask(__name__)

@app.route('/model',methods=['POST'])
def ml_model():
    request_data = request.get_json(force=True)
    age = request_data['age']
    salary = request_data['salary']
    pred_proba = local_classifier.predict(local_scaler.transform(np.array([[age, salary]])))
    pred_proba = {"prediction": int(pred_proba)}
    return jsonify(pred_proba)

if __name__ == "__main__":
    app.run(port=8005, debug=True)
    
    
    

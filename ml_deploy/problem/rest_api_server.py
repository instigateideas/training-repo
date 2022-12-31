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
    # 'Pclass', 'Sex', 'Age', 'SibSp', 'Fare'
    pclass = request_data['Pclass']
    sex = request_data['Sex']
    age = request_data['Age']
    sibsp = request_data['SibSp']
    fare = request_data['Fare']
    pred_proba = local_classifier.predict(local_scaler.transform(np.array([[pclass, sex, age, sibsp, fare]])))
    pred_proba = {"prediction": int(pred_proba)}
    return jsonify(pred_proba)


if __name__ == "__main__":
    app.run(port=8005, debug=True)
    
    
    

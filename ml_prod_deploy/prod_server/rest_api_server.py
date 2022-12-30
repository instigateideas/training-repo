from flask import Flask, request, render_template, abort
import pickle
import numpy as np
from flask import jsonify
import logging

logging.basicConfig(level=logging.DEBUG, filename="app_server.log", filemode='a', \
    format='%(name)s - %(levelname)s - %(asctime)s - %(message)s')

ALLOWED_IPS = ['192.168.1.', '127.0.0.1']

local_classifier = pickle.load(open('./pickle_files/classifier.pickle','rb'))
local_scaler = pickle.load(open('./pickle_files/sc.pickle','rb'))

app = Flask(__name__)

@app.errorhandler(403)
def permission_error(e):
    logging.info("you don't have the neccessary permission to access the API")
    return render_template('403.html', error_code=403)

@app.before_request
def limit_remote_addr():
    client_ip = str(request.remote_addr)
    valid = False
    for ip in ALLOWED_IPS:
        if client_ip.startswith(ip) or client_ip == ip:
            valid = True
            logging.info(f"IP: {client_ip} address is allowed")
            break
    if not valid:
        logging.warning(f"IP: {client_ip} address is blocked..!!!")
        abort(403)

@app.route('/model',methods=['POST'])
def ml_model():
    try:
        request_data = request.get_json(force=True)
        pclass = request_data['Pclass']
        sex = request_data['Sex']
        age = request_data['Age']
        sibsp = request_data['SibSp']
        fare = request_data['Fare']
        pred_proba = local_classifier.predict(local_scaler.transform(np.array([[pclass, sex, age, sibsp, fare]])))
        pred_proba = {"prediction": int(pred_proba)}
        logging.info("Prediction successfull")
        return jsonify(pred_proba)
    except Exception as e:
        logging.error(f"Check the data passed to the API server from client")
        return jsonify({"prediction": "Error in the data sent"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
    
    

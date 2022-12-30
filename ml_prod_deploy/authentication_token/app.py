from flask import Flask, request, jsonify, make_response, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime
from functools import wraps
import pickle
import logging
import numpy as np
import warnings
warnings.filterwarnings('ignore')

logging.basicConfig(level=logging.DEBUG, filename="app_server.log", filemode='a', \
    format='%(name)s - %(levelname)s - %(asctime)s - %(message)s')

# Load the model files and IP Restriction
model = pickle.load(open("model.pkl", "rb"))
ALLOWED_IPS = ['192.168.1.', '127.0.0.1']

# Configurations
app = Flask(__name__)
app.config['SECRET_KEY']='Th1s1ss3cr3t'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite://///home/arunachalamdharmaraj/Documents/training-repo/ml_prod_deploy/authentication_token/register.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Users(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     public_id = db.Column(db.Integer)
     name = db.Column(db.String(50))
     password = db.Column(db.String(50))
     admin = db.Column(db.Boolean)

## Create the Model - push model to be created outside the app
app.app_context().push()

# IP Restrict Function
@app.before_request
def limit_remote_addr():
    valid = False
    for ip in ALLOWED_IPS:
        client_ip = str(request.remote_addr)
        if client_ip.startswith(ip) or client_ip == ip:
            valid = True
            logging.info(f"IP: {client_ip} address is allowed")
            break
    if not valid:
        logging.warning(f"IP: {client_ip} address is blocked..!!!")
        abort(403)

## Function to allow the registered users
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = Users.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)

    return decorator

# Register user API method
@app.route('/register', methods=['GET', 'POST'])
def signup_user():  
    data = request.get_json()  

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = Users(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password, admin=False) 
    db.session.add(new_user)  
    db.session.commit()    

    return jsonify({'message': 'registered successfully'})

# Login user API method
@app.route('/login', methods=['GET', 'POST'])  
def login_user(): 
    auth = request.authorization

    if not auth or not auth.username or not auth.password:  
        return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})    

    user = Users.query.filter_by(name=auth.username).first()
        
    if check_password_hash(user.password, auth.password):  
        token = jwt.encode({'public_id': user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])  
        return jsonify({'token' : token}) 

    return make_response('could not verify',  401, {'WWW.Authentication': 'Basic realm: "login required"'})

## See the list of users registered
@app.route('/users', methods=['GET'])
def get_all_users():  
    users = Users.query.all() 
    result = []   

    for user in users:   
        user_data = {}   
        user_data['public_id'] = user.public_id  
        user_data['name'] = user.name 
        user_data['password'] = user.password
        user_data['admin'] = user.admin 
        
        result.append(user_data)   

    return jsonify({'users': result})


@app.route("/")
def Home():
    client_ip = str(request.remote_addr)
    logging.info(f"IP: {client_ip} accesed the Home page")
    return render_template("index.html")


## Predict the data
@app.route('/predict', methods=['POST', 'GET'])
@token_required
def predict(current_user):
    client_ip = str(request.remote_addr)
    if request.method == "GET":
        return render_template("index.html", prediction_text="Please fill the form to Predict")
    if request.method == "POST":
        if list(request.form.values()) != []:
            float_features = [float(x) for x in request.form.values()]
            features = [np.array(float_features)]
            prediction = model.predict(features)[0]
            logging.info(f"User: {current_user.name} accessed ML API from Machine of IP: {client_ip} using front-end")
            return render_template("index.html", prediction_text = "The flower species is {}".format(prediction))
        else:
            request_data = request.get_json(force=True)
            sepal_length = request_data['Sepal_Length']
            sepal_width = request_data['Sepal_Width']
            petal_length = request_data['Petal_Length']
            petal_width = request_data['Petal_Width']
            features = [np.array([sepal_length, sepal_width, petal_length, petal_width])]
            prediction = model.predict(features)[0]
            logging.info(f"User: {current_user.name} accessed ML API from Machine of IP: {client_ip}")

            return jsonify({"prediction": prediction})


if  __name__ == '__main__':  
     app.run(port=5000, debug=True)
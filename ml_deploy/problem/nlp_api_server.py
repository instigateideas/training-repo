from flask import Flask, request
import pickle
import numpy as np
from flask import jsonify

text_classifier = pickle.load(open('textclassifier.pickle','rb'))
tfidf_model = pickle.load(open('tfidfmodel.pickle','rb'))

app = Flask(__name__)

@app.route('/nlp_model',methods=['POST'])
def ml_model():
    request_data = request.get_json(force=True)
    txt = [request_data['sample']]
    pred_proba = text_classifier.predict(tfidf_model.transform(txt).toarray())
    pred_proba = {"prediction": int(pred_proba)}
    return jsonify(pred_proba)

if __name__ == "__main__":
    app.run(port=8005, debug=True)
    
    
    

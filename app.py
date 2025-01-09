import pickle
from flask import Flask, request, app, jsonify,url_for,render_template 
import numpy as np
import pandas as pd
app = Flask(__name__)

# load model
lrmodel = pickle.load(open('lr_model.pkl','rb'))
scaler = pickle.load(open('transformation_pipeline.pkl','rb'))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods= ['POST']) # for testing api with postman
def predict_api():
    data = request.json['data'] # fetching data key in json
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output = lrmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods= ['POST'])
def predict():
    data = [float(x) for x in request.form.values()] # feticing data from html form
    new_data = scaler.transform(np.array(data).reshape(1,-1))
    print(new_data)
    output = lrmodel.predict(new_data)[0]
    print(output)
    return render_template('home.html',prediction_text=output)

if __name__=='__main__':
    app.run(debug=True)
    
    
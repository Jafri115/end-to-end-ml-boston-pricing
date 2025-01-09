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


@app.route('/predict',methods= ['POST'])
def predict():

    output = 10
    return render_template('home.html',prediction_text=output)

if __name__=='__main__':
    app.run(debug=True)
    
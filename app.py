import pickle
from flask import Flask, request, app, jsonify,url_for,render_template 
import numpy as np
import pandas as pd
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict',methods= ['POST'])
def predict():

    output = 10
    return render_template('home.html',prediction_text=output)

if __name__=='__main__':
    app.run(debug=True)
    
    
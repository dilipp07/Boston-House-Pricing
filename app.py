import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)

#LOAD MODEL
regmodel=pickle.load(open("regmodel.pkl",'rb'))
scaler=pickle.load(open("scaling.pkl",'rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['Post'])

def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    
    output=regmodel.predict(scaler.transform(np.array(list(data.values())).reshape(1,-1)))    
    print(output[0])
    return jsonify(output[0])
if __name__=='__main__':
    app.run(debug=True)





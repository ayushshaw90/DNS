from flask import Flask, request, jsonify
import pickle
import numpy as np
from config import Config
import pandas as pd
from domain_name_preprocessor import get_feature_rich_row

app = Flask(__name__)

app.config.from_object(Config)

@app.route('/')
def home():
    return "Hello World"


@app.route('/predict', methods=['POST'])
def predict():
    
     domain_name = request.form.get('domain_name')
   
     preprocessed_data = get_feature_rich_row(domain_name)
     df = pd.DataFrame(preprocessed_data,index=[0])
     df['label'] = 0

     with open('models/dga_tld_encoder.pkl', 'rb') as encoder_file:
         encoder = pickle.load(encoder_file)

     encoded_data = encoder.transform(df)

     encoded_data = encoded_data.drop(['label'], axis=1)

     with open('models/dga_feature_scaler.pkl', 'rb') as scalar_file: 
         scalar = pickle.load(scalar_file)

     scaled_data = scalar.transform(encoded_data)

     with open('models/dga_svm_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
     
     predict = model.predict(scaled_data)[0]

     if predict == 0:
         result = 'LEGITIMATE DOMAIN NAME'
     else:
         result = 'DGA DOMAIN NAME'
    
     return jsonify({'prediction': str(result)})

if __name__ == '__main__':
    app.run(debug=True)
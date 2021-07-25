import os
import pickle
import pandas as pd
from flask import Flask, request, Response
from CardioCatch.Cardio_Catch import cardio_catch

# loading model
model = pickle.load(open('model/cardio_catch_model.pkl', 'rb'))

# initialize API
app = Flask(__name__)

@app.route('/cardio_catch/predict', methods=['POST'])

def cardio_catch_predict():
    test_json = request.get_json()
    
    if test_json:
        # Unique Example
        if isinstance(test_json, dict):
            test_raw = pd.DataFrame(test_json, index=[0])
        # Multiple Example
        else:
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())
            
        # Instantiate cardio_catch_class
        pipeline = cardio_catch()
        
        # rename columns
        df1 = pipeline.rename_columns(test_raw)
        
         # feature engineering
        df2 = pipeline.feature_engineering(df1)
        
         # data preparation
        df3 = pipeline.data_preparation(df2)
        
         # prediction
        df_response = pipeline.get_prediction(model, test_raw, df3)
        
        return df_response
    
    else:
        return Response('{}', status=200, mimetype='application/json')

if __name__ == '__main__':
	port = os.environ.get('PORT', 5000)
	app.run(host='0.0.0.0', port=port)

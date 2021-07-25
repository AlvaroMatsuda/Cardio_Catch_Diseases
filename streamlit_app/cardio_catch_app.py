import streamlit as st
import pandas as pd
import numpy as np
import json
import datetime
import requests
import json

# Page configuration
st.set_page_config(page_title='Cardio_Catch_App', layout='centered')

st.title('Patient Profile')


def form():
	# PATIENT PROFILE
	# age_days
	st.subheader('Birthday')
	birthday = st.date_input(label='', min_value=datetime.date(1900, 1, 1))
	now = datetime.datetime.today()
	now = now.date()
	age = (now - birthday).days

	# gender
	st.subheader('Gender')
	gender = st.selectbox(label='', options=['Select', 'Male', 'Female'])

	# height
	st.subheader('Height (cm)')
	height = int(st.text_input(label='', value=0, max_chars=3, help='Example: 170'))

	# weight
	st.subheader('Weight (kg)')
	weight = float(st.text_input(label='', value=0, max_chars=4, help='Example: 70.5'))

	# smoke (yes or no)
	st.subheader('Smoke')
	smoke = st.selectbox(label='', options=['Select', 'Yes', 'No'], key='smoke')

	# alcohol (yes or no)
	st.subheader('Drink Alcohol')
	alcohol = st.selectbox(label='', options=['Select', 'Yes', 'No'])

	# active (frequency in a week)
	st.subheader('How Often do You Exercise in a Week')
	active_freq = int(st.number_input(label='', min_value=0, max_value=7))

	# cholesterol
	st.subheader('Total Cholesterol (mg/dL)')
	cholesterol_value = int(st.text_input(label='', value=0, max_chars=3, help='Example: 180'))

	# glucose
	st.subheader('Total Glucose (mg/dL)')
	glucose_value = int(st.text_input(label='', value=0, max_chars=3, help='Example: 125'))

	# Blood Pressure
	st.header('Blood Pressure')

	col1, col2 = st.beta_columns(2)

	with col1:
		# systolic_bp
		st.subheader('Systolic Blood Pressure')
		systolic_bp = int(st.text_input(label='', value=0, max_chars=3, help='Example: 120'))
		
	with col2:
		# diastolic_bp
		st.subheader('Diastolic Blood Pressure')
		diastolic_bp = int(st.text_input(label='', value=0, max_chars=3, help='Example: 80'))
		
	data_form = pd.DataFrame([age, gender, height, weight, systolic_bp, diastolic_bp, cholesterol_value, glucose_value, smoke, alcohol, active_freq], index=['age_days', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active']).T
	
	return data_form

def feature_engineering(data):
	# FEATURE ENGINEERING
	# cholesterol (1=normal, 2=above normal, 3 well above normal)
	data['cholesterol'] = data['cholesterol'].apply(lambda x: 1 if x <= 200 else 2 if x <=240 else 3)

	# gluc (1=normal, 2=above normal, 3 well above normal)
	data['gluc'] = data['gluc'].apply(lambda x: 1 if x <= 125 else 2 if x <=200 else 3)

	# active (1 = active, 0 = not active)
	data['active'] = data['active'].apply(lambda x: 1 if x >= 3 else 0)

	return data
	


# SAVING DATA
#patient_info = pd.DataFrame([age, gender, height, weight, systolic_bp, diastolic_bp, cholesterol, glucose, smoke, alcohol, active], index=['age_days', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active']).T

def predict(data):
	# GET PREDICTION
	st.header('Get Prediction')

	if st.button(label='Predict'):
		# Loading Data
		#pred = pd.read_json(data)
		data = json.dumps(data.to_dict(orient='records'))
		
		# API Call
		url = 'https://cardio-catch-prediction.herokuapp.com/cardio_catch/predict'
		header = {'Content-type': 'application/json'}
		data = data
		r = requests.post(url, data=data, headers=header)

		prediction = pd.DataFrame(r.json(), columns=r.json()[0].keys())
		
		return st.write(prediction)




#################################
###ETL
#################################

# Extract Patient Infos
patient_infos = form()

# Transform
df1 = feature_engineering(patient_infos)

st.header('Patient Infos')
st.dataframe(data=df1)

# Predict
predict(df1)




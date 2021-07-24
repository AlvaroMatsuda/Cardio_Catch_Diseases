import pickle
import pandas as pd

class cardio_catch(object):
    def __init__(self):
        self.home_path = '/home/kazu/Repos/Cardio_Catch_Diseases/pa001_cardio_catch_diseases/'
        self.age_days_scaler = pickle.load(open(self.home_path + 'parameters/age_days_scaler.pkl', 'rb'))
        self.age_year_scaler = pickle.load(open(self.home_path + 'parameters/age_year_scaler.pkl', 'rb'))
        self.bmi_scaler = pickle.load(open(self.home_path + 'parameters/bmi_scaler.pkl', 'rb'))
        self.systolic_bp_scaler = pickle.load(open(self.home_path + 'parameters/systolic_bp_scaler.pkl', 'rb'))
        self.diastolic_bp_scaler = pickle.load(open(self.home_path + 'parameters/diastolic_bp_scaler.pkl', 'rb'))
        self.height_scaler = pickle.load(open(self.home_path + 'parameters/height_scaler.pkl', 'rb'))
        self.weight_scaler = pickle.load(open(self.home_path + 'parameters/weight_scaler.pkl', 'rb'))

    # RENAMING COLUMNS
    def rename_columns(self, df1):
        
        df1 = df1.rename(mapper={'age': 'age_days',
                                 'ap_hi': 'systolic_bp',
                                 'ap_lo': 'diastolic_bp'}, axis=1)

        return df1

    # Feature Engineering
    def feature_engineering(self, df2):

        # calculating BMI
        df2['bmi'] = df2['weight'] / (df2['height'] / 100)**2

        # age_year
        df2['age_year'] = (df2['age_days'] / 365).astype('int')

        # blood_pressure classification
        df2['bp_class'] = ['normal' if (systolic_bp < 120) & (diastolic_bp < 80) else
                           'elevated' if ((systolic_bp >= 120) & (systolic_bp <= 129)) & (diastolic_bp < 80) else
                           'hypertension 1' if ((systolic_bp >= 130) & (systolic_bp <= 139)) | ((diastolic_bp >= 80) & (diastolic_bp <= 89)) else
                           'hypertension 2' for systolic_bp, diastolic_bp in zip(df2['systolic_bp'], df2['diastolic_bp'])]

        # bmi_class
        df2['bmi_class'] = df2['bmi'].apply(lambda x: 'underweight' if x <= 20
                                           else 'health' if x < 25
                                           else 'overweight' if x < 30
                                           else 'obese' if x < 40
                                           else 'extreme obese')    



        # rearrenge columns
        df2 = df2[['age_days', 'age_year', 'gender', 'height', 'weight', 'bmi', 'bmi_class', 'systolic_bp',
               'diastolic_bp', 'bp_class', 'cholesterol', 'gluc', 'smoke', 'alco', 'active']]

        return df2

    def data_preparation(self, df3):
        ## RESCALING
        # age_days
        df3['age_days'] = self.age_days_scaler.transform(df3[['age_days']].values);
        
        # age_years
        df3['age_year'] = self.age_year_scaler.transform(df3[['age_year']].values);

        # bmi
        df3['bmi'] = self.bmi_scaler.transform(df3[['bmi']].values);
        
        # systolic_bp
        df3['systolic_bp'] = self.systolic_bp_scaler.transform(df3[['systolic_bp']].values);
        
        # diastolic_bp
        df3['diastolic_bp'] = self.diastolic_bp_scaler.transform(df3[['diastolic_bp']].values);
        
        # height
        df3['height'] = self.height_scaler.transform(df3[['height']].values);
        
        # weight
        df3['weight'] = self.weight_scaler.transform(df3[['weight']].values);
        
        ## ENCODING
        # One Hot Encoding -> gender (1=woman -> 1, 2=man -> 0)
        df3['gender'] = df3['gender'].apply(lambda x: 0 if x == 2 else 1)

        # ordinal Encoding -> bmi_class, bp_class
        # bmi_class
        bmi_class_dict = {'underweight': 1,
                          'health': 2,
                          'overweight': 3,
                          'obese': 4,
                          'extreme obese': 5}
        
        df3['bmi_class'] = df3['bmi_class'].map(bmi_class_dict)

        # bp_class
        bp_class_dict = {'normal': 1,
                         'elevated': 2,
                         'hypertension 1': 3,
                         'hypertension 2': 4}
        
        df3['bp_class'] = df3['bp_class'].map(bp_class_dict)
        
        ## FEATURE SELECTION
        # Columns Selected
        cols_selected = ['age_days','bmi', 'height', 'weight', 'systolic_bp', 'diastolic_bp', 'cholesterol']
        
        return df3[cols_selected]
    
    def get_prediction(self, model, original_data, test_data):
        # prediction
        pred = model.predict(test_data)
        
        # join pred into original data
        original_data['prediction'] = pred
        
        return original_data.to_json(orient='records')

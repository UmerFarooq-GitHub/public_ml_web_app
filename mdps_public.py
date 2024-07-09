# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 01:36:01 2024

@author: PMYLS
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('heart_prediction_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb')) 

with st.sidebar:
    selected = option_menu('Mulitple Disease Prediction System',
                            ['Diabetes Prediction System','Heart Disease Prediction System','Parkinsons Prediction System'],
                            icons = ['activity', 'heart', 'person'],
                            default_index = 0)

if(selected == 'Diabetes Prediction System'):
    st.title('Diabetes Prediction System')
    
    #creating columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI Value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    diabetes_diagnosis = ''
    
    with col2:
        if st.button('Check Diabetes'):
            diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
            if (diabetes_prediction[0]==1):
                diabetes_diagnosis = 'The person is Diabetic'
            
            else:
                diabetes_diagnosis = 'The person is Non Diabetic'
            
    st.success(diabetes_diagnosis)
    
if(selected == 'Heart Disease Prediction System'):
    st.title('Heart Disease Prediction System')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.number_input('Age')
    
    with col2:
        sex = st.number_input('Sex')
    
    with col3:
        cp = st.number_input('Chest Pain Type')
    
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
    
    with col2:
        chol = st.number_input('Serum Cholesterol')
    
    with col3:
        fbs = st.number_input('Fasting Blood Sugar')
    
    with col1:
        restecg = st.number_input('Resting Electrocardiographic Results')
    
    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved')
    
    with col3:
        exang = st.number_input('Exercise Induced Angina')
    
    with col1:
        oldpeak = st.number_input('ST segment depression')
    
    with col2:
        slope = st.number_input('Slope of peak exercise ST segment')
    
    with col3:
        ca = st.number_input('Number of major vessels colored by fluoroscopy')
    
    with col1:
        thal = st.number_input('Thallium Stress Test Result')

    heart_disease_diagnosis = ''
     
    with col2: 
         if st.button('Check Heart Disease'):
             heart_disease_prediction = heart_model.predict([[Age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
             
         
             if (heart_disease_prediction[0]==1):
                 heart_disease_diagnosis = 'Person has the Heart Disease'
             
             else:
                 heart_disease_diagnosis = 'Person doesnot have the Heart Disease'
             
    st.success(heart_disease_diagnosis)
     
if(selected == 'Parkinsons Prediction System'):
    st.title('Parkinsons Prediction System')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        MDVP_Fo_Hz = st.text_input('Fundamental Frequency (Hz)')
    with col2:
            MDVP_Fhi_Hz = st.text_input('Maximum Frequency (Hz)')
    with col3:
        MDVP_Flo_Hz = st.text_input('Minimum Frequency (Hz)')

    with col1:
        MDVP_Jitter_percent = st.text_input('Jitter (%)')
    with col2:
        MDVP_Jitter_Abs = st.text_input('Jitter (Absolute)')
    with col3:
        MDVP_RAP = st.text_input('RAP (Relative Amplitude Perturbation)')

    with col1:
        MDVP_PPQ = st.text_input('PPQ (Pitch Period Perturbation Quotient)')
    with col2:
        Jitter_DDP = st.text_input('DDP (Degree of Deviation from Periodicity)')
    with col3:
        MDVP_Shimmer = st.text_input('Shimmer')

    with col1:
        MDVP_Shimmer_dB = st.text_input('Shimmer (dB)')
    with col2:
        Shimmer_APQ3 = st.text_input('APQ3 (Three-Point Amplitude Perturbation Quotient)')
    with col3:
        Shimmer_APQ5 = st.text_input('APQ5 (Five-Point Amplitude Perturbation Quotient)')

    with col1:
        MDVP_APQ = st.text_input('APQ (Amplitude Perturbation Quotient)')
    with col2:
        Shimmer_DDA = st.text_input('DDA (Average Absolute Differences of Periodic Amplitudes)')
    with col3:
        NHR = st.text_input('NHR (Noise-to-Harmonics Ratio)')

    with col1:
        HNR = st.text_input('HNR (Harmonics-to-Noise Ratio)')
    with col2:
        RPDE = st.text_input('RPDE (Recurrence Period Density Entropy)')
    with col3:
        DFA = st.text_input('DFA (Detrended Fluctuation Analysis)')

    with col1:
        spread1 = st.text_input('Spread1 (Nonlinear Measure of Fundamental Frequency)')
    with col2:
        spread2 = st.text_input('Spread2 (Nonlinear Measure of Fundamental Frequency)')
    with col3:
        D2 = st.text_input('D2 (Nonlinear Measure of Fundamental Frequency)')

    with col1:
        PPE = st.text_input('PPE (Pitch Period Entropy)')

# Prediction
    parkinsons_diagnosis = ''

    if st.button('Check Parkinsons Disease'):
         parkinsons_disease_prediction = parkinsons_model.predict([[MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP,
                      MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
         
         if (parkinsons_disease_prediction[0]==1):
             parkinsons_diagnosis = 'Person has the Parkinsons Disease'
         
         else:
             parkinsons_diagnosis = 'Person does not have the Parkinsons Disease'
         
    st.success(parkinsons_diagnosis)
    
    
    

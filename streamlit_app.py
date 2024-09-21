# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:20:18 2024

@author: Lenovo
"""

import pickle
import streamlit as st
import streamlit_option_menu
from streamlit_option_menu import option_menu

# Loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           icons=['activity', 'heart'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # Page title
    st.title('Diabetes Prediction using ML')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
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
        Age = st.text_input("Age of the Person")

    # Code for prediction
    diab_diagnosis = ''

    # Creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # Page title
    st.title('Heart Disease Prediction using ML')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain Type (cp)')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure (Trestbps)')
    with col2:
        chol = st.text_input('Serum Cholesterol (chol)')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar (fbs)')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results (restecg)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved (thalach)')
    with col3:
        exang = st.text_input('Exercise Induced Angina (exang)')
    with col1:
        oldpeak = st.text_input('Oldpeak')
    with col2:
        slope = st.text_input('Slope')
    with col3:
        ca = st.text_input('Number of Major Vessels (ca)')
    with col1:
        thal = st.text_input('Thalassemia (thal)')

    # Code for prediction
    heart_diagnosis = ''

    # Creating a button for prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has a high risk of heart disease'
        else:
            heart_diagnosis = 'The person does not have a high risk of heart disease'

    st.success(heart_diagnosis)

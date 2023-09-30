# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu


df = pd.read_csv("diabete_cleaned.csv")

#random_forest = joblib.load('diabete_prediction.sav')
# loading the saved model
loaded_model = pickle.load(open('diabete_prediction.sav', 'rb'))

def predict(input_data):
    
    my_array = np.array(input_data)
    input_reshaped = my_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_reshaped)
    
    
    
    if (prediction[0] == 0):
        st.success("The person has no diabets")
    else:
        st.error("the person is diabetic")
        st.success(prediction)
        
    
def main():
       
    with st.sidebar:
        selected = option_menu ('Multiple Diabete Prediction System',
                            
                            ['Home',
                             'Diabete Prediction',
                            'Dataset label encoded',
                            'Author',
                            ],
                            icons = ['house','bi bi-file-medical-fill','person','book'],
                            default_index=0
    
                            )
    
    if(selected == "Home") :
        st.title("Diabetes Prediction Using Machine Learning")
        
        st.subheader("Author : LAGRE GABBA BERTRAND")
        st.write(" I am happy to see you reading my work. TThe objective of the dataset is to diagnostically predict whether a patient has diabetes based on certain diagnostic measurements included in the dataset. Several constraints were placed on the selection of these instances from a larger database. As data analyst intern at MeriSkill , I am building and a Machine Learning Model to preditc if a person is diabetic or no..")
        st.subheader("Github link  : https://github.com/FoubaDev/MeriSkills.git \n")
       
    if(selected == "Dataset label encoded") :
        st.write(df)
        st.write(df.shape)
    if(selected == "Diabete Prediction") :
    
       
        col1, col2,col3,col4 = st.columns(4)
    
        with col1:
            pregnancies = st.number_input('Pregnancies',key=1,min_value = 0)
    
        with col2:
           glucose = st.number_input('Glucose', min_value=0)   
            
        with col3:
            
            blood_pressure = st.number_input('BloodPressure',min_value=0)

        with col4:
        
            skinThickness = st.number_input('SkinThickness',min_value=0)
    
        with col1:
        
            insulin = st.number_input('Insulin',min_value=0)
            
        with col2 :
            
            bmi = st.number_input('BMI',min_value=0.0,step=0.01)
    
        with col3 :
          
            diabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction',min_value=0.000,format="%.3f",step=0.001) 
    
        with col4:
        
            age = st.number_input('Age',key=2,min_value = 0)
    
        diabete = ''
        
        data = (pregnancies,glucose,blood_pressure,skinThickness,insulin,bmi,diabetesPedigreeFunction,age)
        
        if st.button('Prédictions'):
           
            result = predict(data)
        st.success(diabete)
        
    if(selected == "Author") :
        
         st.subheader("Author : LAGRE GABBA BERTRAND")
         st.subheader(" Software Engineer and Data Develper") 
         st.write("Intern at MerSkill \n")
        
if __name__=='__main__':
    main()
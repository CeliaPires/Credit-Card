# churn_prediction_streamlit_app.py

import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('models/logistic_churn_model.pkl')  
st.title("💳 Customer Churn Prediction App")


st.markdown("Enter customer information to predict if they are likely to churn.")

# Input features (match exactly as model training)
Customer_Age = st.number_input("Customer Age", 18, 100, 30)

Income_Category = st.selectbox("Income Category", 
    ['Less than $40K', '$40K - $60K', '$60K - $80K', '$80K - $120K', '$120K +'])

Card_Category = st.selectbox("Card Category", ['Blue', 'Silver', 'Gold', 'Platinum'])

Months_Inactive_12_mon = st.number_input("Months Inactive in Last 12 Months", 0, 12, 1)

Avg_Utilization_Ratio = st.slider("Average Credit Utilization Ratio", 0.0, 1.0, 0.5)

Total_Trans_Amt = st.number_input("Total Transaction Amount", 0, 100000, 1000)

Credit_Limit = st.number_input("Credit Limit", 0, 100000, 10000)


# Encode categorical features manually (must match training)
income_mapping = {
    'Less than $40K': 0,
    '$40K - $60K': 1,
    '$60K - $80K': 2,
    '$80K - $120K': 3,
    '$120K +': 4
}

card_mapping = {
    'Blue': 0,
    'Silver': 1,
    'Gold': 2,
    'Platinum': 3
}
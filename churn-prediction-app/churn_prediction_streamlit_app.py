import streamlit as st
import numpy as np
import joblib

# Load your saved model
model = joblib.load('models/logistic_churn_model.pkl')

st.title("Customer Churn Prediction App")

st.markdown("""
### Persona: Sarah, Customer Retention Specialist
- Age: 35  
- Goal: Identify customers at risk of churning quickly and easily  
- Challenge: Needs a simple and fast tool for predictions  
""")

st.markdown("## Enter Customer Details:")

Customer_Age = st.number_input("Customer Age", min_value=18, max_value=100, value=30)

Income_Category = st.selectbox("Income Category", 
    ['Less Than $40K', '$40K - $60K', '$60K - $80K', '$80K - $120K', '$120K +'])

Card_Category = st.selectbox("Card Category", ['Blue', 'Gold', 'Platinum', 'Silver'])

Months_Inactive_12_mon = st.number_input("Months Inactive in Last 12 Months", min_value=0, max_value=12, value=1)

Avg_Utilization_Ratio = st.slider("Average Credit Utilization Ratio", min_value=0.0, max_value=1.0, value=0.5)

Total_Trans_Amt = st.number_input("Total Transaction Amount", min_value=0, value=1000)

Credit_Limit = st.number_input("Credit Limit", min_value=0, value=10000)

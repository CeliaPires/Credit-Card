import streamlit as st
import numpy as np
import joblib

# Load your saved model
model = joblib.load('/Users/ebenezerrajakumar/Credit-Card/Credit-Card-1/models/logistic_churn_model.pkl')

st.title("Customer Churn Prediction App")

st.markdown("""
### Persona: Sarah, Customer Retention Specialist
- Age: 35  
- Goal: Identify customers at risk of churning quickly and easily  
- Challenge: Needs a simple and fast tool for predictions  
""")

# 📊 Customer Churn Prediction – Streamlit App

This is a simple and interactive Streamlit web application that predicts whether a customer is likely to churn based on selected input features. The prediction is powered by a Logistic Regression model trained on cleaned credit card customer data.

---

## 🎯 Goal

Help businesses proactively identify at-risk customers so they can take action to improve retention.

---

## 🧠 Design Thinking Approach

We followed the five stages of Design Thinking:

- **Empathize**: Identified challenges faced by customer experience teams.
- **Define**: The business problem is high customer churn and the inability to predict it early.
- **Ideate**: Designed a machine learning solution to classify churn risk.
- **Prototype**: Built a user-friendly web app using Streamlit.
- **Test**: Use the app with various customer profiles and refine based on feedback.

---

## 👤 Persona 1

**Name**: Sarah  
**Age**: 38  
**Role**: Customer Retention Manager  
**Pain Point**: Struggles to predict customer churn in time.  
**Goal**: Use a quick tool to identify and act on churn risks.

---

## 📌 Features Used in the Model

| Feature Name             | Description                                   |
| ------------------------ | --------------------------------------------- |
| `Customer_Age`           | Age of the customer                           |
| `Income_Category`        | Income group category                         |
| `Card_Category`          | Credit card type/category                     |
| `Months_Inactive_12_mon` | Months customer was inactive in the past year |
| `Avg_Utilization_Ratio`  | Average credit utilization ratio              |
| `Total_Trans_Amt`        | Total transaction amount                      |
| `Credit_Limit`           | Credit limit on the card                      |

---

## ⚙️ How to Run the App

### 1. Install Required Packages

pip install streamlit pandas scikit-learn joblib

### 2. Run the Streamlit App

streamlit run churn_prediction_streamlit_app.py

✅ Output
You will receive one of the following predictions:

"The customer is likely to churn"

"The customer is not likely to churn"

🚧 Future Development Notice
This Streamlit app is currently in an early stage and serves as a prototype for customer churn prediction using a logistic regression model. While the core data analysis and model training components have been completed, the Streamlit application is still under development.

Some features may not work as intended, including model integration and full input handling. Due to time constraints, these parts have been pushed to the next stage of development.

Further updates will include:

Full integration of the trained model with the app interface

Handling of all necessary input features expected by the model

Improved user experience and error handling

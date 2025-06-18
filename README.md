# <span style="color: #FF6B9D;">ChurnTrailblazers</span>

**<span style="color: #C77DFF;">Where Women meet Data magic</span>**
_<span style="color: #7209B7;">Breaking barriers, predicting churn, shaping future</span>_

This project builds an end-to-end machine learning system to predict customer churn and deliver personalized retention strategies. Using comprehensive data analysis across demographics, financial behavior, and account patterns, the system identifies at-risk customers through four analytical notebooks. An interactive Streamlit application provides real-time churn predictions and matches customers to personas like "Stressed Sarah" for targeted retention solutions including personalized outreach, payment plans, and financial wellness resources. The platform combines predictive analytics with design thinking to proactively reduce churn and maximize customer lifetime value.

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Dataset Information

**Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers/data)

**Total Columns:** 23 (analyzing all columns)

**Target Variable:** Attrition_Flag (whether customer churned or not)

### Column Descriptions

| Column                       | Description                                                  |
| ---------------------------- | ------------------------------------------------------------ |
| **CLIENTNUM**                | Unique customer ID number                                    |
| **Attrition_Flag**           | Whether customer left the service (TARGET VARIABLE)          |
| **Customer_Age**             | Age of the customer in years                                 |
| **Gender**                   | Male or Female                                               |
| **Dependent_count**          | Number of dependents (family members)                        |
| **Education_Level**          | Customer's education level                                   |
| **Marital_Status**           | Single, Married, or Divorced                                 |
| **Income_Category**          | Annual income range category                                 |
| **Card_Category**            | Type of credit card (Blue, Silver, Gold, Platinum)           |
| **Months_on_book**           | How long customer has been with the company                  |
| **Total_Relationship_Count** | Number of products customer has with the company             |
| **Months_Inactive_12_mon**   | Number of months customer was inactive in last 12 months     |
| **Contacts_Count_12_mon**    | Number of times customer contacted company in last 12 months |
| **Credit_Limit**             | Maximum credit limit allowed                                 |
| **Total_Revolving_Bal**      | Outstanding balance on the card                              |
| **Avg_Open_To_Buy**          | Average available credit remaining                           |
| **Total_Amt_Chng_Q4_Q1**     | Change in transaction amount from Q4 to Q1                   |
| **Total_Trans_Amt**          | Total transaction amount in last 12 months                   |
| **Total_Trans_Ct**           | Total transaction count in last 12 months                    |
| **Total_Ct_Chng_Q4_Q1**      | Change in transaction count from Q4 to Q1                    |
| **Avg_Utilization_Ratio**    | How much of credit limit is being used                       |


## Business Requirements

- Develop analytical reports to identify customers at risk of churning and provide actionable insights to reduce churn rates. 

## Hypothesis and how to validate?

- **Hypothesis 1:** Card Category affects churn probability
 Validated by a Chi-Square 

- **Hypothesis 2:** Credit Limit differs significantly between churners and non-churners
Validated by a t-test

- **Hypothesis 3:** Average Utilization Ratio is significantly lower for churners
Validated by a t-test

## Project Plan


## Mapping Business Requirements to Data Visualisation

To meet the business requirements, each visualisation in the dashboard is designed to highlight patterns, trends, and predictors of customer churn, making it easier for business users to identify at-risk customers and target interventions effectively. Here’s how each visualisation supports the requirement:

| Business Requirement     | Visualisation Method    |
|-----------------------------------------------------|------------------------------------------------------|
| Show distribution of total credit limits between churned and existing customers  | Bar Chart                   |
| Examine transaction activity by card category and attrition status                     | Line Chart                     |
| Visualise inactivity levels by card type and churn status        | Line Chart                                |
| Plot credit limit against model-prediction churn probability                 | Scatter Plot                     |
| Display churn rates by the number of products held        | Bar Chart                            |


## Dashboard Design

Our Tableau dashboard provides a comprehensive analysis and visualisation of credit card customer churn. Factors such as card type, credit limit, account utilisation, transaction activity, account inactivity, and customer engagement are analysed to determine the likelihood of customer attrition, enabling deeper understanding of the drivers behind churn. 

This dashboard was designed with the main users in mind (bank managers, analysts, customer service etc.) to clearly articulate the insights from the main issue, which is customer churn. The dashboard includes a range of features such as filters to allow for user customisation and clearly labelled visualisations to ensure inclusivity and ease of use for both technical and non-technical audiences. 

[Tableau Link](https://public.tableau.com/views/CreditCardChurnersDashboard/Dashboard3?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)


## Tableau Dashboard Pages

### Churned Status vs. Credit Limit

![**Bar Chart**](<b5e1428f-4bcd-4552-a9f9-9b46b2ba830f.png>)

**Filters**

 * Available Credit (range slider)

 * Products Count (range slider)


 **Legend**

 * Colour Legend - Attrition Flag


 ### Card Type vs. Avg Transaction Count

![**Line Chart**](<8f69cb85-f2a8-4204-84b1-0f74eef6d62d.png>)

**Filters**
 (-) Available Credit (range slider)
 (-) Products Count (range slider)
 (-) Avg. Total Trans Ct (range slider)

 **Legend**
 (-) Colour Legend - Card Category

 **Labels**
 (-) Attrition Flag


 ### Card Type vs. Avg Months of Inactivity (per 12 months)

![**Line Chart**](<271338c6-9a41-4e23-a80c-c5b35be9a1aa.png>)

**Filters**
 (-) Available Credit (range slider)
 (-) Products Count (range slider)
 (-) Card Category (checkboxes: Blue, Gold, Platinum, Silver)

 **Legend**
 (-) Colour Legend - Card Category

 **Labels**
 (-) Attrition Flag


### Credit Limit vs. Churn Probability

![**Scatter Plot**](<e02810bf-9e26-4c5b-8ba1-1dee72c85837.png>)

**Filters**
 (-) Available Credit (range slider)
 (-) Products Count (range slider)

 **Legend**
 (-) Colour Legend - Attrition Flag
 (-) Size Legend - Total Revolving Balance

 **Tooltip**
 (-) Customer ID, Credit Limit, NB Churn Probability etc.


### Avg Utilisation Ratio vs. Churn Probability

![**Scatter Plot**](<45a5b83d-bc3d-4c0a-866b-2c3c7a1fa5cf.png>)

**Filters**
 (-) Available Credit (range slider)
 (-) Products Count (range slider)

 **Legend**
 (-) Colour Legend - Attrition Flag
 (-) Size Legend - Total Revolving Balance


### Product Count vs. Churn Status

![**Bar Chart**](<f79db157-79e7-43b8-8800-5647f8435226.png>)

**Filters**
 (-) Available Credit (range slider)
 (-) Products Count (range slider)

 **Legend**
 (-) Colour Legend - Attrition Flag

 
 ### Contacts Count Per 12 Months

![**Bar Chart**](<cbc465b8-21cc-42a0-9fb0-de9736a2afda.png>)

**Filters**
 (-) Available Credit (range slider)
 (-) Products Count (range slider)

 **Legend**
 (-) Colour Legend - Card Category


 ## Ethical considerations

**Were there any data privacy, bias or fairness issues with the data?**

- I did not spot any issues with the data or concerns with bias/fairness. 
- In terms of GDPR, the file did not contain any identifiable personal data. 
- Had it been the case, I would have had to adhere GDPR legislation.


## Development Roadmap

# Main Data Analysis Libraries
## Core Data Processing
- pandas
- NumPy
## Data Visualization
- matplotlib
- seaborn
- plotly
- Tableau
## Machine Learning
- scikit-learn
## Interactive Dashboard
- streamlit

## Conclusions 

In conclusion, the analysis reveals that customer churn among credit card holders is strongly associated with several key factors: card category, credit limit, product holding, transaction activity, and engagement levels. Customers with lower credit limits, fewer products, higher inactivity, and lower transaction counts are more likely to churn. Additionally, certain card types—particularly those with less activity—show higher attrition rates. These insights highlight opportunities for targeted interventions, such as offering credit increases, promoting additional products, and engaging less active customers, to effectively reduce churn rates and improve customer retention.

## Credits

- Data Source: The customer dataset used in this project is sourced from Kaggle.
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)
- Youtube videos to aid in creating visualisations in Tableau [Pie Chart Tutorial](https://www.youtube.com/watch?v=mWZL2ae1l30) [Bar Chart Tutorial](https://www.youtube.com/watch?v=wnfbneCCbxA)
- Microsoft CoPilot was used to enhance visualisations and code creation for the calculated fields in Tableau.
- Content from the LMS was used for dashboard creation in Tableau.
- Chatgpt for coding (hypothesis testing) and general troubleshooting.



### Content
- The text for the Home page was taken from Wikipedia Article A

### Media
- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site

## Acknowledgements 

I would like to say a big thank you to Mark and Sheila for stepping in and helping me with my technical issues.

Finally I would like to thank my team (Angel Jayakumar, Kabira Sharpe and Celia Pires) for their work, attitude and contribution to the project.



## ChurnTrailblazers Team! 
Team members section

Angelnesakumari Jayakumar:As a Data Analyst, I led the end-to-end preparation of a machine learning pipeline focused on predicting customer churn. My responsibilities included:

Data Cleaning & Preprocessing: Cleaned and transformed raw customer data to ensure quality and consistency, handling missing values and removing unknowns.

ETL Pipeline Development: Designed and executed an ETL (Extract, Transform, Load) process to structure the dataset for analysis and modeling.

Feature Engineering & Encoding: Selected relevant features for churn prediction and encoded categorical variables to prepare the data for machine learning.

Model Training: Trained a Logistic Regression model using key features such as Customer_Age, Income_Category, Card_Category, Credit_Limit, and transaction data.

Exploratory Data Analysis (EDA): Conducted visual and statistical analysis using Tableau to identify trends, segment behaviors, and understand churn patterns.

Streamlit App Prototype: Initiated a Streamlit app interface for user input and prediction, with further integration planned in the next development phase.

This work demonstrates my ability to apply analytical thinking, data preprocessing, and model development to solve real-world business problems using a structured and user-centered approach.










 












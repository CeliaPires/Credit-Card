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

![**Bar Chart**](<Screenshot 2025-06-18 at 12.08.13 (2).png>)

**Filters**

 * Available Credit (range slider)

 * Products Count (range slider)


 **Legend**

 * Colour Legend - Attrition Flag


 ### Card Type vs. Avg Transaction Count

![**Line Chart**](<Screenshot 2025-06-18 at 12.07.36 (2).png>)

**Filters**
 (-) Available Credit (range slider)
 (-) Products Count (range slider)
 (-) Avg. Total Trans Ct (range slider)

 **Legend**
 (-) Colour Legend - Card Category

 **Labels**
 (-) Attrition Flag


 ### Card Type vs. Avg Months of Inactivity (per 12 months)

![**Line Chart**](<Screenshot 2025-06-18 at 12.07.16 (2).png>)

**Filters**
 (-) Available Credit (range slider)
 (-) Products Count (range slider)
 (-) Card Category (checkboxes: Blue, Gold, Platinum, Silver)

 **Legend**
 (-) Colour Legend - Card Category

 **Labels**
 (-) Attrition Flag


### Credit Limit vs. Churn Probability

![**Scatter Plot**](<Screenshot 2025-06-18 at 12.06.33 (2).png>)

**Filters**
 (-) Available Credit (range slider)
 (-) Products Count (range slider)

 **Legend**
 (-) Colour Legend - Attrition Flag
 (-) Size Legend - Total Revolving Balance

 **Tooltip**
 (-) Customer ID, Credit Limit, NB Churn Probability etc.


### Avg Utilisation Ratio vs. Churn Probability

![**Scatter Plot**](<Screenshot 2025-06-18 at 12.06.03 (2).png>)

**Filters**
 (-) Available Credit (range slider)
 (-) Products Count (range slider)

 **Legend**
 (-) Colour Legend - Attrition Flag
 (-) Size Legend - Total Revolving Balance


### Product Count vs. Churn Status

![**Bar Chart**](<Screenshot 2025-06-18 at 12.01.58 (2).png>)

**Filters**
 (-) Available Credit (range slider)
 (-) Products Count (range slider)

 **Legend**
 (-) Colour Legend - Attrition Flag

 
 ### Contacts Count Per 12 Months

![**Bar Chart**](<Screenshot 2025-06-18 at 12.03.07 (2).png>)

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



### Content
- The text for the Home page was taken from Wikipedia Article A

### Media
- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site

## Acknowledgements 


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



# Customer Churn Analysis Project

## Work Completed

### 1. Data Preparation and ETL Pipeline

- Created a comprehensive **ETL (Extract, Transform, Load) pipeline** in a dedicated Jupyter notebook.
- Cleaned raw data by handling missing values, removing or capping outliers (using winsorization), and standardizing categories.
- Generated multiple cleaned datasets for different purposes:
  - **`cleaned_data.csv`** — Cleaned and capped dataset, with unknown categories retained for visualization and Tableau dashboards.
  - **`cleaned_no_unknown.csv`** — Dataset with all “Unknown” categories removed, used for hypothesis-driven analysis.
  - **`encoded_data.csv`** — Fully encoded dataset where categorical variables are converted to numeric formats suitable for machine learning.

---

### 2. Churn Prediction Model Training

- Developed a **logistic regression model** in a separate notebook.
- Trained the model using carefully selected features, including:
  - `Customer_Age`, `Income_Category`, `Card_Category`, `Months_Inactive_12_mon`, `Avg_Utilization_Ratio`, `Total_Trans_Amt`, `Credit_Limit`.
- Evaluated the model with accuracy, confusion matrix, and classification report to ensure performance.
- Saved the trained model for reuse and deployment.

---

### 3. Churn Prediction Generator

- Created a third notebook with a **customer churn prediction generator** — a script that loads the trained model and generates churn predictions on new input data.
- Implemented user-friendly input forms (planned to integrate with Streamlit app) for end-users to input customer details and receive churn risk predictions.

---

### 4. Project Status: In Progress

\*Streamlit App - Interactive Churn Prediction & Solutions:\*\*

- **Model Testing:** Real-time churn prediction using all relevant features
- **Persona-Based Solutions:** Design thinking approach with customer personas
- **Interactive Dashboard:** Input customer data and get personalized retention strategies

## Streamlit App Features

### Churn Prediction Interface

``````python
# Key input fields for prediction
- Customer_Age (slider)
- Income_Category (selectbox)
- Card_Category (selectbox)
- Months_Inactive_12_mon (slider)
- Avg_Utilization_Ratio (slider)
- Total_Trans_Amt (number_input)
- Credit_Limit (number_input)
Streamlit App Tabs:
├── :dart: Churn Predictor (main prediction interface)
├── :silhouettes: Customer Personas (design thinking profiles)
├── :bulb: Retention Solutions (persona-based strategies)
└── :bar_chart: Model Performance (accuracy metrics)
### Sample output
Prediction: 85% Churn Risk :warning:
Customer Persona: "Stressed Sarah"
Recommended Action:
- Immediate personal call within 24 hours
- Offer payment plan restructuring
- Provide financial wellness resources
- Consider credit limit review

## Data Sets Summary

| Dataset Name             | Purpose                                  | Notes                                              |
| ------------------------ | ---------------------------------------- | -------------------------------------------------- |
| `cleaned_data.csv`       | Visualization and Tableau dashboards     | Unknown categories retained, outliers capped.      |
| `cleaned_no_unknown.csv` | Hypothesis testing and detailed analysis | Removed "Unknown" categories for cleaner insights. |
| `encoded_data.csv`       | Machine learning model training          | All categorical data encoded to numeric values.    |

---

## Next Steps

- Use the cleaned and encoded datasets for further model experimentation or to build additional models.




## Project Plan(Celia)

- Outline the high-level steps taken for the analysis.
- How was the data managed throughout the collection, processing, analysis and interpretation steps?
- Why did you choose the research methodologies you used?

# Analysis Techniques Used (Angel)

## Data Analysis Methods Used

- **Data Cleaning and Preprocessing:**
  Implemented in the ETL pipeline notebook, including handling missing values, treating "Unknown" categories, and outlier capping using winsorization. This ensured that the data was consistent and reliable for both visualization and machine learning purposes.

- **Feature Engineering and Encoding:**
  Converted categorical variables into numeric formats in the encoded dataset to make it suitable for machine learning models like logistic regression.

- **Logistic Regression Modeling:**
  Used logistic regression in the model training notebook to predict customer churn based on selected features. Logistic regression was chosen for its interpretability and efficiency on structured tabular data.

- **Model Evaluation:**
  Assessed the model performance using accuracy, confusion matrix, and classification reports to understand precision, recall, and overall prediction quality.

- **Prediction Generation:**
  Developed a churn prediction generator notebook to apply the trained model to new inputs and generate predictions interactively.

---

## Limitations and Alternative Approaches

- **Limitations:**

  - Logistic regression assumes linearity between features and log-odds of the target, which may oversimplify complex relationships.
  - Handling of unknown categories as a separate label may introduce noise; alternatively, these could be imputed or excluded.
  - Outlier capping via winsorization is effective but might distort natural data variability.

- **Alternative Approaches:**
  - Exploring more complex models such as Random Forests, Gradient Boosting, or Neural Networks for potentially better predictive performance.
  - Using imputation techniques or clustering to handle missing or unknown categorical data.
  - Applying advanced feature engineering techniques like polynomial features or interaction terms.

---

## Structure and Justification of Data Analysis Techniques

- The analysis was structured into three focused notebooks for clarity and modularity:

  1. **ETL Pipeline:** For data cleaning and preparation, ensuring high-quality data as the foundation.
  2. **Model Training:** To focus on machine learning model development and evaluation without distraction from data issues.
  3. **Prediction Generator:** For applying the model to real-world scenarios and enabling interactive use.

- This structure allows incremental development, easier debugging, and better collaboration or sharing with stakeholders.

- Splitting datasets into `cleaned_data`, `cleaned_no_unknown`, and `encoded_data` allowed for tailored use cases such as visualization, hypothesis testing, and modeling, respectively.

---

## Data Constraints and Alternative Strategies

- The presence of many "Unknown" categories limited the initial data quality, particularly for hypothesis testing. To address this, a dedicated dataset with these unknowns removed (`cleaned_no_unknown.csv`) was created for cleaner insights.

- The dataset size and feature set limited model complexity; hence logistic regression was preferred for interpretability and speed.

- When data constraints were encountered, alternative approaches such as data capping and selective removal were used to maintain balance between data quality and quantity.

---

## Use of Generative AI Tools

- Utilized generative AI (like ChatGPT) for:

  - **Ideation:** Brainstorming project structure, data cleaning strategies, and feature selection.
  - **Design Thinking:** Crafting user personas and defining app features to align with end-user needs.
  - **Code Optimization:** Receiving help with writing clean, commented, and efficient code snippets, especially for the logistic regression pipeline and Streamlit app.
  - **Documentation:** Generating clear markdown summaries and explanations to improve project communication.

- Generative AI sped up problem-solving, enhanced learning, and helped maintain focus on project goals.



 



## Known Issues & Solutions(Angel,Celia,Kabira)

### Issue 1: PyArrow Dependency Installation Error

**Problem:** Installation failed when running `pip install -r requirements.txt` with PyArrow dependency errors, even though PyArrow not directly listed in requirements.txt. The error occurred because PyArrow is an internal dependency of pandas and Streamlit packages, causing pip to automatically attempt installation during setup.
**Root Cause:** PyArrow gets pulled in automatically as a transitive dependency from pandas and Streamlit, making it a "hidden dependency" that can cause installation issues on certain machine configurations.
**Solution:**

`````bash
pip install --only-binary=pyarrow pyarrow
Then proceed with the normal requirements installation:
Date Resolved: [16/06/2025]
Key Learning: Hidden/transitive dependencies can affect package installation even when not explicitly listed in requirements.txt. The --only-binary flag forces pip to use pre-compiled binary packages instead of building from source, which resolves compatibility issues on problematic machine configurations.

### Issue 2: Git Repository Conflict from Cloning Template Repository
**Problem:** Cloned a data template repository inside the group project folder, which created two separate Git repositories with conflicting .git folders. This prevented committing changes to the main group project repository, as Git couldn't determine which repository to use for version control.
**Root Cause:** Having multiple .git folders in the same project directory creates Git conflicts, as each .git folder represents a separate repository with its own commit history and remote origin.
**Solution:**
1. Delete the cloned template repository folder completely
2. Copy-paste only the needed template files into the main group repository
3. Use normal Git workflow: `git add` → `git commit` → `git push`
**Date Resolved:** [Add the date when you fixed this]
**Key Learning:**
- **Golden Rule:** Only one .git folder per project
- Clone only the main group repository
- For templates or external files → copy-paste manually, don't clone
- Multiple Git repositories in the same folder cause version control conflicts
# Main Data Analysis Libraries(Angel,Kabira)
## Core Data Processing
- pandas
- NumPy
## Data Visualization
- matplotlib
- seaborn
- plotly
## Machine Learning
- scikit-learn
## Interactive Dashboard
- streamlit

## Conclusions (Celia,Angel,Kabira)

Through the three notebooks—ETL pipeline, churn prediction model training, and churn prediction generator—I successfully prepared and processed the customer data, developed a reliable logistic regression model to predict churn, and created a functional churn prediction tool. The ETL pipeline ensured clean, well-structured data suitable for modeling by handling missing values, encoding categorical features, and capping outliers. The logistic regression model demonstrated solid performance with a good balance of accuracy and interpretability, identifying key factors influencing customer churn. The churn prediction generator notebook integrates the model to provide churn likelihood for new customers. These results set a strong foundation for building interactive dashboards and deployment apps, enabling actionable insights to reduce churn and improve customer retention strategies.



## Credits(Celia,Angel,Kabira)

Data Source: The customer dataset used in this project is sourced from Kaggle.



### Content(Angel,Kabira,Celia)
- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media(Angel, Kabira)
- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site

## Acknowledgements (Angel, Celia, Kabira)
* Thank all  the people who provided support through this project.

## ChurnTrailblazers Team! (Celia,Angel,Kabira)
Team members section

Angelnesakumari Jayakumar:As a Data Analyst, I led the end-to-end preparation of a machine learning pipeline focused on predicting customer churn. My responsibilities included:

Data Cleaning & Preprocessing: Cleaned and transformed raw customer data to ensure quality and consistency, handling missing values and removing unknowns.

ETL Pipeline Development: Designed and executed an ETL (Extract, Transform, Load) process to structure the dataset for analysis and modeling.

Feature Engineering & Encoding: Selected relevant features for churn prediction and encoded categorical variables to prepare the data for machine learning.

Model Training: Trained a Logistic Regression model using key features such as Customer_Age, Income_Category, Card_Category, Credit_Limit, and transaction data.

Exploratory Data Analysis (EDA): Conducted visual and statistical analysis using Tableau to identify trends, segment behaviors, and understand churn patterns.

Streamlit App Prototype: Initiated a Streamlit app interface for user input and prediction, with further integration planned in the next development phase.

This work demonstrates my ability to apply analytical thinking, data preprocessing, and model development to solve real-world business problems using a structured and user-centered approach.



Font AwesomeFont Awesome
Font Awesome
The internet's icon library + toolkit. Used by millions of designers, devs, & content creators. Open-source. Always free. Always awesome.
``````

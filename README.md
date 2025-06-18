# <span style="color: #FF6B9D;">ChurnTrailblazers</span>

**<span style="color: #C77DFF;">Where Women meet Data mAgic</span>**
_<span style="color: #7209B7;">Breaking barriers, predicting churn, shaping future</span>_

This project builds an end-to-end machine learning system to predict customer churn and deliver personalized retention strategies. Using comprehensive data analysis across demographics, financial behavior, and account patterns, the system identifies at-risk customers through four analytical notebooks covering ETL, descriptive statistics, correlations, and segmentation. An interactive Streamlit application provides real-time churn predictions and matches customers to personas like "Stressed Sarah" for targeted retention solutions including personalized outreach, payment plans, and financial wellness resources. The platform combines predictive analytics with design thinking to proactively reduce churn and maximize customer lifetime value.

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)(CELIA)

## Dataset Information

**Source:** Kaggle Credit Card Customer Churn Dataset
**Total Columns:** 23 (analyzing 21 columns)
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

### Analysis Plan

**Notebook 1 - ETL Pipeline:**

- All 21 columns for data cleaning and preprocessing

**Notebook 2 - Descriptive Statistics:**

- Demographics: `Customer_Age`, `Gender`, `Education_Level`, `Marital_Status`, `Income_Category`
- Account Info: `Card_Category`, `Months_on_book`, `Credit_Limit`

**Notebook 3 - Correlation Analysis:**

- Financial: `Credit_Limit`, `Total_Revolving_Bal`, `Avg_Utilization_Ratio`, `Total_Trans_Amt`
- Behavioral: `Months_Inactive_12_mon`, `Contacts_Count_12_mon`, `Total_Trans_Ct`

**Notebook 4 - Segmentation Analysis:**

- Key Segments: `Income_Category`, `Card_Category`, `Customer_Age`, `Total_Relationship_Count`
- Risk Factors: `Avg_Utilization_Ratio`, `Months_Inactive_12_mon`, `Total_Revolving_Bal`

**Streamlit App - Interactive Churn Prediction & Solutions:**

- **Model Testing:** Real-time churn prediction using all relevant features
- **Persona-Based Solutions:** Design thinking approach with customer personas
- **Interactive Dashboard:** Input customer data and get personalized retention strategies

## Streamlit App Features

### Churn Prediction Interface

`````python

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

## Business Requirements()(Celia)
- Describe your business requirements

## Hypothesis and how to validate?()(Celia)
- List here your project hypothesis(es) and how you envision validating it (them)

## Project Plan(Celia)
- Outline the high-level steps taken for the analysis.
- How was the data managed throughout the collection, processing, analysis and interpretation steps?
- Why did you choose the research methodologies you used?

## The rationale to map the business requirements to the Data Visualisations(Kabira)
- List your business requirements and a rationale to map them to the Data Visualisations

## Analysis techniques used(Angel)
- List the data analysis methods used and explain limitations or alternative approaches.
- How did you structure the data analysis techniques. Justify your response.
- Did the data limit you, and did you use an alternative approach to meet these challenges?
- How did you use generative AI tools to help with ideation, design thinking and code optimisation?

## Ethical considerations(Celia)
- Were there any data privacy, bias or fairness issues with the data?
- How did you overcome any legal or societal issues?

## Dashboard Design

Our Tableau dashboard provides a comprehensive analysis and visualisation of credit card customer churn. Factors such as card type, credit limit, account utilisation, transaction activity, account inactivity, and customer engagement are analysed to determine the likelihood of customer attrition, enabling deeper understanding of the drivers behind churn. 

This dashboard was designed with the main users in mind (bank managers, analysts, customer service etc.) to clearly articulate in the insghts from the main issue, which is customer churn. The dashboard includes a range of features such as filters to allow for user customisation and clearly labelled visualisations to ensure inclusivity and ease of use for both technical and non-technical audiences. 

## Tableau Dashboard Pages

### Churned Status vs. Credit Limit

**Visualisation**: Bar Chart

**Filters**
 (-) Available Credit (range slider)
 (-) Products Count (range slider)

 **Legend**
 (-) Colour Legend - Attrition Flag


 ### Card Type vs. Avg Transaction Count

**Visualisation**: Line Chart

**Filters**
 (-) Available Credit (range slider)
 (-) Products Count (range slider)
 (-) Avg. Total Trans Ct (range slider)

 **Legend**
 (-) Colour Legend - Card Category

 **Labels**
 (-) Attrition Flag


 ### Card Type vs. Avg Months of Inactivity (per 12 months)

**Visualisation**: Line Chart

**Filters**
 (-) Available Credit (range slider)
 (-) Products Count (range slider)
 (-) Card Category (checkboxes: Blue, Gold, Platinum, Silver)

 **Legend**
 (-) Colour Legend - Card Category

 **Labels**
 (-) Attrition Flag


### Credit Limit vs. Churn Probability

**Visualisation**: Scatter Plot

**Filters**
 (-) Available Credit (range slider)
 (-) Products Count (range slider)

 **Legend**
 (-) Colour Legend - Attrition Flag
 (-) Size Legend - Total Revolving Balance

 **Tooltip**
 (-) Customer ID, Credit Limit, NB Churn Probability etc.


### Avg Utilisation Ratio vs. Churn Probability

**Visualisation**: Scatter Plot

**Filters**
 (-) Available Credit (range slider)
 (-) Products Count (range slider)

 **Legend**
 (-) Colour Legend - Attrition Flag
 (-) Size Legend - Total Revolving Balance


### Product Count vs. Churn Status

**Visualisation**: Bar Chart 

**Filters**
 (-) Available Credit (range slider)
 (-) Products Count (range slider)

 **Legend**
 (-) Colour Legend - Attrition Flag

 
 ### Contacts Count Per 12 Months

**Visualisation**: Stacked Bar Chart 

**Filters**
 (-) Available Credit (range slider)
 (-) Products Count (range slider)

 **Legend**
 (-) Colour Legend - Card Category
 


## Development Roadmap(Celia)
- What challenges did you face, and what strategies were used to overcome these challenges?
- What new skills or tools do you plan to learn next based on your project experience?

## Known Issues & Solutions(Angel,Celia,Kabira)

### Issue 1: PyArrow Dependency Installation Error
**Problem:** Installation failed when running `pip install -r requirements.txt` with PyArrow dependency errors, even though PyArrow not directly listed in requirements.txt. The error occurred because PyArrow is an internal dependency of pandas and Streamlit packages, causing pip to automatically attempt installation during setup.
**Root Cause:** PyArrow gets pulled in automatically as a transitive dependency from pandas and Streamlit, making it a "hidden dependency" that can cause installation issues on certain machine configurations.
**Solution:**
```bash
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
Key findings

## Credits(Celia,Angel,Kabira)

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content(Angel,Kabira,Celia)
- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media(Angel, Kabira)
- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site

## Acknowledgements (Angel, Celia, Kabira)
* Thank the people who provided support through this project.

## ChurnTrailblazers Team! (Celia,Angel,Kabira)
Team members section (roles)
```` (edited)

Font AwesomeFont Awesome
Font Awesome
The internet's icon library + toolkit. Used by millions of designers, devs, & content creators. Open-source. Always free. Always awesome.
`````

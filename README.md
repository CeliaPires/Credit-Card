# <span style="color: #FF6B9D;">ChurnTrailblazers</span>

**<span style="color: #C77DFF;">Where Women meet Data mAgic</span>**
_<span style="color: #7209B7;">Breaking barriers, predicting churn, shaping future</span>_

This project aims to develop an end-to-end machine learning solution to predict customer churn in the financial services sector. By leveraging historical customer data—including demographics, transaction behavior, and credit usage—the system identifies customers who are at risk of leaving. The project begins with a robust ETL pipeline that cleans, preprocesses, and encodes the data to prepare it for modeling. A logistic regression model is then trained to predict churn with high accuracy. Complementing the predictive model, Tableau dashboards provide interactive visualizations for exploratory data analysis and business insights. The ultimate goal is to create a customer-centric platform that integrates predictive analytics with design thinking principles to enable personalized retention strategies and improve customer lifetime value. Future development includes advanced segmentation, enhanced model deployment, and a user-friendly Streamlit app for real-time churn prediction and intervention.

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)(CELIA)

## Dataset Information

**Source:** Kaggle Credit Card Customer Churn Dataset
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

### Analysis Plan

- All 23 columns for data cleaning and preprocessing

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

## Data Sets Summary

| Dataset Name             | Purpose                                  | Notes                                              |
| ------------------------ | ---------------------------------------- | -------------------------------------------------- |
| `cleaned_data.csv`       | Visualization and Tableau dashboards     | Unknown categories retained, outliers capped.      |
| `cleaned_no_unknown.csv` | Hypothesis testing and detailed analysis | Removed "Unknown" categories for cleaner insights. |
| `encoded_data.csv`       | Machine learning model training          | All categorical data encoded to numeric values.    |

---

## Next Steps

- Build and deploy a **Streamlit app** integrating the trained logistic regression model for real-time churn prediction.
- Include **design thinking** and user personas in the app for better user experience and alignment with business needs.
- Use the cleaned and encoded datasets for further model experimentation or to build additional models.

---

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

---

## Ethical considerations(Celia)

- Were there any data privacy, bias or fairness issues with the data?
- How did you overcome any legal or societal issues?

## Dashboard Design(Kabira's SEction)

- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
- Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).
- How were data insights communicated to technical and non-technical audiences?
- Explain how the dashboard was designed to communicate complex data insights to different audiences.

## Development Roadmap(Celia)

- What challenges did you face, and what strategies were used to overcome these challenges?
- What new skills or tools do you plan to learn next based on your project experience?

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

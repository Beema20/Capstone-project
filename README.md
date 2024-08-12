# **LinkedIn Job Postings Analysis (2023-2024)**
## **Big Data Capstone Project**

### **Project Overview**
This project focuses on analyzing the LinkedIn Job Postings dataset from 2023-2024 to extract insights into job market trends, salary predictions, and job market segmentation. The analysis aims to provide valuable information for job seekers, employers, and policymakers by identifying key patterns in job postings, salaries, and industry demands.

### **Project Objectives**
- **Trend Analysis**: Identify the most active companies and industries, and understand the demand for specific job skills.
- **Salary Prediction**: Develop predictive models to estimate salaries based on job descriptions, company attributes, and industry data.
- **Job Market Segmentation**: Analyze job postings to segment the market by various attributes such as industry, job type, and company size.

### **Datasets Used**
- **Job Postings**: Contains details such as job titles, descriptions, locations, salaries, and job types.
- **Companies**: Includes information on company size, industry, location, and employee counts.
- **Benefits**: Lists the benefits associated with job postings.
- **Employee Counts**: Provides the number of employees and followers for each company.

### **Data Collection & Preprocessing**
- **Data Cleaning**: Removed duplicates, handled missing values, and filtered irrelevant columns.
- **Data Integration**: Merged multiple datasets to create a unified dataset linking job postings with company and benefit details.
- **Feature Engineering**: Created new features such as 'location' and extracted relevant information from job descriptions.
- **Preprocessing**: Applied text preprocessing (tokenization, stopword removal, lemmatization), categorical encoding, and numerical scaling.

### **Exploratory Data Analysis (EDA)**
- **Company Activity**: Analyzed the most active companies in terms of job postings, with Macy’s leading.
- **Industry Distribution**: Identified Technology and Healthcare as the top sectors for job postings.
- **Skill Demand**: Highlighted the most in-demand job skills such as data analysis and project management.
- **Visualizations**: Used bar charts, scatter plots, and correlation matrices to explore data patterns.

### **Model Development**
- **Feature Selection**: Key features like job title, industry, and company size were selected for modeling.
- **Modeling Techniques**: Used regression models for salary prediction and classification models for predicting job types(XgBoost, Linear Regression, etc.).
- **Hyperparameter Tuning**: Applied Grid Search to optimize model parameters for better accuracy.
- **Model Evaluation**: Models were evaluated using accuracy, precision, and recall metrics.

### **Key Findings**
- **Salary Prediction**: Successfully predicted salaries across industries, with key features across various sectors.
- **Company Insights**: Large companies like Macy’s are leading in job postings, indicating high demand for new hires.
- **Industry Trends**: Technology and Healthcare sectors show significant growth in job postings, with certain industries offering higher salaries.
- **Skill Demand**: Strong demand for specific skills in data analysis and project management.
- **Salary Analysis**: Identified a wide range of salaries across industries, with notable outliers in certain sectors.
- **Job Market Segmentation**: Certain industries and company sizes show distinct hiring patterns and salary distributions, indicating segmented job markets.

### **Challenges Faced**
- **Data Integration**: Merging datasets from different sources required careful handling to maintain data consistency.
- **Missing Data**: Addressed challenges in handling missing salary and location information through imputation and exclusion strategies.
- **Outlier Management**: Managed outliers in salary data to ensure accurate analysis and model predictions.

### **Future Work**
- Expand the analysis to include a broader time frame for more comprehensive insights.
- Improve model features and explore additional industry-specific trends.
- Investigate deeper segmentation of the job market based on more detailed job attributes.
- Build another web app for Job recommendations based on skills and experience.

### **Technologies Used**
- **Python**: Primary programming language for data processing and analysis.
- **Pandas, NumPy**: Libraries for data manipulation and analysis.
- **Scikit-learn**: Used for machine learning models and preprocessing.
- **Matplotlib, Seaborn**: Libraries for data visualization.
- **NLTK/Spacy**: Libraries for natural language processing.
- **Jupyter Notebook**: Environment for developing and sharing code.

### **Contributors**
- **Harsh Kundal**: Data acquisition, preliminary analysis, report.
- **Parminder Kaur**: Data exploration, visualization, presentation.
- **Diksha**: Data visualization, presentation.
- **Jaisy Joy**: Data exploration and preprocessing, model building, user-interface development, reports
- **Beema Sajeev**: Data exploration and preprocessing, EDA, Model building, reports, presentation.

### **Conclusion**
The LinkedIn Job Postings Analysis project provided valuable insights into job market dynamics, salary distributions, and job market segmentation. The predictive models developed during this project can serve as tools for job seekers, employers, and policymakers to make data-driven decisions. The project demonstrated the importance of thorough data preprocessing, effective feature engineering, and the use of advanced machine learning techniques to extract actionable insights from complex datasets.

### **Repository Structure**
- **/data**: Contains the raw and processed datasets..
- **/notebooks**: Jupyter notebooks used for data exploration, preprocessing, and modeling.
- **/models**: Saved models and scripts used for model training and evaluation.
- **/app**: A user interface incorparated with streamlit to predict Salary.
- **/visualizations**: Graphs, charts, and visual outputs from the EDA and model results.
- **/reports**: Final project report, milestone reports, and presentation slides.


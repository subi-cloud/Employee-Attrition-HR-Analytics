# 📊 Employee Attrition & HR Analytics

An end-to-end **Data Analyst portfolio project** that analyzes employee attrition patterns using **Python, SQL, MySQL, data visualization, and Streamlit**.

The project explores how factors such as overtime, job satisfaction, salary, age, experience, job role, business travel, job level, and promotion history are associated with employee attrition.

---

## 📌 Project Overview

Employee attrition is an important HR analytics problem that can affect workforce stability and organizational planning.

This project analyzes an employee dataset to identify patterns in employee attrition and understand how different HR-related factors are associated with employees leaving the organization.

The project follows a complete data analytics workflow:

**Data Collection → Data Cleaning → Exploratory Data Analysis → SQL Analysis → Data Visualization → Dashboard Development → Business Insights**

---

## 🎯 Project Objective

The main objectives of this project are:

- Analyze overall employee attrition.
- Calculate the employee attrition rate.
- Identify HR factors associated with employee attrition.
- Analyze attrition across departments and job roles.
- Examine the relationship between overtime and attrition.
- Analyze job satisfaction and work-life balance.
- Study salary and compensation patterns.
- Analyze age and years of experience.
- Examine business travel and job levels.
- Analyze promotion history.
- Build an interactive HR analytics dashboard.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data analysis and processing |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| SQL | Data analysis and querying |
| MySQL | Database management |
| Streamlit | Interactive dashboard |
| VS Code | Development environment |
| GitHub | Project version control |

---

## 📂 Project Structure

```text
Employee-Attrition-HR-Analytics/
│
├── charts/
│   ├── age_group_attrition.png
│   ├── business_travel_attrition.png
│   ├── department_attrition.png
│   ├── experience_attrition.png
│   ├── job_satisfaction_attrition.png
│   ├── joblevel_attrition.png
│   ├── jobrole_attrition.png
│   ├── overall_attrition.png
│   ├── overtime_attrition.png
│   ├── promotion_attrition.png
│   ├── salary_attrition.png
│   └── worklife_balance_attrition.png
│
├── dashboard/
│   └── dashboard.py
│
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── python/
│   ├── analysis.py
│   ├── data_cleaning.py
│   └── visualization.py
│
├── sql/
│   └── analysis.sql
│
└── README.md

Project Workflow

Dataset
   ↓
Data Loading
   ↓
Data Cleaning & Validation
   ↓
Exploratory Data Analysis
   ↓
SQL Analysis using MySQL
   ↓
Data Visualization
   ↓
Interactive Streamlit Dashboard
   ↓
Business Insights

📊 Dataset

The project uses the IBM HR Analytics Employee Attrition & Performance practice dataset.

The dataset contains:
1,470 employee records
35 columns
Employee demographics
Job information
Compensation information
Satisfaction metrics
Work-related information
Attrition status

🧹 Data Cleaning & Validation
The dataset was loaded and checked using Python and Pandas.

The following checks were performed:
Dataset dimensions
Column names
Missing values
Data types
Categorical variables
Numerical variables
Attrition values

🐍 Python Analysis

Python was used for exploratory analysis and data processing.

Main analysis areas
Overall employee attrition
Department distribution
Job role distribution
Average monthly income
Overtime and attrition
Job satisfaction
Work-life balance
Age groups
Years at company
Business travel
Job level
Promotion history

Python Files

data_cleaning.py
Loads the dataset and performs initial data validation.

analysis.py
Performs exploratory analysis and calculates important HR metrics.

visualization.py
Creates visualizations for different HR factors and attrition patterns.

🗄️ SQL Analysis

The dataset was imported into MySQL for structured analysis.

Database
CREATE DATABASE hr_analytics;
Main SQL Analysis

The project includes SQL queries for:
Overall attrition rate
Department-wise attrition
Overtime vs attrition
Salary vs attrition
Job satisfaction vs attrition
Work-life balance vs attrition
Age group vs attrition
Years at company vs attrition
Promotion history vs attrition
Job role vs attrition
Business travel vs attrition
Job level vs attrition

SQL queries are available in:
sql/analysis.sql

📈 Data Visualization

The project contains 12 visualizations:

Overall Employee Attrition
Department-wise Attrition
Overtime vs Attrition
Age Group vs Attrition
Job Satisfaction vs Attrition
Work-Life Balance vs Attrition
Average Monthly Income vs Attrition
Job Role vs Attrition
Years at Company vs Attrition
Business Travel vs Attrition
Job Level vs Attrition
Promotion History vs Attrition

The generated charts are stored in:
charts/

🖥️ Interactive Streamlit Dashboard

The project includes an interactive Streamlit HR Analytics Dashboard.

Dashboard KPIs

The dashboard displays:

Total Employees
Employees Left
Attrition Rate
Average Monthly Income
Dashboard Filters

Users can filter the analysis by:

Department
Job Role
Overtime
Attrition
Dashboard Analysis

The dashboard provides interactive analysis of:

Department
Overtime
Job Satisfaction
Age Group
Years at Company
Job Role
Monthly Income
Business Travel
Job Level
Promotion History

It also provides an employee data preview and dynamically updates the displayed metrics based on selected filters.

🔍 Key Findings

Based on the analysis of the dataset:

Overall Attrition
Total employees: 1,470
Employees recorded as having left: 237
Overall attrition rate: 16.12%
Overtime

Employees with overtime had a recorded attrition rate of approximately 30.53%, compared with 10.44% among employees without overtime.

Salary
Average monthly income:

Employees who left: 4,787
Employees who stayed: 6,833
Age
The recorded attrition rate was highest among employees under 25, at approximately 39.18%.

Experience
Employees with 0–2 years at the company had a recorded attrition rate of approximately 29.82%.
Business Travel
The recorded attrition rates were:
Travel Frequently: 24.91%
Travel Rarely: 14.96%
Non-Travel: 8.00%
Job Role

Some job roles showed substantially different recorded attrition rates. For example:

Sales Representative: 39.76%
Laboratory Technician: 23.94%
Human Resources: 23.08%
Manager: 4.90%
Research Director: 2.50%

These results describe associations within this practice dataset and do not establish that any individual factor causes attrition.

💡 Business Insights

The analysis highlights several areas that HR teams could investigate further:

Overtime patterns may be useful for workforce planning.
Early-tenure employees show different attrition patterns from longer-tenured employees.
Compensation levels differ between employees who stayed and those recorded as having left.
Attrition patterns vary across job roles.
Business travel frequency is associated with different attrition rates.
Job satisfaction and work-life balance provide additional dimensions for understanding employee turnover patterns.

These observations are descriptive and should be combined with additional organizational data before making HR decisions.


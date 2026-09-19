# 📊 Employee Attrition & HR Analytics

An end-to-end Data Analyst portfolio project that analyzes employee attrition patterns using Python, SQL, MySQL, data visualization, and an interactive Streamlit dashboard.

---

## 📌 Project Overview

Employee Attrition & HR Analytics is an end-to-end data analytics project developed to explore employee attrition patterns and understand how different HR-related factors are associated with employee turnover.

The project follows a complete data analytics workflow, starting from dataset exploration and data cleaning, followed by exploratory analysis, SQL analysis, data visualization, and interactive dashboard development.

The project uses:

- **Python** for data cleaning, analysis, and visualization
- **Pandas and NumPy** for data manipulation
- **Matplotlib and Seaborn** for visualization
- **MySQL and SQL** for database analysis
- **Streamlit** for the interactive dashboard

---

## 🎯 Project Objective

The main objective of this project is to analyze employee attrition and explore patterns associated with different HR factors.

The analysis focuses on:

- Employee attrition
- Department
- Job role
- Overtime
- Job satisfaction
- Work-life balance
- Monthly income
- Age
- Years at company
- Business travel
- Job level
- Promotion history

The project demonstrates how data analytics can be used to explore HR data, identify patterns, and communicate findings through an interactive dashboard.

---

## 🔄 Project Workflow

```text
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
Python Data Visualization
   ↓
Interactive Streamlit Dashboard
   ↓
HR Analytics Insights
   ↓
Portfolio Presentation


Employee-Attrition-HR-Analytics/
│
├── charts/
│   ├── overall_attrition.png
│   ├── department_attrition.png
│   ├── overtime_attrition.png
│   ├── age_group_attrition.png
│   ├── job_satisfaction_attrition.png
│   ├── worklife_balance_attrition.png
│   ├── salary_attrition.png
│   ├── jobrole_attrition.png
│   ├── experience_attrition.png
│   ├── business_travel_attrition.png
│   ├── joblevel_attrition.png
│   └── promotion_attrition.png
│
├── dashboard/
│   └── dashboard.py
│
├── python/
│   ├── data_cleaning.py
│   ├── analysis.py
│   └── visualization.py
│
├── sql/
│   └── analysis.sql
│
└── README.md

Technologies Used

Programming & Data Analysis
Python
Pandas
NumPy

Data Visualization
Matplotlib
Seaborn

Database
MySQL
SQL

Dashboard
Streamlit

Development Tools
Visual Studio Code
MySQL Workbench

Dataset
The project uses the IBM HR Analytics Employee Attrition & Performance practice dataset.
The dataset contains employee-related attributes such as:

Age
Attrition
Business Travel
Department
Distance From Home
Education
Education Field
Environment Satisfaction
Job Involvement
Job Level
Job Role
Job Satisfaction
Monthly Income
Overtime
Performance Rating
Relationship Satisfaction
Total Working Years
Work-Life Balance
Years at Company
Years in Current Role
Years Since Last Promotion
Years With Current Manager

Dataset Information
Total Records: 1,470
Total Columns: 35
Missing Values: 0

Data Cleaning

Python and Pandas were used to perform the initial data inspection and validation.

The data cleaning process included:
Loading the CSV dataset
Inspecting the first few records
Checking dataset dimensions
Checking column names
Checking missing values
Validating the dataset structure
Preparing the dataset for further analysis

The dataset contains 1,470 records and 35 columns, with no missing values.

Python Data Analysis

Python was used to perform exploratory analysis on the HR dataset.

The analysis included:
Total employee count
Overall attrition count
Department distribution
Job role distribution
Average monthly income by attrition
Overtime vs attrition
Job satisfaction vs attrition
Work-life balance vs attrition

SQL Analysis Performed

Overall attrition
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


Data Visualization

Python was used to create 12 visualizations to explore different employee attrition patterns.

Visualizations Created
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

Interactive Streamlit Dashboard

An interactive dashboard was developed using Streamlit to allow users to explore the HR dataset through filters, KPIs, charts, and insights.

Dashboard KPIs
Total Employees
Employees Left
Attrition Rate
Average Monthly Income
Dashboard Filters
Department
Job Role
Overtime
Attrition
Dashboard Analysis Sections
Department Analysis
Work Conditions & Satisfaction
Employee Demographics & Experience
Job Role & Compensation
Business Travel & Career Patterns
Promotion History
HR Analytics Insights
Employee Data Preview

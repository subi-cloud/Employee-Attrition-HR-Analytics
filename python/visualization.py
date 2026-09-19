import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
file_path = "data/WA_Fn-UseC_-HR-Employee-Attrition.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Total employees:", len(df))

# Create charts folder
os.makedirs("charts", exist_ok=True)


# =====================================================
# 1. OVERALL ATTRITION
# =====================================================

attrition_counts = df["Attrition"].value_counts()

plt.figure(figsize=(6, 5))

sns.barplot(
    x=attrition_counts.index,
    y=attrition_counts.values
)

plt.title("Overall Employee Attrition")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig("charts/overall_attrition.png")
plt.close()

print("Overall attrition chart created.")


# =====================================================
# 2. DEPARTMENT-WISE ATTRITION
# =====================================================

department_attrition = pd.crosstab(
    df["Department"],
    df["Attrition"]
)

department_attrition.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Department-wise Attrition")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/department_attrition.png")
plt.close()

print("Department attrition chart created.")


# =====================================================
# 3. OVERTIME VS ATTRITION
# =====================================================

overtime_attrition = pd.crosstab(
    df["OverTime"],
    df["Attrition"]
)

overtime_attrition.plot(
    kind="bar",
    figsize=(7, 5)
)

plt.title("Overtime vs Attrition")
plt.xlabel("Overtime")
plt.ylabel("Number of Employees")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/overtime_attrition.png")
plt.close()

print("Overtime chart created.")


print("\nAll initial charts created successfully!")
# =====================================================
# 4. AGE GROUP VS ATTRITION
# =====================================================

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 24, 34, 44, 54, 100],
    labels=["Under 25", "25-34", "35-44", "45-54", "55+"]
)

age_attrition = pd.crosstab(
    df["Age_Group"],
    df["Attrition"]
)

age_attrition.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Age Group vs Attrition")
plt.xlabel("Age Group")
plt.ylabel("Number of Employees")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/age_group_attrition.png")
plt.close()

print("Age group chart created.")


# =====================================================
# 5. JOB SATISFACTION VS ATTRITION
# =====================================================

satisfaction_attrition = pd.crosstab(
    df["JobSatisfaction"],
    df["Attrition"]
)

satisfaction_attrition.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Job Satisfaction vs Attrition")
plt.xlabel("Job Satisfaction Level")
plt.ylabel("Number of Employees")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/job_satisfaction_attrition.png")
plt.close()

print("Job satisfaction chart created.")


# =====================================================
# 6. WORK-LIFE BALANCE VS ATTRITION
# =====================================================

worklife_attrition = pd.crosstab(
    df["WorkLifeBalance"],
    df["Attrition"]
)

worklife_attrition.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Work-Life Balance vs Attrition")
plt.xlabel("Work-Life Balance Level")
plt.ylabel("Number of Employees")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/worklife_balance_attrition.png")
plt.close()

print("Work-life balance chart created.")


print("\nAll charts created successfully!")
# =====================================================
# 7. SALARY VS ATTRITION
# =====================================================

salary_attrition = df.groupby("Attrition")["MonthlyIncome"].mean()

plt.figure(figsize=(7, 5))

sns.barplot(
    x=salary_attrition.index,
    y=salary_attrition.values
)

plt.title("Average Monthly Income vs Attrition")
plt.xlabel("Attrition")
plt.ylabel("Average Monthly Income")

plt.tight_layout()

plt.savefig("charts/salary_attrition.png")
plt.close()

print("Salary vs attrition chart created.")
# =====================================================
# 8. JOB ROLE VS ATTRITION
# =====================================================

jobrole_attrition = pd.crosstab(
    df["JobRole"],
    df["Attrition"]
)

jobrole_attrition.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Job Role vs Attrition")
plt.xlabel("Job Role")
plt.ylabel("Number of Employees")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("charts/jobrole_attrition.png")
plt.close()

print("Job role chart created.")
# =====================================================
# 9. EXPERIENCE VS ATTRITION
# =====================================================

df["Experience_Group"] = pd.cut(
    df["YearsAtCompany"],
    bins=[-1, 2, 5, 10, 100],
    labels=["0-2 Years", "3-5 Years", "6-10 Years", "10+ Years"]
)

experience_attrition = pd.crosstab(
    df["Experience_Group"],
    df["Attrition"]
)

experience_attrition.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Years at Company vs Attrition")
plt.xlabel("Experience at Company")
plt.ylabel("Number of Employees")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/experience_attrition.png")
plt.close()

print("Experience vs attrition chart created.")
# =====================================================
# 10. BUSINESS TRAVEL VS ATTRITION
# =====================================================

travel_attrition = pd.crosstab(
    df["BusinessTravel"],
    df["Attrition"]
)

travel_attrition.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Business Travel vs Attrition")
plt.xlabel("Business Travel")
plt.ylabel("Number of Employees")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/business_travel_attrition.png")
plt.close()

print("Business travel chart created.")
# =====================================================
# 11. JOB LEVEL VS ATTRITION
# =====================================================

joblevel_attrition = pd.crosstab(
    df["JobLevel"],
    df["Attrition"]
)

joblevel_attrition.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Job Level vs Attrition")
plt.xlabel("Job Level")
plt.ylabel("Number of Employees")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/joblevel_attrition.png")
plt.close()

print("Job level chart created.")
# =====================================================
# 12. PROMOTION HISTORY VS ATTRITION
# =====================================================

df["Promotion_Group"] = pd.cut(
    df["YearsSinceLastPromotion"],
    bins=[-1, 0, 2, 5, 100],
    labels=[
        "No Promotion Yet",
        "1-2 Years",
        "3-5 Years",
        "6+ Years"
    ]
)

promotion_attrition = pd.crosstab(
    df["Promotion_Group"],
    df["Attrition"]
)

promotion_attrition.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Promotion History vs Attrition")
plt.xlabel("Years Since Last Promotion")
plt.ylabel("Number of Employees")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/promotion_attrition.png")
plt.close()

print("Promotion history chart created.")

print("\nAll 12 HR analysis charts created successfully!")








import streamlit as st
import pandas as pd


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Employee Attrition & HR Analytics",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 17px;
    color: #666666;
    margin-bottom: 25px;
}

.section-title {
    font-size: 25px;
    font-weight: 650;
    margin-top: 25px;
    margin-bottom: 15px;
}

.metric-card {
    background-color: #f7f8fa;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
    text-align: center;
}

.insight-box {
    background-color: #f7f8fa;
    padding: 18px;
    border-radius: 10px;
    border-left: 5px solid #4f46e5;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

file_path = "data/WA_Fn-UseC_-HR-Employee-Attrition.csv"

df = pd.read_csv(file_path)


# ============================================================
# TITLE
# ============================================================

st.markdown(
    '<div class="main-title">📊 Employee Attrition & HR Analytics Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Interactive analysis of employee attrition patterns and HR factors.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.title("🔎 Dashboard Filters")

st.sidebar.caption(
    "Use the filters to explore different employee groups."
)


# Department
department_options = ["All"] + sorted(
    df["Department"].unique().tolist()
)

selected_department = st.sidebar.selectbox(
    "Department",
    department_options
)


# Job Role
jobrole_options = ["All"] + sorted(
    df["JobRole"].unique().tolist()
)

selected_jobrole = st.sidebar.selectbox(
    "Job Role",
    jobrole_options
)


# Overtime
overtime_options = ["All"] + sorted(
    df["OverTime"].unique().tolist()
)

selected_overtime = st.sidebar.selectbox(
    "Overtime",
    overtime_options
)


# Attrition
attrition_options = ["All"] + sorted(
    df["Attrition"].unique().tolist()
)

selected_attrition = st.sidebar.selectbox(
    "Attrition",
    attrition_options
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


if selected_department != "All":
    filtered_df = filtered_df[
        filtered_df["Department"] == selected_department
    ]


if selected_jobrole != "All":
    filtered_df = filtered_df[
        filtered_df["JobRole"] == selected_jobrole
    ]


if selected_overtime != "All":
    filtered_df = filtered_df[
        filtered_df["OverTime"] == selected_overtime
    ]


if selected_attrition != "All":
    filtered_df = filtered_df[
        filtered_df["Attrition"] == selected_attrition
    ]


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_employees = len(filtered_df)

employees_left = len(
    filtered_df[filtered_df["Attrition"] == "Yes"]
)

if total_employees > 0:
    attrition_rate = (
        employees_left / total_employees
    ) * 100
else:
    attrition_rate = 0


if total_employees > 0:
    average_income = filtered_df["MonthlyIncome"].mean()
else:
    average_income = 0


average_age = (
    filtered_df["Age"].mean()
    if total_employees > 0
    else 0
)


# ============================================================
# KPI SECTION
# ============================================================

st.markdown(
    '<div class="section-title">📌 Key HR Metrics</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Total Employees",
        f"{total_employees:,}"
    )


with col2:
    st.metric(
        "Employees Left",
        f"{employees_left:,}"
    )


with col3:
    st.metric(
        "Attrition Rate",
        f"{attrition_rate:.2f}%"
    )


with col4:
    st.metric(
        "Average Monthly Income",
        f"{average_income:,.0f}"
    )


# ============================================================
# FILTER STATUS
# ============================================================

if (
    selected_department != "All"
    or selected_jobrole != "All"
    or selected_overtime != "All"
    or selected_attrition != "All"
):

    st.info(
        f"Showing {total_employees:,} employees based on the selected filters."
    )


# ============================================================
# DEPARTMENT ANALYSIS
# ============================================================

st.markdown(
    '<div class="section-title">🏢 Department Analysis</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:

    st.write("**Employees by Department**")

    department_count = (
        filtered_df["Department"]
        .value_counts()
        .sort_index()
    )

    st.bar_chart(
        department_count
    )


with col2:

    st.write("**Department Attrition Rate**")

    department_rate = (
        filtered_df.groupby("Department")["Attrition"]
        .apply(
            lambda x:
            (x == "Yes").mean() * 100
        )
        .round(2)
    )

    st.bar_chart(
        department_rate
    )


# ============================================================
# OVERTIME & JOB SATISFACTION
# ============================================================

st.markdown(
    '<div class="section-title">⏰ Work Conditions & Satisfaction</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:

    st.write("**Overtime vs Attrition**")

    overtime_data = pd.crosstab(
        filtered_df["OverTime"],
        filtered_df["Attrition"]
    )

    st.bar_chart(
        overtime_data
    )


with col2:

    st.write("**Job Satisfaction vs Attrition**")

    satisfaction_data = pd.crosstab(
        filtered_df["JobSatisfaction"],
        filtered_df["Attrition"]
    )

    st.bar_chart(
        satisfaction_data
    )


# ============================================================
# AGE & EXPERIENCE
# ============================================================

st.markdown(
    '<div class="section-title">👥 Employee Demographics & Experience</div>',
    unsafe_allow_html=True
)


analysis_df = filtered_df.copy()


analysis_df["Age_Group"] = pd.cut(
    analysis_df["Age"],
    bins=[0, 24, 34, 44, 54, 100],
    labels=[
        "Under 25",
        "25-34",
        "35-44",
        "45-54",
        "55+"
    ]
)


analysis_df["Experience_Group"] = pd.cut(
    analysis_df["YearsAtCompany"],
    bins=[-1, 2, 5, 10, 100],
    labels=[
        "0-2 Years",
        "3-5 Years",
        "6-10 Years",
        "10+ Years"
    ]
)


col1, col2 = st.columns(2)


with col1:

    st.write("**Age Group vs Attrition**")

    age_data = pd.crosstab(
        analysis_df["Age_Group"],
        analysis_df["Attrition"]
    )

    st.bar_chart(
        age_data
    )


with col2:

    st.write("**Years at Company vs Attrition**")

    experience_data = pd.crosstab(
        analysis_df["Experience_Group"],
        analysis_df["Attrition"]
    )

    st.bar_chart(
        experience_data
    )


# ============================================================
# JOB ROLE & SALARY
# ============================================================

st.markdown(
    '<div class="section-title">💼 Job Role & Compensation</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:

    st.write("**Job Role vs Attrition**")

    role_data = pd.crosstab(
        filtered_df["JobRole"],
        filtered_df["Attrition"]
    )

    st.bar_chart(
        role_data
    )


with col2:

    st.write("**Average Monthly Income by Attrition**")

    salary_data = (
        filtered_df.groupby("Attrition")["MonthlyIncome"]
        .mean()
        .round(2)
    )

    st.bar_chart(
        salary_data
    )


# ============================================================
# BUSINESS TRAVEL & JOB LEVEL
# ============================================================

st.markdown(
    '<div class="section-title">✈️ Career & Work Patterns</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:

    st.write("**Business Travel vs Attrition**")

    travel_data = pd.crosstab(
        filtered_df["BusinessTravel"],
        filtered_df["Attrition"]
    )

    st.bar_chart(
        travel_data
    )


with col2:

    st.write("**Job Level vs Attrition**")

    joblevel_data = pd.crosstab(
        filtered_df["JobLevel"],
        filtered_df["Attrition"]
    )

    st.bar_chart(
        joblevel_data
    )


# ============================================================
# PROMOTION HISTORY
# ============================================================

st.markdown(
    '<div class="section-title">📈 Promotion History</div>',
    unsafe_allow_html=True
)


analysis_df["Promotion_Group"] = pd.cut(
    analysis_df["YearsSinceLastPromotion"],
    bins=[-1, 0, 2, 5, 100],
    labels=[
        "No Promotion Yet",
        "1-2 Years",
        "3-5 Years",
        "6+ Years"
    ]
)


promotion_data = pd.crosstab(
    analysis_df["Promotion_Group"],
    analysis_df["Attrition"]
)


st.bar_chart(
    promotion_data
)


# ============================================================
# HR INSIGHTS
# ============================================================

st.markdown(
    '<div class="section-title">💡 HR Analytics Insights</div>',
    unsafe_allow_html=True
)


# Overall insight
st.markdown(
    f"""
    <div class="insight-box">
    <b>Overall Attrition:</b>
    {employees_left:,} out of {total_employees:,} employees in the
    current selection are recorded as having left,
    resulting in an attrition rate of {attrition_rate:.2f}%.
    </div>
    """,
    unsafe_allow_html=True
)


# Overtime insight
if len(filtered_df) > 0:

    overtime_rate = (
        filtered_df.groupby("OverTime")["Attrition"]
        .apply(lambda x: (x == "Yes").mean() * 100)
    )

    if "Yes" in overtime_rate.index:

        st.markdown(
            f"""
            <div class="insight-box">
            <b>Overtime:</b>
            Employees with overtime have a recorded attrition rate of
            {overtime_rate["Yes"]:.2f}% in the current selection.
            </div>
            """,
            unsafe_allow_html=True
        )


# Salary insight
if "Yes" in filtered_df["Attrition"].values:

    left_income = filtered_df[
        filtered_df["Attrition"] == "Yes"
    ]["MonthlyIncome"].mean()

    st.markdown(
        f"""
        <div class="insight-box">
        <b>Compensation:</b>
        Employees recorded as having left have an average monthly income
        of {left_income:,.0f} in the current selection.
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# DATA PREVIEW
# ============================================================

st.markdown(
    '<div class="section-title">📋 Employee Data Preview</div>',
    unsafe_allow_html=True
)


st.dataframe(
    filtered_df.head(20),
    use_container_width=True
)


# ============================================================
# PROJECT INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">📝 Project Information</div>',
    unsafe_allow_html=True
)

st.write(
    """
    **Project:** Employee Attrition & HR Analytics

    **Tools:** Python, Pandas, MySQL, Streamlit

    **Dataset:** IBM HR Analytics Employee Attrition & Performance
    practice dataset

    **Objective:** Analyze employee attrition patterns and identify
    relationships between attrition and factors such as overtime,
    job satisfaction, salary, age, experience, job role, business travel,
    job level, and promotion history.
    """
)


# ============================================================
# FOOTER
# ============================================================

st.write("---")

st.caption(
    "Employee Attrition & HR Analytics | "
    "Data Analyst Portfolio Project"
)
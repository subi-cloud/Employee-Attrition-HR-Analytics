-- =====================================================
-- EMPLOYEE ATTRITION & HR ANALYTICS
-- SQL ANALYSIS
-- Dataset: IBM HR Analytics Employee Attrition Dataset
-- Records: 1470
-- =====================================================

USE hr_analytics;


-- =====================================================
-- 1. OVERALL ATTRITION
-- =====================================================

SELECT
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS Attrition_Rate
FROM employees;


-- =====================================================
-- 2. DEPARTMENT-WISE ATTRITION
-- =====================================================

SELECT
    Department,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS Attrition_Rate
FROM employees
GROUP BY Department
ORDER BY Attrition_Rate DESC;


-- =====================================================
-- 3. OVERTIME VS ATTRITION
-- =====================================================

SELECT
    OverTime,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS Attrition_Rate
FROM employees
GROUP BY OverTime
ORDER BY Attrition_Rate DESC;


-- =====================================================
-- 4. SALARY VS ATTRITION
-- =====================================================

SELECT
    Attrition,
    COUNT(*) AS Employee_Count,
    ROUND(AVG(MonthlyIncome), 2) AS Average_Monthly_Income
FROM employees
GROUP BY Attrition;


-- =====================================================
-- 5. JOB SATISFACTION VS ATTRITION
-- =====================================================

SELECT
    JobSatisfaction,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS Attrition_Rate
FROM employees
GROUP BY JobSatisfaction
ORDER BY JobSatisfaction;


-- =====================================================
-- 6. WORK-LIFE BALANCE VS ATTRITION
-- =====================================================

SELECT
    WorkLifeBalance,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS Attrition_Rate
FROM employees
GROUP BY WorkLifeBalance
ORDER BY WorkLifeBalance;


-- =====================================================
-- 7. AGE GROUP VS ATTRITION
-- =====================================================

SELECT
    CASE
        WHEN Age < 25 THEN 'Under 25'
        WHEN Age BETWEEN 25 AND 34 THEN '25-34'
        WHEN Age BETWEEN 35 AND 44 THEN '35-44'
        WHEN Age BETWEEN 45 AND 54 THEN '45-54'
        ELSE '55+'
    END AS Age_Group,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS Attrition_Rate
FROM employees
GROUP BY Age_Group
ORDER BY Attrition_Rate DESC;


-- =====================================================
-- 8. YEARS AT COMPANY VS ATTRITION
-- =====================================================

SELECT
    CASE
        WHEN YearsAtCompany <= 2 THEN '0-2 Years'
        WHEN YearsAtCompany BETWEEN 3 AND 5 THEN '3-5 Years'
        WHEN YearsAtCompany BETWEEN 6 AND 10 THEN '6-10 Years'
        ELSE '10+ Years'
    END AS Experience_Group,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS Attrition_Rate
FROM employees
GROUP BY Experience_Group
ORDER BY Attrition_Rate DESC;


-- =====================================================
-- 9. PROMOTION HISTORY VS ATTRITION
-- =====================================================

SELECT
    CASE
        WHEN YearsSinceLastPromotion = 0 THEN 'No Promotion Yet'
        WHEN YearsSinceLastPromotion BETWEEN 1 AND 2 THEN '1-2 Years'
        WHEN YearsSinceLastPromotion BETWEEN 3 AND 5 THEN '3-5 Years'
        ELSE '6+ Years'
    END AS Promotion_Group,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS Attrition_Rate
FROM employees
GROUP BY Promotion_Group
ORDER BY Attrition_Rate DESC;


-- =====================================================
-- 10. JOB ROLE VS ATTRITION
-- =====================================================

SELECT
    JobRole,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS Attrition_Rate
FROM employees
GROUP BY JobRole
ORDER BY Attrition_Rate DESC;


-- =====================================================
-- 11. BUSINESS TRAVEL VS ATTRITION
-- =====================================================

SELECT
    BusinessTravel,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS Attrition_Rate
FROM employees
GROUP BY BusinessTravel
ORDER BY Attrition_Rate DESC;


-- =====================================================
-- 12. JOB LEVEL VS ATTRITION
-- =====================================================

SELECT
    JobLevel,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS Attrition_Rate
FROM employees
GROUP BY JobLevel
ORDER BY JobLevel;
-- HAVING Clause - Filtering Grouped Data
-- Learning how to filter groups after GROUP BY

USE employee_org;

-- 1. Basic HAVING with COUNT
-- Departments with more than 3 employees
SELECT 
    dept_id,
    COUNT(*) AS employee_count
FROM EMPLOYEES 
GROUP BY dept_id 
HAVING COUNT(*) > 3
ORDER BY employee_count DESC;

-- Job titles with more than 1 employee
SELECT 
    job_title,
    COUNT(*) AS employee_count
FROM EMPLOYEES 
GROUP BY job_title 
HAVING COUNT(*) > 1
ORDER BY employee_count DESC;

-- 2. HAVING with SUM
-- Departments with total salary cost over 300,000
SELECT 
    dept_id,
    SUM(salary) AS total_salary_cost,
    COUNT(*) AS employee_count
FROM EMPLOYEES 
GROUP BY dept_id 
HAVING SUM(salary) > 300000
ORDER BY total_salary_cost DESC;

-- 3. HAVING with AVG
-- Departments with average salary above 80,000
SELECT 
    dept_id,
    COUNT(*) AS employee_count,
    AVG(salary) AS average_salary
FROM EMPLOYEES 
GROUP BY dept_id 
HAVING AVG(salary) > 80000
ORDER BY average_salary DESC;

-- Job titles with average salary above 70,000
SELECT 
    job_title,
    COUNT(*) AS employee_count,
    AVG(salary) AS average_salary
FROM EMPLOYEES 
GROUP BY job_title 
HAVING AVG(salary) > 70000
ORDER BY average_salary DESC;

-- 4. HAVING with MIN and MAX
-- Departments with salary range (max - min) greater than 40,000
SELECT 
    dept_id,
    COUNT(*) AS employee_count,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary,
    MAX(salary) - MIN(salary) AS salary_range
FROM EMPLOYEES 
GROUP BY dept_id 
HAVING MAX(salary) - MIN(salary) > 40000
ORDER BY salary_range DESC;

-- 5. HAVING with multiple conditions
-- Departments with more than 2 employees AND average salary > 70000
SELECT 
    dept_id,
    COUNT(*) AS employee_count,
    AVG(salary) AS average_salary,
    SUM(salary) AS total_salary
FROM EMPLOYEES 
GROUP BY dept_id 
HAVING COUNT(*) > 2 AND AVG(salary) > 70000
ORDER BY average_salary DESC;

-- 6. WHERE and HAVING together
-- For active employees only, find departments with more than 2 employees and avg salary > 65000
SELECT 
    dept_id,
    COUNT(*) AS active_employee_count,
    AVG(salary) AS average_salary
FROM EMPLOYEES 
WHERE status = 'Active'  -- Filter before grouping
GROUP BY dept_id 
HAVING COUNT(*) > 2 AND AVG(salary) > 65000  -- Filter after grouping
ORDER BY average_salary DESC;

-- 7. HAVING with date functions
-- Departments that hired more than 1 employee after 2020
SELECT 
    dept_id,
    COUNT(*) AS recent_hires,
    AVG(salary) AS avg_salary_recent_hires
FROM EMPLOYEES 
WHERE hire_date > '2020-01-01'
GROUP BY dept_id 
HAVING COUNT(*) > 1
ORDER BY recent_hires DESC;

-- Years with more than 3 hires
SELECT 
    YEAR(hire_date) AS hire_year,
    COUNT(*) AS employees_hired,
    AVG(salary) AS average_starting_salary
FROM EMPLOYEES 
GROUP BY YEAR(hire_date)
HAVING COUNT(*) > 3
ORDER BY hire_year;

-- 8. Project analysis with HAVING
-- Departments with total project budget over 200,000
SELECT 
    dept_id,
    COUNT(*) AS project_count,
    SUM(budget) AS total_budget,
    AVG(budget) AS average_budget
FROM PROJECTS 
GROUP BY dept_id 
HAVING SUM(budget) > 200000
ORDER BY total_budget DESC;

-- Project status with more than 1 project and average budget > 100000
SELECT 
    status,
    COUNT(*) AS project_count,
    SUM(budget) AS total_budget,
    AVG(budget) AS average_budget
FROM PROJECTS 
GROUP BY status 
HAVING COUNT(*) > 1 AND AVG(budget) > 100000
ORDER BY total_budget DESC;

-- 9. Complex HAVING with expressions
-- Salary categories with more than 2 employees
SELECT 
    CASE 
        WHEN salary < 60000 THEN 'Low (< 60K)'
        WHEN salary BETWEEN 60000 AND 90000 THEN 'Medium (60K-90K)'
        ELSE 'High (> 90K)'
    END AS salary_category,
    COUNT(*) AS employee_count,
    AVG(salary) AS average_salary
FROM EMPLOYEES 
GROUP BY 
    CASE 
        WHEN salary < 60000 THEN 'Low (< 60K)'
        WHEN salary BETWEEN 60000 AND 90000 THEN 'Medium (60K-90K)'
        ELSE 'High (> 90K)'
    END
HAVING COUNT(*) > 2
ORDER BY average_salary;

-- Practice Questions:
-- Q1: Find job titles that have an average salary greater than 75,000
-- Q2: Find departments where the total salary expense exceeds 250,000
-- Q3: Find years where more than 2 employees were hired
-- Q4: Find project statuses that have an average budget greater than 150,000
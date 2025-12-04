-- GROUP BY Clause - Grouping Data for Analysis
-- Learning how to group rows and apply aggregate functions

USE employee_org;

-- 1. Basic GROUP BY with COUNT
-- Count employees by department
SELECT dept_id, COUNT(*) AS employee_count 
FROM EMPLOYEES 
GROUP BY dept_id 
ORDER BY dept_id;

-- Count employees by job title
SELECT job_title, COUNT(*) AS employee_count 
FROM EMPLOYEES 
GROUP BY job_title 
ORDER BY employee_count DESC;

-- 2. GROUP BY with SUM
-- Total salary expense by department
SELECT dept_id, SUM(salary) AS total_salary_cost 
FROM EMPLOYEES 
GROUP BY dept_id 
ORDER BY total_salary_cost DESC;

-- Total project budget by department
SELECT dept_id, SUM(budget) AS total_budget 
FROM PROJECTS 
GROUP BY dept_id 
ORDER BY total_budget DESC;

-- 3. GROUP BY with AVG
-- Average salary by department
SELECT dept_id, AVG(salary) AS average_salary 
FROM EMPLOYEES 
GROUP BY dept_id 
ORDER BY average_salary DESC;

-- Average salary by job title
SELECT job_title, AVG(salary) AS average_salary 
FROM EMPLOYEES 
GROUP BY job_title 
ORDER BY average_salary DESC;

-- 4. GROUP BY with MIN and MAX
-- Salary range by department
SELECT 
    dept_id,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary,
    MAX(salary) - MIN(salary) AS salary_range
FROM EMPLOYEES 
GROUP BY dept_id 
ORDER BY dept_id;

-- 5. GROUP BY with multiple aggregate functions
-- Comprehensive department statistics
SELECT 
    dept_id,
    COUNT(*) AS employee_count,
    SUM(salary) AS total_salary,
    AVG(salary) AS average_salary,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary
FROM EMPLOYEES 
GROUP BY dept_id 
ORDER BY dept_id;

-- 6. GROUP BY with multiple columns
-- Employee count and average salary by department and status
SELECT 
    dept_id,
    status,
    COUNT(*) AS employee_count,
    AVG(salary) AS average_salary
FROM EMPLOYEES 
GROUP BY dept_id, status 
ORDER BY dept_id, status;

-- 7. GROUP BY with WHERE clause (filter before grouping)
-- Average salary by department for employees hired after 2020
SELECT 
    dept_id,
    COUNT(*) AS recent_hires,
    AVG(salary) AS avg_salary_recent_hires
FROM EMPLOYEES 
WHERE hire_date > '2020-01-01'
GROUP BY dept_id 
ORDER BY avg_salary_recent_hires DESC;

-- 8. GROUP BY with date functions
-- Employees hired by year
SELECT 
    YEAR(hire_date) AS hire_year,
    COUNT(*) AS employees_hired,
    AVG(salary) AS average_starting_salary
FROM EMPLOYEES 
GROUP BY YEAR(hire_date) 
ORDER BY hire_year;

-- Employees hired by month in 2021
SELECT 
    MONTH(hire_date) AS hire_month,
    MONTHNAME(hire_date) AS month_name,
    COUNT(*) AS employees_hired
FROM EMPLOYEES 
WHERE YEAR(hire_date) = 2021
GROUP BY MONTH(hire_date), MONTHNAME(hire_date)
ORDER BY hire_month;

-- 9. GROUP BY with expressions
-- Salary categories analysis
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
ORDER BY average_salary;

-- 10. Project analysis by status
SELECT 
    status,
    COUNT(*) AS project_count,
    SUM(budget) AS total_budget,
    AVG(budget) AS average_budget
FROM PROJECTS 
GROUP BY status 
ORDER BY total_budget DESC;

-- Practice Questions:
-- Q1: Count the number of projects by status
-- Q2: Find the total and average salary for each job title
-- Q3: Group employees by hire year and show count and average salary
-- Q4: Show department-wise employee count only for departments with more than 2 employees
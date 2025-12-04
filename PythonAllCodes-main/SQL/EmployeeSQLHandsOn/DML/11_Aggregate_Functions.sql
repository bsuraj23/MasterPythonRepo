-- Aggregate Functions - COUNT, SUM, AVG, MIN, MAX
-- Learning how to perform calculations on groups of data

USE employee_org;

-- 1. COUNT function
-- Count total number of employees
SELECT COUNT(*) AS total_employees FROM EMPLOYEES;

-- Count employees with non-null commission
SELECT COUNT(commission_pct) AS employees_with_commission FROM EMPLOYEES;

-- Count distinct job titles
SELECT COUNT(DISTINCT job_title) AS unique_job_ti FROM EMPLOYEES;

-- Count distinct departments
SELECT COUNT(DISTINCT dept_id) AS total_departments FROM EMPLOYEES;

-- 2. SUM function
-- Total salary expense for all employees
SELECT SUM(salary) AS total_salary_expense FROM EMPLOYEES;

-- Total budget for all projects
SELECT SUM(budget) AS total_project_budget FROM PROJECTS;

-- Sum of salaries for IT department (dept_id = 2)
SELECT SUM(salary) AS it_department_salary FROM EMPLOYEES WHERE dept_id = 2;

-- 3. AVG function
-- Average salary across all employees
SELECT AVG(salary) AS average_salary FROM EMPLOYEES;

-- Average salary by department
SELECT AVG(salary) AS average_salary FROM EMPLOYEES WHERE dept_id = 2;

-- Average project budget
SELECT AVG(budget) AS average_project_budget FROM PROJECTS;

-- 4. MIN function
-- Lowest salary in the company
SELECT MIN(salary) AS lowest_salary FROM EMPLOYEES;

-- Earliest hire date
SELECT MIN(hire_date) AS earliest_hire_date FROM EMPLOYEES;

-- Minimum project budget
SELECT MIN(budget) AS min_project_budget FROM PROJECTS;

-- 5. MAX function
-- Highest salary in the company
SELECT MAX(salary) AS highest_salary FROM EMPLOYEES;

-- Latest hire date
SELECT MAX(hire_date) AS latest_hire_date FROM EMPLOYEES;

-- Maximum project budget
SELECT MAX(budget) AS max_project_budget FROM PROJECTS;

-- 6. Combining multiple aggregate functions
SELECT 
    COUNT(*) AS total_employees,
    SUM(salary) AS total_salary_cost,
    AVG(salary) AS average_salary,
    MIN(salary) AS minimum_salary,
    MAX(salary) AS maximum_salary,
    MIN(hire_date) AS earliest_hire,
    MAX(hire_date) AS latest_hire
FROM EMPLOYEES;

-- 7. Aggregate functions with WHERE clause
-- Statistics for employees earning more than 70000
SELECT 
    COUNT(*) AS high_earners_count,
    AVG(salary) AS avg_high_earner_salary,
    MIN(salary) AS min_high_earner_salary,
    MAX(salary) AS max_high_earner_salary
FROM EMPLOYEES 
WHERE salary > 70000;

-- 8. Aggregate functions with expressions
-- Calculate total annual salary cost
SELECT 
    SUM(salary * 12) AS total_annual_cost,
    AVG(salary * 12) AS average_annual_salary
FROM EMPLOYEES;

-- Statistics on years of service
SELECT 
    AVG(DATEDIFF(CURDATE(), hire_date) / 365) AS avg_years_service,
    MIN(DATEDIFF(CURDATE(), hire_date) / 365) AS min_years_service,
    MAX(DATEDIFF(CURDATE(), hire_date) / 365) AS max_years_service
FROM EMPLOYEES;

-- Practice Questions:
-- Q1: What is the total number of projects in the company?
-- Q2: What is the average salary of employees hired after 2020?
-- Q3: What is the sum of all department budgets?
-- Q4: How many employees have a commission percentage greater than 0?
-- ORDER BY Clause - Sorting Results
-- Learning how to sort query results

USE employee_org;

-- 1. ORDER BY single column (ascending - default)
SELECT first_name, last_name, salary 
FROM EMPLOYEES 
ORDER BY salary;

SELECT first_name, last_name, hire_date 
FROM EMPLOYEES 
ORDER BY hire_date;

-- 2. ORDER BY single column (descending)
SELECT first_name, last_name, salary 
FROM EMPLOYEES 
ORDER BY salary DESC;

SELECT first_name, last_name, hire_date 
FROM EMPLOYEES 
ORDER BY hire_date DESC;

-- 3. ORDER BY multiple columns
SELECT first_name, last_name, dept_id, salary 
FROM EMPLOYEES 
ORDER BY dept_id, salary DESC;

SELECT first_name, last_name, job_title, hire_date 
FROM EMPLOYEES 
ORDER BY job_title, hire_date DESC;

-- 4. ORDER BY with WHERE clause
SELECT first_name, last_name, salary, dept_id 
FROM EMPLOYEES 
WHERE salary > 70000 
ORDER BY salary DESC;

SELECT first_name, last_name, hire_date, job_title 
FROM EMPLOYEES 
WHERE hire_date >= '2020-01-01' 
ORDER BY hire_date, last_name;

-- 5. ORDER BY column numbers (using column positions)
SELECT first_name, last_name, salary, dept_id 
FROM EMPLOYEES 
ORDER BY 3 DESC, 4;  -- Sort by 3rd column (salary) DESC, then 4th column (dept_id)

-- 6. ORDER BY with expressions
SELECT first_name, last_name, salary, salary * 12 AS annual_salary 
FROM EMPLOYEES 
ORDER BY salary * 12 DESC;

-- 7. ORDER BY with NULL values
SELECT first_name, last_name, commission_pct 
FROM EMPLOYEES 
ORDER BY commission_pct;  -- NULLs appear first in MySQL

SELECT first_name, last_name, commission_pct 
FROM EMPLOYEES 
ORDER BY commission_pct DESC;  -- NULLs appear last when DESC

-- 8. Complex sorting scenarios
-- Sort by department, then by salary (highest first), then by hire date (newest first)
SELECT first_name, last_name, dept_id, salary, hire_date 
FROM EMPLOYEES 
ORDER BY dept_id, salary DESC, hire_date DESC;

-- 9. ORDER BY with LIMIT (MySQL specific)
-- Top 5 highest paid employees
SELECT first_name, last_name, salary 
FROM EMPLOYEES 
ORDER BY salary DESC 
LIMIT 5;

-- Employees hired in last 3 years, sorted by hire date
SELECT first_name, last_name, hire_date, job_title 
FROM EMPLOYEES 
WHERE hire_date >= DATE_SUB(CURDATE(), INTERVAL 3 YEAR)
ORDER BY hire_date DESC;

-- Practice Questions:
-- Q1: List all employees sorted by last name alphabetically
-- Q2: Show top 3 highest paid employees
-- Q3: List employees by department, then by hire date (oldest first)
-- Q4: Show employees with commission, sorted by commission percentage
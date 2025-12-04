-- Logical Operators - AND, OR, NOT
-- Combining multiple conditions in WHERE clause

USE employee_org;

-- 1. AND operator - all conditions must be true
SELECT first_name, last_name, job_title, salary, dept_id
FROM EMPLOYEES 
WHERE salary > 70000 AND dept_id = 2;

SELECT first_name, last_name, hire_date, job_title
FROM EMPLOYEES 
WHERE hire_date >= '2020-01-01' AND job_title LIKE '%Manager%';

-- 2. OR operator - at least one condition must be true
SELECT first_name, last_name, job_title, dept_id
FROM EMPLOYEES 
WHERE dept_id = 1 OR dept_id = 3;

SELECT first_name, last_name, job_title, salary
FROM EMPLOYEES 
WHERE salary > 100000 OR commission_pct > 0;

-- 3. Combining AND and OR with parentheses
SELECT first_name, last_name, job_title, salary, dept_id
FROM EMPLOYEES 
WHERE (salary > 80000 AND dept_id = 2) OR (salary > 90000 AND dept_id = 4);

SELECT first_name, last_name, job_title, hire_date
FROM EMPLOYEES 
WHERE job_title LIKE '%Manager%' AND (hire_date >= '2018-01-01' OR salary > 100000);

-- 4. NOT operator
SELECT first_name, last_name, job_title, dept_id
FROM EMPLOYEES 
WHERE NOT dept_id = 2;

SELECT first_name, last_name, job_title, salary
FROM EMPLOYEES 
WHERE NOT (salary < 60000 OR commission_pct IS NOT NULL);

-- 5. Complex combinations
-- Find employees who are either:
-- - Managers with salary > 90000, OR
-- - IT employees hired after 2020, OR  
-- - Sales employees with commission
SELECT first_name, last_name, job_title, salary, dept_id, hire_date, commission_pct
FROM EMPLOYEES 
WHERE (job_title LIKE '%Manager%' AND salary > 90000)
   OR (dept_id = 2 AND hire_date > '2020-01-01')
   OR (dept_id = 7 AND commission_pct > 0);

-- 6. Using logical operators with different data types
-- Find active employees in specific departments with recent hire dates
SELECT first_name, last_name, job_title, status, dept_id, hire_date
FROM EMPLOYEES 
WHERE status = 'Active' 
  AND dept_id IN (2, 4, 7) 
  AND hire_date BETWEEN '2019-01-01' AND '2023-12-31';

-- Practice Questions:
-- Q1: Find employees who earn more than 80000 AND work in IT department
-- Q2: Find employees who are either Managers OR earn more than 100000
-- Q3: Find employees who are NOT in Sales department AND hired after 2020
-- Q4: Find employees who work in (HR OR Finance) AND earn between 60000-90000
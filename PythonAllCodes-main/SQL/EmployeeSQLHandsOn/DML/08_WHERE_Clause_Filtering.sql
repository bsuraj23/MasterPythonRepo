-- WHERE Clause - Filtering Data
-- Learning how to filter records based on conditions

USE employee_org;

-- 1. Simple WHERE with equality
SELECT * FROM EMPLOYEES WHERE dept_id = 2;

-- 2. WHERE with text comparison
SELECT * FROM EMPLOYEES WHERE job_title = 'Sales Representative';

-- 3. WHERE with inequality operators
SELECT first_name, last_name, salary 
FROM EMPLOYEES 
WHERE salary > 80000;

SELECT first_name, last_name, salary 
FROM EMPLOYEES 
WHERE salary <= 60000;

-- 4. WHERE with date comparisons
SELECT first_name, last_name, hire_date 
FROM EMPLOYEES 
WHERE hire_date >= '2020-01-01';

SELECT first_name, last_name, hire_date 
FROM EMPLOYEES 
WHERE hire_date BETWEEN '2019-01-01' AND '2021-12-31';

-- 5. WHERE with LIKE pattern matching
-- Find employees whose first name starts with 'J'
SELECT * FROM EMPLOYEES WHERE first_name LIKE 'J%';

-- Find employees whose last name ends with 'son'
SELECT * FROM EMPLOYEES WHERE last_name LIKE '%son';

-- Find employees whose email contains 'gmail'
SELECT * FROM EMPLOYEES WHERE email LIKE '%gmail%';

-- 6. WHERE with IN operator
SELECT * FROM EMPLOYEES WHERE dept_id IN (1, 2, 3);

SELECT * FROM EMPLOYEES WHERE job_title IN ('Manager', 'Senior Software Engineer');

-- 7. WHERE with NULL values
SELECT * FROM EMPLOYEES WHERE commission_pct IS NULL;
SELECT * FROM EMPLOYEES WHERE commission_pct IS NOT NULL;

-- 8. WHERE with NOT operator
SELECT * FROM EMPLOYEES WHERE NOT dept_id = 2;
SELECT * FROM EMPLOYEES WHERE job_title NOT LIKE '%Manager%';

-- Practice Questions:
-- Q1: Find all employees hired after 2020
-- Q2: Find employees with salary between 50000 and 90000
-- Q3: Find all employees whose job title contains 'Developer'
-- Q4: Find employees in HR or Finance departments
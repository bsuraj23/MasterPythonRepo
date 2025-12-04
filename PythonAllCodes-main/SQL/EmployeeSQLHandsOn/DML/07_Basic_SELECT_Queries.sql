-- Basic SELECT Queries
-- Learning basic data retrieval from single table

USE employee_org;

-- 1. Select all columns from employees table
SELECT * FROM EMPLOYEES;

-- 2. Select specific columns
SELECT first_name, last_name, job_title, salary FROM EMPLOYEES;

-- 3. Select with alias for better readability
SELECT 
    first_name AS 'First Name',
    last_name AS 'Last Name',
    job_title AS 'Position',
    salary AS 'Annual Salary'
FROM EMPLOYEES;

-- 4. Select distinct values
SELECT DISTINCT job_title FROM EMPLOYEES;
SELECT DISTINCT dept_id FROM EMPLOYEES;

-- 5. Count total records
SELECT COUNT(*) AS 'Total Employees' FROM EMPLOYEES;

-- 6. Select with simple calculations
SELECT 
    first_name,
    last_name,
    salary,
    salary * 12 AS 'Annual Salary',
    salary / 12 AS 'Monthly Salary'
FROM EMPLOYEES;

-- Practice Questions:
-- Q1: Display all department names
-- Q2: Show unique job titles in the company
-- Q3: Display employee names and their email addresses
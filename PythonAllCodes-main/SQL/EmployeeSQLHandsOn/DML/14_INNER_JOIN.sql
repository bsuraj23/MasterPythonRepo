-- INNER JOIN - Combining Data from Multiple Tables
-- Learning how to join related tables using INNER JOIN

USE employee_org;

-- 1. Basic INNER JOIN - Employees with Department Information
SELECT 
    e.first_name,
    e.last_name,
    e.job_title,
    e.salary,
    d.dept_name,
    d.location
FROM EMPLOYEES e
INNER JOIN DEPARTMENTS d ON e.dept_id = d.dept_id
ORDER BY d.dept_name, e.last_name;

-- 2. INNER JOIN with WHERE clause
-- IT Department employees with their department details
SELECT 
    e.first_name,
    e.last_name,
    e.job_title,
    e.salary,
    d.dept_name,
    d.location
FROM EMPLOYEES e
INNER JOIN DEPARTMENTS d ON e.dept_id = d.dept_id
WHERE d.dept_name = 'Information Technology'
ORDER BY e.salary DESC;

-- 3. INNER JOIN with aggregate functions
-- Department-wise employee count and average salary
SELECT 
    d.dept_name,
    d.location,
    COUNT(e.emp_id) AS employee_count,
    AVG(e.salary) AS average_salary,
    SUM(e.salary) AS total_salary_cost
FROM DEPARTMENTS d
INNER JOIN EMPLOYEES e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name, d.location
ORDER BY employee_count DESC;

-- 4. Multiple INNER JOINs - Employee, Department, and Manager Information
SELECT 
    e.first_name AS employee_first_name,
    e.last_name AS employee_last_name,
    e.job_title,
    d.dept_name,
    CONCAT(m.first_name, ' ', m.last_name) AS manager_name
FROM EMPLOYEES e
INNER JOIN DEPARTMENTS d ON e.dept_id = d.dept_id
INNER JOIN EMPLOYEES m ON e.manager_id = m.emp_id
ORDER BY d.dept_name, e.last_name;

-- 5. INNER JOIN - Projects with Department Information
SELECT 
    p.project_name,
    p.budget,
    p.status,
    p.start_date,
    p.end_date,
    d.dept_name,
    d.location
FROM PROJECTS p
INNER JOIN DEPARTMENTS d ON p.dept_id = d.dept_id
ORDER BY d.dept_name, p.start_date;

-- 6. INNER JOIN - Employee Project Assignments
SELECT 
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    e.job_title,
    p.project_name,
    ep.role AS project_role,
    ep.hours_allocated,
    ep.start_date AS assignment_start
FROM EMPLOYEES e
INNER JOIN EMPLOYEE_PROJECTS ep ON e.emp_id = ep.emp_id
INNER JOIN PROJECTS p ON ep.project_id = p.project_id
ORDER BY p.project_name, ep.role;

-- 7. Complex INNER JOIN with multiple tables
-- Complete project information with employee and department details
SELECT 
    p.project_name,
    p.status AS project_status,
    p.budget,
    d.dept_name,
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    e.job_title,
    ep.role AS project_role,
    ep.hours_allocated
FROM PROJECTS p
INNER JOIN DEPARTMENTS d ON p.dept_id = d.dept_id
INNER JOIN EMPLOYEE_PROJECTS ep ON p.project_id = ep.project_id
INNER JOIN EMPLOYEES e ON ep.emp_id = e.emp_id
WHERE p.status = 'In Progress'
ORDER BY p.project_name, ep.role;

-- 8. INNER JOIN with calculations
-- Project workload analysis
SELECT 
    p.project_name,
    COUNT(ep.emp_id) AS team_size,
    SUM(ep.hours_allocated) AS total_hours_allocated,
    AVG(e.salary) AS average_team_salary,
    SUM(e.salary) AS total_team_salary_cost
FROM PROJECTS p
INNER JOIN EMPLOYEE_PROJECTS ep ON p.project_id = ep.project_id
INNER JOIN EMPLOYEES e ON ep.emp_id = e.emp_id
GROUP BY p.project_id, p.project_name
ORDER BY total_hours_allocated DESC;

-- 9. INNER JOIN with date functions
-- Recent salary changes with employee and approver details
SELECT 
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    e.job_title,
    d.dept_name,
    sh.old_salary,
    sh.new_salary,
    sh.change_date,
    sh.reason,
    CONCAT(approver.first_name, ' ', approver.last_name) AS approved_by
FROM SALARY_HISTORY sh
INNER JOIN EMPLOYEES e ON sh.emp_id = e.emp_id
INNER JOIN DEPARTMENTS d ON e.dept_id = d.dept_id
INNER JOIN EMPLOYEES approver ON sh.approved_by = approver.emp_id
WHERE sh.change_date >= '2023-01-01'
ORDER BY sh.change_date DESC;

-- 10. Department managers with their department information
SELECT 
    d.dept_name,
    d.location,
    d.budget,
    CONCAT(m.first_name, ' ', m.last_name) AS manager_name,
    m.job_title,
    m.salary AS manager_salary,
    m.hire_date
FROM DEPARTMENTS d
INNER JOIN EMPLOYEES m ON d.manager_id = m.emp_id
ORDER BY d.dept_name;

-- Practice Questions:
-- Q1: List all employees with their department names and locations
-- Q2: Show all projects with their department names, sorted by budget
-- Q3: Find all employees working on 'In Progress' projects
-- Q4: Show salary history with employee names and department names
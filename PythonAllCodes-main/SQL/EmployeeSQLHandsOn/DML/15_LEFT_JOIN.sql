-- LEFT JOIN - Including All Records from Left Table
-- Learning how to include all records from the left table, even without matches

USE employee_org;

-- 1. Basic LEFT JOIN - All Departments with Employee Count
-- Shows all departments, even those without employees
SELECT 
    d.dept_name,
    d.location,
    d.budget,
    COUNT(e.emp_id) AS employee_count
FROM DEPARTMENTS d
LEFT JOIN EMPLOYEES e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name, d.location, d.budget
ORDER BY employee_count DESC;

-- 2. LEFT JOIN to find departments without employees
SELECT 
    d.dept_name,
    d.location,
    d.budget
FROM DEPARTMENTS d
LEFT JOIN EMPLOYEES e ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;

-- 3. LEFT JOIN - All Employees with Project Assignments
-- Shows all employees, including those not assigned to any project
SELECT 
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    e.job_title,
    e.salary,
    p.project_name,
    ep.role AS project_role,
    ep.hours_allocated
FROM EMPLOYEES e
LEFT JOIN EMPLOYEE_PROJECTS ep ON e.emp_id = ep.emp_id
LEFT JOIN PROJECTS p ON ep.project_id = p.project_id
ORDER BY e.last_name, p.project_name;

-- 4. LEFT JOIN to find employees without project assignments
SELECT 
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    e.job_title,
    d.dept_name,
    e.salary
FROM EMPLOYEES e
LEFT JOIN EMPLOYEE_PROJECTS ep ON e.emp_id = ep.emp_id
LEFT JOIN DEPARTMENTS d ON e.dept_id = d.dept_id
WHERE ep.emp_id IS NULL
ORDER BY e.salary DESC;

-- 5. LEFT JOIN - All Projects with Team Information
-- Shows all projects, including those with no team assigned yet
SELECT 
    p.project_name,
    p.status,
    p.budget,
    d.dept_name,
    COUNT(ep.emp_id) AS team_size,
    SUM(ep.hours_allocated) AS total_hours_allocated
FROM PROJECTS p
LEFT JOIN EMPLOYEE_PROJECTS ep ON p.project_id = ep.project_id
LEFT JOIN DEPARTMENTS d ON p.dept_id = d.dept_id
GROUP BY p.project_id, p.project_name, p.status, p.budget, d.dept_name
ORDER BY team_size DESC;

-- 6. LEFT JOIN to find projects without team members
SELECT 
    p.project_name,
    p.status,
    p.budget,
    d.dept_name,
    p.start_date
FROM PROJECTS p
LEFT JOIN EMPLOYEE_PROJECTS ep ON p.project_id = ep.project_id
LEFT JOIN DEPARTMENTS d ON p.dept_id = d.dept_id
WHERE ep.emp_id IS NULL
ORDER BY p.start_date;

-- 7. LEFT JOIN - All Employees with Salary History
-- Shows all employees, including those with no salary changes
SELECT 
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    e.job_title,
    e.salary AS current_salary,
    COUNT(sh.history_id) AS salary_changes,
    MAX(sh.change_date) AS last_salary_change,
    MAX(sh.new_salary) AS last_new_salary
FROM EMPLOYEES e
LEFT JOIN SALARY_HISTORY sh ON e.emp_id = sh.emp_id
GROUP BY e.emp_id, e.first_name, e.last_name, e.job_title, e.salary
ORDER BY salary_changes DESC;

-- 8. LEFT JOIN to find employees with no salary history
SELECT 
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    e.job_title,
    e.salary,
    e.hire_date,
    d.dept_name
FROM EMPLOYEES e
LEFT JOIN SALARY_HISTORY sh ON e.emp_id = sh.emp_id
LEFT JOIN DEPARTMENTS d ON e.dept_id = d.dept_id
WHERE sh.emp_id IS NULL
ORDER BY e.hire_date;

-- 9. LEFT JOIN with aggregate functions and filtering
-- Department project summary including departments with no projects
SELECT 
    d.dept_name,
    d.location,
    d.budget AS dept_budget,
    COUNT(p.project_id) AS project_count,
    COALESCE(SUM(p.budget), 0) AS total_project_budget,
    COALESCE(AVG(p.budget), 0) AS avg_project_budget
FROM DEPARTMENTS d
LEFT JOIN PROJECTS p ON d.dept_id = p.dept_id
GROUP BY d.dept_id, d.dept_name, d.location, d.budget
ORDER BY project_count DESC;

-- 10. Complex LEFT JOIN - Employee workload analysis
-- All employees with their total project hours and project count
SELECT 
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    e.job_title,
    d.dept_name,
    e.salary,
    COUNT(ep.project_id) AS projects_assigned,
    COALESCE(SUM(ep.hours_allocated), 0) AS total_hours_allocated,
    CASE 
        WHEN SUM(ep.hours_allocated) IS NULL THEN 'Available'
        WHEN SUM(ep.hours_allocated) < 40 THEN 'Under-allocated'
        WHEN SUM(ep.hours_allocated) = 40 THEN 'Fully allocated'
        ELSE 'Over-allocated'
    END AS allocation_status
FROM EMPLOYEES e
LEFT JOIN EMPLOYEE_PROJECTS ep ON e.emp_id = ep.emp_id
LEFT JOIN DEPARTMENTS d ON e.dept_id = d.dept_id
WHERE e.status = 'Active'
GROUP BY e.emp_id, e.first_name, e.last_name, e.job_title, d.dept_name, e.salary
ORDER BY total_hours_allocated DESC;

-- Practice Questions:
-- Q1: Show all departments with their project counts (include departments with 0 projects)
-- Q2: List all employees with their manager names (include employees without managers)
-- Q3: Find all projects with their team member counts (include projects with no team)
-- Q4: Show employees who have never received a salary increase
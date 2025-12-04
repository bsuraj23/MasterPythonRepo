-- MySQL Workbench Comprehensive Test Script
-- This script tests all DDL and DML files for MySQL compatibility
-- Run this script in MySQL Workbench to verify everything works correctly

-- ===========================================
-- STEP 1: DATABASE SETUP
-- ===========================================

-- Drop database if exists (for clean testing)
DROP DATABASE IF EXISTS employee_org;

-- Create new database
CREATE DATABASE employee_org 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- Use the database
USE employee_org;

-- ===========================================
-- STEP 2: CREATE TABLES (DDL Phase)
-- ===========================================

-- 1. Create DEPARTMENTS table (without foreign keys)
CREATE TABLE DEPARTMENTS (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL UNIQUE,
    location VARCHAR(100) NOT NULL,
    budget DECIMAL(15,2) DEFAULT 0,
    manager_id INT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Check constraint for budget
    CONSTRAINT chk_dept_budget CHECK (budget >= 0)
);

-- 2. Create EMPLOYEES table (without foreign keys)
CREATE TABLE EMPLOYEES (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    hire_date DATE NOT NULL,
    job_title VARCHAR(100) NOT NULL,
    dept_id INT NOT NULL,
    manager_id INT,
    salary DECIMAL(10,2) NOT NULL,
    commission_pct DECIMAL(3,2) DEFAULT 0,
    status ENUM('Active', 'Inactive', 'Terminated') DEFAULT 'Active',
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    -- Check constraints
    CONSTRAINT chk_emp_salary CHECK (salary > 0),
    CONSTRAINT chk_emp_commission CHECK (commission_pct >= 0 AND commission_pct <= 1)
);

-- 3. Create PROJECTS table (without foreign keys)
CREATE TABLE PROJECTS (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    budget DECIMAL(15,2) DEFAULT 0,
    status ENUM('Planning', 'In Progress', 'Completed', 'On Hold', 'Cancelled') DEFAULT 'Planning',
    priority ENUM('Low', 'Medium', 'High', 'Critical') DEFAULT 'Medium',
    dept_id INT NOT NULL,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Check constraints
    CONSTRAINT chk_project_budget CHECK (budget >= 0),
    CONSTRAINT chk_project_dates CHECK (end_date IS NULL OR end_date >= start_date)
);

-- 4. Create EMPLOYEE_PROJECTS table (without foreign keys)
CREATE TABLE EMPLOYEE_PROJECTS (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT NOT NULL,
    project_id INT NOT NULL,
    role VARCHAR(50) NOT NULL,
    hours_allocated DECIMAL(5,2) DEFAULT 0,
    start_date DATE NOT NULL,
    end_date DATE,
    status ENUM('Active', 'Completed', 'On Hold') DEFAULT 'Active',
    notes TEXT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Unique constraint to prevent duplicate assignments
    CONSTRAINT uk_emp_project UNIQUE (emp_id, project_id),
    
    -- Check constraints
    CONSTRAINT chk_emp_proj_hours CHECK (hours_allocated >= 0),
    CONSTRAINT chk_emp_proj_dates CHECK (end_date IS NULL OR end_date >= start_date)
);

-- 5. Create SALARY_HISTORY table (without foreign keys)
CREATE TABLE SALARY_HISTORY (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT NOT NULL,
    old_salary DECIMAL(10,2),
    new_salary DECIMAL(10,2) NOT NULL,
    change_date DATE NOT NULL,
    reason VARCHAR(255),
    approved_by INT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Check constraints
    CONSTRAINT chk_salary_hist_old CHECK (old_salary IS NULL OR old_salary > 0),
    CONSTRAINT chk_salary_hist_new CHECK (new_salary > 0)
);

-- 6. Create ATTENDANCE table (without foreign keys)
CREATE TABLE ATTENDANCE (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    time_in TIME,
    time_out TIME,
    total_hours DECIMAL(4,2) DEFAULT 0,
    status ENUM('Present', 'Absent', 'Late', 'Half Day', 'Holiday', 'Leave') DEFAULT 'Present',
    notes TEXT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Unique constraint to prevent duplicate entries for same employee on same date
    CONSTRAINT uk_emp_date UNIQUE (emp_id, attendance_date),
    
    -- Check constraints
    CONSTRAINT chk_attendance_hours CHECK (total_hours >= 0 AND total_hours <= 24),
    CONSTRAINT chk_attendance_times CHECK (time_out IS NULL OR time_in IS NULL OR time_out >= time_in)
);

-- ===========================================
-- STEP 3: INSERT SAMPLE DATA
-- ===========================================

-- Insert Departments
INSERT INTO DEPARTMENTS (dept_name, location, budget) VALUES
('Human Resources', 'New York', 500000.00),
('Information Technology', 'San Francisco', 2000000.00),
('Finance', 'Chicago', 800000.00),
('Marketing', 'Los Angeles', 600000.00),
('Operations', 'Dallas', 750000.00),
('Research & Development', 'Seattle', 1500000.00),
('Sales', 'Miami', 900000.00),
('Customer Service', 'Phoenix', 400000.00);

-- Insert Employees
INSERT INTO EMPLOYEES (first_name, last_name, email, phone, hire_date, job_title, dept_id, salary, commission_pct, status) VALUES
-- IT Department (dept_id = 2)
('John', 'Smith', 'john.smith@company.com', '555-0101', '2020-01-15', 'Senior Software Engineer', 2, 95000.00, 0, 'Active'),
('Sarah', 'Johnson', 'sarah.johnson@company.com', '555-0102', '2019-03-20', 'IT Manager', 2, 120000.00, 0, 'Active'),
('Mike', 'Davis', 'mike.davis@company.com', '555-0103', '2021-06-10', 'Database Administrator', 2, 85000.00, 0, 'Active'),
('Lisa', 'Wilson', 'lisa.wilson@company.com', '555-0104', '2022-02-01', 'Web Developer', 2, 75000.00, 0, 'Active'),
('David', 'Brown', 'david.brown@company.com', '555-0105', '2020-09-15', 'System Analyst', 2, 80000.00, 0, 'Active'),

-- HR Department (dept_id = 1)
('Emily', 'Taylor', 'emily.taylor@company.com', '555-0201', '2018-05-12', 'HR Manager', 1, 90000.00, 0, 'Active'),
('Robert', 'Anderson', 'robert.anderson@company.com', '555-0202', '2021-01-20', 'HR Specialist', 1, 60000.00, 0, 'Active'),
('Jennifer', 'Thomas', 'jennifer.thomas@company.com', '555-0203', '2020-11-05', 'Recruiter', 1, 55000.00, 0, 'Active'),

-- Finance Department (dept_id = 3)
('Michael', 'Jackson', 'michael.jackson@company.com', '555-0301', '2017-08-30', 'Finance Manager', 3, 110000.00, 0, 'Active'),
('Amanda', 'White', 'amanda.white@company.com', '555-0302', '2019-12-15', 'Senior Accountant', 3, 70000.00, 0, 'Active'),
('James', 'Harris', 'james.harris@company.com', '555-0303', '2021-04-22', 'Financial Analyst', 3, 65000.00, 0, 'Active'),

-- Marketing Department (dept_id = 4)
('Jessica', 'Martin', 'jessica.martin@company.com', '555-0401', '2020-07-08', 'Marketing Manager', 4, 95000.00, 0, 'Active'),
('Christopher', 'Thompson', 'christopher.thompson@company.com', '555-0402', '2021-09-12', 'Marketing Specialist', 4, 60000.00, 0, 'Active'),
('Ashley', 'Garcia', 'ashley.garcia@company.com', '555-0403', '2022-01-18', 'Social Media Manager', 4, 58000.00, 0, 'Active'),

-- Sales Department (dept_id = 7)
('Daniel', 'Martinez', 'daniel.martinez@company.com', '555-0701', '2019-06-25', 'Sales Manager', 7, 100000.00, 0.10, 'Active'),
('Michelle', 'Robinson', 'michelle.robinson@company.com', '555-0702', '2020-10-30', 'Sales Representative', 7, 55000.00, 0.15, 'Active'),
('Kevin', 'Clark', 'kevin.clark@company.com', '555-0703', '2021-03-14', 'Sales Representative', 7, 52000.00, 0.12, 'Active'),

-- Operations Department (dept_id = 5)
('Rachel', 'Rodriguez', 'rachel.rodriguez@company.com', '555-0501', '2018-11-20', 'Operations Manager', 5, 88000.00, 0, 'Active'),
('Ryan', 'Lewis', 'ryan.lewis@company.com', '555-0502', '2020-05-15', 'Operations Specialist', 5, 62000.00, 0, 'Active'),

-- R&D Department (dept_id = 6)
('Stephanie', 'Lee', 'stephanie.lee@company.com', '555-0601', '2019-02-28', 'Research Manager', 6, 105000.00, 0, 'Active'),
('Andrew', 'Walker', 'andrew.walker@company.com', '555-0602', '2021-08-05', 'Research Scientist', 6, 90000.00, 0, 'Active'),

-- Customer Service Department (dept_id = 8)
('Nicole', 'Hall', 'nicole.hall@company.com', '555-0801', '2020-12-10', 'Customer Service Manager', 8, 65000.00, 0, 'Active'),
('Brandon', 'Allen', 'brandon.allen@company.com', '555-0802', '2021-07-20', 'Customer Service Rep', 8, 40000.00, 0, 'Active');

-- ===========================================
-- STEP 4: ADD FOREIGN KEY CONSTRAINTS
-- ===========================================

-- Add foreign key constraints after all tables and data are created
ALTER TABLE DEPARTMENTS 
ADD CONSTRAINT fk_dept_manager 
FOREIGN KEY (manager_id) REFERENCES EMPLOYEES(emp_id);

ALTER TABLE EMPLOYEES 
ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY (dept_id) REFERENCES DEPARTMENTS(dept_id);

ALTER TABLE PROJECTS 
ADD CONSTRAINT fk_project_dept 
FOREIGN KEY (dept_id) REFERENCES DEPARTMENTS(dept_id);

ALTER TABLE EMPLOYEE_PROJECTS 
ADD CONSTRAINT fk_emp_proj_emp 
FOREIGN KEY (emp_id) REFERENCES EMPLOYEES(emp_id) ON DELETE CASCADE;

ALTER TABLE EMPLOYEE_PROJECTS 
ADD CONSTRAINT fk_emp_proj_project 
FOREIGN KEY (project_id) REFERENCES PROJECTS(project_id) ON DELETE CASCADE;

ALTER TABLE SALARY_HISTORY 
ADD CONSTRAINT fk_salary_emp 
FOREIGN KEY (emp_id) REFERENCES EMPLOYEES(emp_id) ON DELETE CASCADE;

ALTER TABLE SALARY_HISTORY 
ADD CONSTRAINT fk_salary_approver 
FOREIGN KEY (approved_by) REFERENCES EMPLOYEES(emp_id);

ALTER TABLE ATTENDANCE 
ADD CONSTRAINT fk_attendance_emp 
FOREIGN KEY (emp_id) REFERENCES EMPLOYEES(emp_id) ON DELETE CASCADE;

-- ===========================================
-- STEP 5: TEST BASIC QUERIES
-- ===========================================

-- Test 1: Basic SELECT queries
SELECT 'Test 1: Basic SELECT - All Employees' AS test_description;
SELECT emp_id, first_name, last_name, job_title, salary FROM EMPLOYEES LIMIT 5;

-- Test 2: JOIN queries
SELECT 'Test 2: INNER JOIN - Employees with Departments' AS test_description;
SELECT 
    e.first_name,
    e.last_name,
    e.job_title,
    d.dept_name,
    d.location
FROM EMPLOYEES e
INNER JOIN DEPARTMENTS d ON e.dept_id = d.dept_id
LIMIT 5;

-- Test 3: Aggregate functions
SELECT 'Test 3: Aggregate Functions' AS test_description;
SELECT 
    COUNT(*) AS total_employees,
    AVG(salary) AS average_salary,
    MIN(salary) AS minimum_salary,
    MAX(salary) AS maximum_salary
FROM EMPLOYEES;

-- Test 4: GROUP BY with HAVING
SELECT 'Test 4: GROUP BY with HAVING' AS test_description;
SELECT 
    d.dept_name,
    COUNT(e.emp_id) AS employee_count,
    AVG(e.salary) AS average_salary
FROM DEPARTMENTS d
INNER JOIN EMPLOYEES e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING COUNT(e.emp_id) >= 2
ORDER BY average_salary DESC;

-- ===========================================
-- STEP 6: VERIFICATION QUERIES
-- ===========================================

-- Show all tables created
SELECT 'Test 5: Verify Tables Created' AS test_description;
SHOW TABLES;

-- Show all foreign key constraints
SELECT 'Test 6: Verify Foreign Key Constraints' AS test_description;
SELECT 
    TABLE_NAME,
    CONSTRAINT_NAME,
    CONSTRAINT_TYPE,
    REFERENCED_TABLE_NAME
FROM information_schema.TABLE_CONSTRAINTS 
WHERE TABLE_SCHEMA = 'employee_org'
AND CONSTRAINT_TYPE = 'FOREIGN KEY'
ORDER BY TABLE_NAME;

-- Show record counts for all tables
SELECT 'Test 7: Verify Data Insertion' AS test_description;
SELECT 'DEPARTMENTS' AS table_name, COUNT(*) AS record_count FROM DEPARTMENTS
UNION ALL
SELECT 'EMPLOYEES' AS table_name, COUNT(*) AS record_count FROM EMPLOYEES
UNION ALL
SELECT 'PROJECTS' AS table_name, COUNT(*) AS record_count FROM PROJECTS
UNION ALL
SELECT 'EMPLOYEE_PROJECTS' AS table_name, COUNT(*) AS record_count FROM EMPLOYEE_PROJECTS
UNION ALL
SELECT 'SALARY_HISTORY' AS table_name, COUNT(*) AS record_count FROM SALARY_HISTORY
UNION ALL
SELECT 'ATTENDANCE' AS table_name, COUNT(*) AS record_count FROM ATTENDANCE;

-- ===========================================
-- SUCCESS MESSAGE
-- ===========================================
SELECT 'ALL TESTS COMPLETED SUCCESSFULLY!' AS result, 
       'Employee Organization Database is ready for use in MySQL Workbench!' AS message;
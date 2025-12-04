-- Insert Sample Data into EMPLOYEES table
-- Run this after departments are created

USE employee_org;
##TODO Fix this commision_pct insert error
-- Insert employees (without manager_id first, will update later)
INSERT INTO EMPLOYEES (first_name, last_name, email, phone, hire_date, job_title, dept_id, salary, commission_pct, status) 
VALUES
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

-- Show inserted data
SELECT COUNT(*) AS 'Total Employees' FROM EMPLOYEES;
SELECT dept_id, COUNT(*) AS 'Employee Count' FROM EMPLOYEES GROUP BY dept_id;
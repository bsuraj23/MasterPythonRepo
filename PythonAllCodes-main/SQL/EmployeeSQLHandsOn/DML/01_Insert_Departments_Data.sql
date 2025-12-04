-- Insert Sample Data into DEPARTMENTS table
-- This should be run first before inserting employees

USE employee_org;

-- Insert departments
INSERT INTO DEPARTMENTS (dept_name, location, budget,Time) VALUES
('Human Resources', 'New York', 500000.00),
('Information Technology', 'San Francisco', 2000000.00),
('Finance', 'Chicago', 800000.00),
('Marketing', 'Los Angeles', 600000.00),
('Operations', 'Dallas', 750000.00),
('Research & Development', 'Seattle', 1500000.00),
('Sales', 'Miami', 900000.00),
('Customer Service', 'Denver', 400000.00);

-- Show inserted data
SELECT * FROM DEPARTMENTS;

-- Show department count
SELECT COUNT(*) AS 'Total Departments' FROM DEPARTMENTS;
-- Complete Setup Script for Employee Organization Database
-- Run this script in MySQL Workbench to set up the entire learning environment

-- Step 1: Create Database and Tables
SOURCE DDL/01_Create_Database.sql;
SOURCE DDL/02_Create_Departments_Table.sql;
SOURCE DDL/03_Create_Employees_Table.sql;
SOURCE DDL/04_Create_Projects_Table.sql;
SOURCE DDL/05_Create_Employee_Projects_Table.sql;
SOURCE DDL/06_Create_Salary_History_Table.sql;
SOURCE DDL/07_Create_Attendance_Table.sql;

-- Step 2: Insert Sample Data
SOURCE DML/01_Insert_Departments_Data.sql;
SOURCE DML/02_Insert_Employees_Data.sql;
SOURCE DML/03_Update_Manager_Relationships.sql;
SOURCE DML/04_Insert_Projects_Data.sql;
SOURCE DML/05_Insert_Employee_Projects_Data.sql;
SOURCE DML/06_Insert_Salary_History_Data.sql;

-- Step 3: Add Foreign Key Constraints
SOURCE DDL/08_Add_Foreign_Key_Constraints.sql;

-- Verification: Show all tables and data counts
SHOW TABLES;

SELECT 'DEPARTMENTS' AS Table_Name, COUNT(*) AS Record_Count FROM DEPARTMENTS
UNION ALL
SELECT 'EMPLOYEES', COUNT(*) FROM EMPLOYEES
UNION ALL
SELECT 'PROJECTS', COUNT(*) FROM PROJECTS
UNION ALL
SELECT 'EMPLOYEE_PROJECTS', COUNT(*) FROM EMPLOYEE_PROJECTS
UNION ALL
SELECT 'SALARY_HISTORY', COUNT(*) FROM SALARY_HISTORY;

-- Setup complete message
SELECT 'Employee Organization Database Setup Complete!' AS Status,
       'Ready for SQL Learning!' AS Message;
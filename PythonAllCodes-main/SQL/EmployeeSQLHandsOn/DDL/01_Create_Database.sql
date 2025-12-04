-- Employee Organization Database Creation
-- MySQL Compatible DDL Script

-- Create Database
CREATE DATABASE IF NOT EXISTS employee_org;
USE employee_org;

-- Drop tables if they exist (for clean setup)
DROP TABLE IF EXISTS ATTENDANCE;
DROP TABLE IF EXISTS SALARY_HISTORY;
DROP TABLE IF EXISTS EMPLOYEE_PROJECTS;
DROP TABLE IF EXISTS PROJECTS;
DROP TABLE IF EXISTS EMPLOYEES;
DROP TABLE IF EXISTS DEPARTMENTS;

-- Show current database
SELECT DATABASE() AS CurrentDatabase;
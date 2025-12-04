-- Add Foreign Key Constraints After All Tables Created
-- This script adds all foreign key constraints that reference other tables


CREATE TABLE Students (
    Roll_No INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Address VARCHAR(100),dddddd
    Phone INT,
    Age INT CHECK (Age > 0)
);

Select * from Students;

INSERT INTO `medha`.`Students` (`Roll_No`, `Name`, `Address`, `Phone`, `Age`, `email`) 
VALUES ('Santosh', '1', 'Address_1', '98989898', '23', 'mail.com');



ALTER TABLE Students  
ADD column email varchar(15) ;





-- Add foreign key constraint for department manager
ALTER TABLE DEPARTMENTS 
ADD CONSTRAINT fk_dept_manager  column add 
FOREIGN KEY (manager_id) REFERENCES EMPLOYEES(emp_id);

-- Add foreign key constraint for employee department
ALTER TABLE EMPLOYEES 
ADD CONSTRAINT fk_emp_dept 
FOREIGN KEY (dept_id) REFERENCES DEPARTMENTS(dept_id);

-- Add foreign key constraint for project department
ALTER TABLE PROJECTS 
ADD CONSTRAINT fk_project_dept 
FOREIGN KEY (dept_id) REFERENCES DEPARTMENTS(dept_id);

-- Add foreign key constraints for employee-project mapping
ALTER TABLE EMPLOYEE_PROJECTS 
ADD CONSTRAINT fk_emp_proj_emp 
FOREIGN KEY (emp_id) REFERENCES EMPLOYEES(emp_id) ON DELETE CASCADE;

ALTER TABLE EMPLOYEE_PROJECTS 
ADD CONSTRAINT fk_emp_proj_project 
FOREIGN KEY (project_id) REFERENCES PROJECTS(project_id) ON DELETE CASCADE;

-- Add foreign key constraints for salary history
ALTER TABLE SALARY_HISTORY 
ADD CONSTRAINT fk_salary_emp 
FOREIGN KEY (emp_id) REFERENCES EMPLOYEES(emp_id) ON DELETE CASCADE;

ALTER TABLE SALARY_HISTORY 
ADD CONSTRAINT fk_salary_approver 
FOREIGN KEY (approved_by) REFERENCES EMPLOYEES(emp_id);

-- Add foreign key constraint for attendance
ALTER TABLE ATTENDANCE 
ADD CONSTRAINT fk_attendance_emp 
FOREIGN KEY (emp_id) REFERENCES EMPLOYEES(emp_id) ON DELETE CASCADE;

-- Show all constraints for verification
SELECT 
    TABLE_NAME,
    CONSTRAINT_NAME,
    CONSTRAINT_TYPE,
    REFERENCED_TABLE_NAME
FROM information_schema.TABLE_CONSTRAINTS 
WHERE TABLE_SCHEMA = 'employee_org'
ORDER BY TABLE_NAME, CONSTRAINT_TYPE;
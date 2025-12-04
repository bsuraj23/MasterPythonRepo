-- Create EMPLOYEES table
-- Central table containing all employee information

CREATE TABLE EMPLOYEES (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    hire_date DATE NOT NULL,
    job_title VARCHAR(100) NOT NULL,
    dept_id INT,
    manager_id INT,
    salary DECIMAL(10,2) NOT NULL,
    status ENUM('Active', 'Inactive', 'On Leave') DEFAULT 'Active',
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    -- Check constraints
    CONSTRAINT chk_emp_salary CHECK (salary > 0)
);

-- Create indexes for better performance
CREATE INDEX idx_emp_name ON EMPLOYEES(last_name, first_name);
CREATE INDEX idx_emp_dept ON EMPLOYEES(dept_id);
CREATE INDEX idx_emp_manager ON EMPLOYEES(manager_id);
CREATE INDEX idx_emp_email ON EMPLOYEES(email);

-- Show table structure
DESCRIBE EMPLOYEES;
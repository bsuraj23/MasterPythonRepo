-- Create DEPARTMENTS table
-- This is the parent table for employee organization structure

CREATE TABLE DEPARTMENTS (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL UNIQUE,
    location VARCHAR(100),
    budget DECIMAL(15,2) DEFAULT 0,
    manager_id INT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Add constraint for budget (must be positive)
    CONSTRAINT chk_dept_budget CHECK (budget >= 0)
);

-- Add index on department name for faster searches
CREATE INDEX idx_dept_name ON DEPARTMENTS(dept_name);

-- Show table structure
DESCRIBE DEPARTMENTS;
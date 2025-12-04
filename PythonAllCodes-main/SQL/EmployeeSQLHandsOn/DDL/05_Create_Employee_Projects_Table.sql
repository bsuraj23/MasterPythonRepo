-- Create EMPLOYEE_PROJECTS table
-- Many-to-many relationship between employees and projects

CREATE TABLE EMPLOYEE_PROJECTS (
    emp_id INT NOT NULL,
    project_id INT NOT NULL,
    role VARCHAR(100) DEFAULT 'Team Member',
    hours_allocated INT DEFAULT 40,
    start_date DATE NOT NULL,
    end_date DATE,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Composite primary key
    PRIMARY KEY (emp_id, project_id),
    
    -- Check constraints
    CONSTRAINT chk_emp_proj_hours CHECK (hours_allocated > 0 AND hours_allocated <= 168),
    CONSTRAINT chk_emp_proj_dates CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Create indexes
CREATE INDEX idx_emp_proj_emp ON EMPLOYEE_PROJECTS(emp_id);
CREATE INDEX idx_emp_proj_project ON EMPLOYEE_PROJECTS(project_id);
CREATE INDEX idx_emp_proj_role ON EMPLOYEE_PROJECTS(role);

-- Show table structure
DESCRIBE EMPLOYEE_PROJECTS;
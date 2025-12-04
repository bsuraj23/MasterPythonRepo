-- Create SALARY_HISTORY table
-- Tracks salary changes over time

CREATE TABLE SALARY_HISTORY (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT NOT NULL,
    old_salary DECIMAL(10,2),
    new_salary DECIMAL(10,2) NOT NULL,
    change_date DATE NOT NULL,
    reason VARCHAR(200),
    approved_by INT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Check constraints
    CONSTRAINT chk_salary_positive CHECK (new_salary > 0),
    CONSTRAINT chk_salary_old_positive CHECK (old_salary IS NULL OR old_salary > 0)
);

-- Create indexes
CREATE INDEX idx_salary_emp ON SALARY_HISTORY(emp_id);
CREATE INDEX idx_salary_date ON SALARY_HISTORY(change_date);

-- Show table structure
DESCRIBE SALARY_HISTORY;
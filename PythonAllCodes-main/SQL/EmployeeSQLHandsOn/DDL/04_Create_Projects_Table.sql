-- Create PROJECTS table
-- Stores information about company projects

CREATE TABLE PROJECTS (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    budget DECIMAL(15,2) DEFAULT 0,
    status ENUM('Planning', 'In Progress', 'Completed', 'On Hold', 'Cancelled') DEFAULT 'Planning',
    dept_id INT NOT NULL,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Check constraints
    CONSTRAINT chk_project_budget CHECK (budget >= 0),
    CONSTRAINT chk_project_dates CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Create indexes
CREATE INDEX idx_project_name ON PROJECTS(project_name);
CREATE INDEX idx_project_dept ON PROJECTS(dept_id);
CREATE INDEX idx_project_status ON PROJECTS(status);
CREATE INDEX idx_project_dates ON PROJECTS(start_date, end_date);

-- Show table structure
DESCRIBE PROJECTS;
-- Insert Sample Data into PROJECTS table

USE employee_org;

INSERT INTO PROJECTS (project_name, description, start_date, end_date, budget, status, dept_id) VALUES
-- IT Projects
('Website Redesign', 'Complete overhaul of company website with modern design and functionality', '2023-01-15', '2023-06-30', 150000.00, 'Completed', 2),
('Mobile App Development', 'Develop mobile application for customer engagement', '2023-07-01', '2024-02-28', 200000.00, 'In Progress', 2),
('Database Migration', 'Migrate legacy database to cloud infrastructure', '2023-09-01', '2024-01-31', 80000.00, 'In Progress', 2),

-- Marketing Projects
('Brand Awareness Campaign', 'Multi-channel marketing campaign to increase brand recognition', '2023-03-01', '2023-12-31', 120000.00, 'In Progress', 4),
('Social Media Strategy', 'Develop comprehensive social media presence across all platforms', '2023-02-15', '2023-08-15', 50000.00, 'Completed', 4),

-- R&D Projects
('AI Integration Research', 'Research and development of AI solutions for business processes', '2023-01-01', '2024-06-30', 300000.00, 'In Progress', 6),
('Product Innovation Lab', 'Establish innovation lab for new product development', '2023-05-01', '2024-04-30', 250000.00, 'Planning', 6),

-- Operations Projects
('Process Optimization', 'Streamline operational processes to improve efficiency', '2023-04-01', '2023-10-31', 75000.00, 'In Progress', 5),
('Supply Chain Upgrade', 'Modernize supply chain management systems', '2023-06-01', '2024-03-31', 180000.00, 'Planning', 5),

-- Sales Projects
('CRM Implementation', 'Implement new customer relationship management system', '2023-02-01', '2023-09-30', 100000.00, 'Completed', 7),
('Sales Training Program', 'Comprehensive training program for sales team', '2023-08-01', '2023-12-31', 40000.00, 'In Progress', 7),

-- Finance Projects
('Financial Reporting System', 'Upgrade financial reporting and analytics capabilities', '2023-03-15', '2023-11-30', 90000.00, 'In Progress', 3),

-- HR Projects
('Employee Wellness Program', 'Implement comprehensive employee wellness and health program', '2023-01-01', '2023-12-31', 60000.00, 'In Progress', 1),

-- Customer Service Projects
('Customer Portal Development', 'Develop self-service customer portal', '2023-05-15', '2024-01-15', 85000.00, 'In Progress', 8);

-- Show inserted data
SELECT * FROM PROJECTS ORDER BY dept_id, project_id;

-- Show project count by department
SELECT 
    d.dept_name,
    COUNT(p.project_id) AS project_count,
    SUM(p.budget) AS total_budget
FROM DEPARTMENTS d
LEFT JOIN PROJECTS p ON d.dept_id = p.dept_id
GROUP BY d.dept_id, d.dept_name
ORDER BY project_count DESC;
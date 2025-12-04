-- Insert Sample Data into EMPLOYEE_PROJECTS table

USE employee_org;

INSERT INTO EMPLOYEE_PROJECTS (emp_id, project_id, role, hours_allocated, start_date, end_date)
 VALUES
-- Website Redesign Project (project_id = 1)
(1, 1, 'Lead Developer', 40, '2023-01-15', '2023-06-30'),
(4, 1, 'Frontend Developer', 35, '2023-01-15', '2023-06-30'),
(2, 1, 'Project Manager', 20, '2023-01-15', '2023-06-30'),

-- Mobile App Development Project (project_id = 2)
(1, 2, 'Senior Developer', 40, '2023-07-01', null),
(4, 2, 'UI/UX Developer', 40, '2023-07-01', null),
(3, 2, 'Database Specialist', 20, '2023-07-01', null),

-- Database Migration Project (project_id = 3)
(3, 3, 'Lead DBA', 40, '2023-09-01', null),
(5, 3, 'System Analyst', 30, '2023-09-01', null),

-- Brand Awareness Campaign (project_id = 4)
(12, 4, 'Project Manager', 30, '2023-03-01', null),
(13, 4, 'Marketing Specialist', 40, '2023-03-01', null),
(14, 4, 'Social Media Manager', 25, '2023-03-01', null),

-- Social Media Strategy (project_id = 5)
(14, 5, 'Lead Social Media Manager', 40, '2023-02-15', '2023-08-15'),
(13, 5, 'Marketing Support', 20, '2023-02-15', '2023-08-15'),

-- AI Integration Research (project_id = 6)
(20, 6, 'Research Manager', 35, '2023-01-01', null),
(21, 6, 'Research Scientist', 40, '2023-01-01', null),
(1, 6, 'Technical Consultant', 10, '2023-01-01', null),

-- Product Innovation Lab (project_id = 7)
(20, 7, 'Lab Director', 30, '2023-05-01', null),
(21, 7, 'Senior Researcher', 35, '2023-05-01', null),

-- Process Optimization (project_id = 8)
(18, 8, 'Project Manager', 35, '2023-04-01', null),
(19, 8, 'Operations Specialist', 40, '2023-04-01', null),

-- Supply Chain Upgrade (project_id = 9)
(18, 9, 'Project Lead', 25, '2023-06-01', null),
(19, 9, 'Operations Analyst', 30, '2023-06-01', null),

-- CRM Implementation (project_id = 10)
(15, 10, 'Project Sponsor', 15, '2023-02-01', '2023-09-30'),
(16, 10, 'User Liaison', 20, '2023-02-01', '2023-09-30'),
(17, 10, 'User Liaison', 20, '2023-02-01', '2023-09-30'),
(1, 10, 'Technical Lead', 25, '2023-02-01', '2023-09-30'),

-- Sales Training Program (project_id = 11)
(15, 11, 'Program Manager', 20, '2023-08-01', null),
(6, 11, 'Training Coordinator', 15, '2023-08-01', null),

-- Financial Reporting System (project_id = 12)
(9, 12, 'Project Manager', 25, '2023-03-15', null),
(10, 12, 'Financial Analyst', 30, '2023-03-15', null),
(11, 12, 'Financial Analyst', 25, '2023-03-15', null),

-- Employee Wellness Program (project_id = 13)
(6, 13, 'Program Manager', 30, '2023-01-01', null),
(7, 13, 'HR Specialist', 25, '2023-01-01', null),

-- Customer Portal Development (project_id = 14)
(22, 14, 'Project Sponsor', 15, '2023-05-15', null),
(4, 14, 'Lead Developer', 35, '2023-05-15', null),
(23, 14, 'User Experience Advisor', 20, '2023-05-15', null);

-- Show project assignments
SELECT 
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    p.project_name,
    ep.role,
    ep.hours_allocated,
    ep.start_date,
    ep.end_date
FROM EMPLOYEE_PROJECTS ep
JOIN EMPLOYEES e ON ep.emp_id = e.emp_id
JOIN PROJECTS p ON ep.project_id = p.project_id
ORDER BY p.project_name, ep.role;
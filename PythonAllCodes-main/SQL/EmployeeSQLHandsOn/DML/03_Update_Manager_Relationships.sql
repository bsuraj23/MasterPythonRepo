-- Update Manager Relationships
-- Run this after all employees are inserted

USE employee_org;

-- Update department managers
UPDATE DEPARTMENTS SET manager_id = 6 WHERE dept_id = 1;  -- Emily Taylor (HR)
UPDATE DEPARTMENTS SET manager_id = 2 WHERE dept_id = 2;  -- Sarah Johnson (IT)
UPDATE DEPARTMENTS SET manager_id = 9 WHERE dept_id = 3;  -- Michael Jackson (Finance)
UPDATE DEPARTMENTS SET manager_id = 12 WHERE dept_id = 4; -- Jessica Martin (Marketing)
UPDATE DEPARTMENTS SET manager_id = 18 WHERE dept_id = 5; -- Rachel Rodriguez (Operations)
UPDATE DEPARTMENTS SET manager_id = 20 WHERE dept_id = 6; -- Stephanie Lee (R&D)
UPDATE DEPARTMENTS SET manager_id = 15 WHERE dept_id = 7; -- Daniel Martinez (Sales)
UPDATE DEPARTMENTS SET manager_id = 22 WHERE dept_id = 8; -- Nicole Hall (Customer Service)

-- Update employee managers (reporting structure)
-- IT Department
UPDATE EMPLOYEES SET manager_id = 2 WHERE emp_id IN (1, 3, 4, 5); -- Sarah Johnson manages IT team

-- HR Department  
UPDATE EMPLOYEES SET manager_id = 6 WHERE emp_id IN (7, 8); -- Emily Taylor manages HR team

-- Finance Department
UPDATE EMPLOYEES SET manager_id = 9 WHERE emp_id IN (10, 11); -- Michael Jackson manages Finance team

-- Marketing Department
UPDATE EMPLOYEES SET manager_id = 12 WHERE emp_id IN (13, 14); -- Jessica Martin manages Marketing team

-- Sales Department
UPDATE EMPLOYEES SET manager_id = 15 WHERE emp_id IN (16, 17); -- Daniel Martinez manages Sales team

-- Operations Department
UPDATE EMPLOYEES SET manager_id = 18 WHERE emp_id IN (19); -- Rachel Rodriguez manages Operations team

-- R&D Department
UPDATE EMPLOYEES SET manager_id = 20 WHERE emp_id IN (21); -- Stephanie Lee manages R&D team

-- Customer Service Department
UPDATE EMPLOYEES SET manager_id = 22 WHERE emp_id IN (23); -- Nicole Hall manages Customer Service team

-- Verify the updates
SELECT 
    d.dept_name,
    CONCAT(m.first_name, ' ', m.last_name) AS department_manager
FROM DEPARTMENTS d
JOIN EMPLOYEES m ON d.manager_id = m.emp_id
ORDER BY d.dept_id;
-- Insert Sample Data into SALARY_HISTORY table

USE employee_org;

INSERT INTO SALARY_HISTORY (emp_id, old_salary, new_salary, change_date, reason, approved_by) VALUES
-- Recent salary increases for 2023
(1, 90000.00, 95000.00, '2023-01-15', 'Annual Performance Review - Exceeds Expectations', 2),
(4, 70000.00, 75000.00, '2023-02-01', 'Promotion to Senior Web Developer', 2),
(7, 55000.00, 60000.00, '2023-03-15', 'Annual Salary Adjustment', 6),
(10, 65000.00, 70000.00, '2023-01-01', 'Annual Performance Review - Meets Expectations', 9),
(13, 55000.00, 60000.00, '2023-04-01', 'Market Rate Adjustment', 12),
(16, 50000.00, 55000.00, '2023-02-15', 'Performance-based Increase', 15),
(19, 58000.00, 62000.00, '2023-05-01', 'Expanded Responsibilities', 18),
(21, 85000.00, 90000.00, '2023-03-01', 'Research Excellence Bonus', 20),

-- Historical salary changes for 2022
(2, 110000.00, 120000.00, '2022-12-01', 'Promotion to IT Manager', 6),
(9, 100000.00, 110000.00, '2022-11-15', 'Promotion to Finance Manager', 6),
(12, 85000.00, 95000.00, '2022-10-01', 'Promotion to Marketing Manager', 6),
(15, 90000.00, 100000.00, '2022-09-01', 'Promotion to Sales Manager', 6),
(18, 80000.00, 88000.00, '2022-08-15', 'Promotion to Operations Manager', 6),
(20, 95000.00, 105000.00, '2022-07-01', 'Promotion to Research Manager', 6),
(22, 60000.00, 65000.00, '2022-12-10', 'Promotion to Customer Service Manager', 6),

-- Mid-year adjustments for 2022
(3, 80000.00, 85000.00, '2022-06-01', 'Mid-year Performance Review', 2),
(5, 75000.00, 80000.00, '2022-06-15', 'Skills Development Achievement', 2),
(8, 50000.00, 55000.00, '2022-07-20', 'One Year Anniversary Increase', 6),
(11, 60000.00, 65000.00, '2022-05-22', 'Certification Completion Bonus', 9),
(14, 53000.00, 58000.00, '2022-02-18', 'Market Rate Adjustment', 12),
(17, 48000.00, 52000.00, '2022-04-14', 'Performance Improvement', 15);

-- Show salary history summary
SELECT 
    e.first_name,
    e.last_name,
    e.salary AS current_salary,
    sh.old_salary,
    sh.new_salary,
    sh.change_date,
    sh.reason,
    ROUND(((sh.new_salary - sh.old_salary) / sh.old_salary) * 100, 2) AS increase_percentage
FROM SALARY_HISTORY sh
JOIN EMPLOYEES e ON sh.emp_id = e.emp_id
ORDER BY sh.change_date DESC;

-- Show total salary increases by year
SELECT 
    YEAR(change_date) AS year,
    COUNT(*) AS total_increases,
    AVG((new_salary - old_salary) / old_salary * 100) AS avg_increase_percentage,
    SUM(new_salary - old_salary) AS total_increase_amount
FROM SALARY_HISTORY
GROUP BY YEAR(change_date)
ORDER BY year DESC;
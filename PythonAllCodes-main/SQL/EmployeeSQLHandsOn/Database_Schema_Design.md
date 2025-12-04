# Employee Organization Database Schema

## Database Overview
This database manages a modern organization with employees, departments, projects, and salary information.

## Tables Structure

### 1. DEPARTMENTS
- dept_id (Primary Key)
- dept_name
- location
- budget
- manager_id (Foreign Key to EMPLOYEES)

### 2. EMPLOYEES  
- emp_id (Primary Key)
- first_name
- last_name
- email
- phone
- hire_date
- job_title
- dept_id (Foreign Key to DEPARTMENTS)
- manager_id (Foreign Key to EMPLOYEES - Self Reference)
- salary
- commission_pct
- status (Active/Inactive)

### 3. PROJECTS
- project_id (Primary Key)
- project_name
- description
- start_date
- end_date
- budget
- status
- dept_id (Foreign Key to DEPARTMENTS)

### 4. EMPLOYEE_PROJECTS (Many-to-Many relationship)
- emp_id (Foreign Key to EMPLOYEES)
- project_id (Foreign Key to PROJECTS)
- role
- hours_allocated
- start_date
- end_date

### 5. SALARY_HISTORY
- history_id (Primary Key)
- emp_id (Foreign Key to EMPLOYEES)
- old_salary
- new_salary
- change_date
- reason

### 6. ATTENDANCE
- attendance_id (Primary Key)
- emp_id (Foreign Key to EMPLOYEES)
- date
- time_in
- time_out
- total_hours
- status

## Learning Objectives
This schema will help beginners learn:
1. Basic DDL operations
2. Data relationships and foreign keys
3. Complex queries with multiple tables
4. Aggregate functions with real business scenarios
5. Advanced SQL concepts like views, indexes, and optimization
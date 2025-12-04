# 🔧 MySQL CHECK Constraint Fix

## Issue Resolved: Error Code 3814

**Problem:** MySQL CHECK constraints cannot use non-deterministic functions like `CURDATE()`, `NOW()`, etc.

**Error Message:** 
```
Error Code: 3814. An expression of a check constraint 'chk_emp_hire_date' contains disallowed function: curdate.
```

## ✅ Files Fixed:

### 1. `DDL/03_Create_Employees_Table.sql`
**Removed:**
```sql
CONSTRAINT chk_emp_hire_date CHECK (hire_date <= CURDATE())
```

### 2. `DDL/06_Create_Salary_History_Table.sql`
**Changed:**
```sql
-- From:
change_date DATE DEFAULT (CURDATE()),

-- To:
change_date DATE NOT NULL,
```

### 3. `MySQL_Workbench_Test_Script.sql`
**Removed both:**
```sql
CONSTRAINT chk_emp_hire_date CHECK (hire_date <= CURDATE())
CONSTRAINT chk_salary_hist_date CHECK (change_date <= CURDATE())
```

## 💡 MySQL CHECK Constraint Rules:

### ✅ Allowed in CHECK constraints:
- Column comparisons: `end_date >= start_date`
- Static values: `salary > 0`
- Mathematical operations: `commission_pct >= 0 AND commission_pct <= 1`
- NULL checks: `old_salary IS NULL OR old_salary > 0`

### ❌ Not allowed in CHECK constraints:
- `CURDATE()`, `NOW()`, `CURRENT_DATE`
- `SYSDATE()`, `CURRENT_TIMESTAMP`
- `RAND()`, `UUID()`
- Subqueries
- User-defined functions

## 🔄 Alternative Solutions:

### For date validation, use application logic or triggers:
```sql
-- Option 1: Application-level validation (recommended)
-- Validate hire_date <= current_date in your application code

-- Option 2: BEFORE INSERT/UPDATE trigger
DELIMITER //
CREATE TRIGGER validate_hire_date 
BEFORE INSERT ON EMPLOYEES 
FOR EACH ROW 
BEGIN 
    IF NEW.hire_date > CURDATE() THEN 
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Hire date cannot be in the future'; 
    END IF; 
END//
DELIMITER ;
```

## ✅ Current Status:
All MySQL compatibility issues resolved. Database now executes without errors in MySQL Workbench.

**Test Command:**
```sql
-- Run this to verify fix
CREATE DATABASE test_employee_org;
USE test_employee_org;
-- Then run any of the corrected DDL files
```
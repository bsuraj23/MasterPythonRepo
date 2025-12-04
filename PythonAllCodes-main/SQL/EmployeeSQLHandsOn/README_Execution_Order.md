# MySQL Workbench Execution Order Guide

## Employee Organization Database - Complete SQL Learning System

This document provides the correct execution order for all SQL files to ensure proper database setup and learning progression in MySQL Workbench.

---

## 🚀 Quick Test (All-in-One)

**For immediate testing, run this single file:**
```
MySQL_Workbench_Test_Script.sql
```
This comprehensive script contains all DDL, DML, and test queries in the correct order.

---

## 📁 Manual Step-by-Step Execution

### Phase 1: Database Setup and DDL (Structure Creation)

**Execute in this exact order:**

1. `DDL/01_Create_Database.sql` - Create database and set character encoding
2. `DDL/02_Create_Departments_Table.sql` - Create departments table (no foreign keys)
3. `DDL/03_Create_Employees_Table.sql` - Create employees table (no foreign keys)
4. `DDL/04_Create_Projects_Table.sql` - Create projects table (no foreign keys)
5. `DDL/05_Create_Employee_Projects_Table.sql` - Create employee-project mapping table (no foreign keys)
6. `DDL/06_Create_Salary_History_Table.sql` - Create salary history table (no foreign keys)
7. `DDL/07_Create_Attendance_Table.sql` - Create attendance table (no foreign keys)

### Phase 2: Data Insertion (DML)

**Execute in this exact order:**

8. `DML/01_Insert_Departments_Data.sql` - Insert sample departments
9. `DML/02_Insert_Employees_Data.sql` - Insert sample employees
10. `DML/03_Update_Manager_Relationships.sql` - Update manager relationships
11. `DML/04_Insert_Projects_Data.sql` - Insert sample projects
12. `DML/05_Insert_Employee_Projects_Data.sql` - Insert employee project assignments
13. `DML/06_Insert_Salary_History_Data.sql` - Insert salary history records

### Phase 3: Add Foreign Key Constraints

**Execute after all data is inserted:**

14. `DDL/08_Add_Foreign_Key_Constraints.sql` - Add all foreign key constraints

### Phase 4: Learning Queries (Practice Files)

**Execute these for learning (can be run in any order):**

#### Basic Queries
- `DML/07_Basic_SELECT_Queries.sql` - Basic SELECT statements
- `DML/08_WHERE_Clause_Filtering.sql` - Filtering with WHERE clause
- `DML/09_Logical_Operators_AND_OR_NOT.sql` - Logical operators
- `DML/10_ORDER_BY_Sorting.sql` - Sorting results

#### Intermediate Queries
- `DML/11_Aggregate_Functions.sql` - COUNT, SUM, AVG, MIN, MAX
- `DML/12_GROUP_BY_Clause.sql` - Grouping data
- `DML/13_HAVING_Clause.sql` - Filtering grouped data

#### Advanced Queries
- `DML/14_INNER_JOIN.sql` - Joining tables with INNER JOIN
- `DML/15_LEFT_JOIN.sql` - Left outer joins

---

## ⚠️ Important MySQL Workbench Setup

### Before Running Scripts:

1. **Open MySQL Workbench**
2. **Connect to your MySQL server**
3. **Create a new SQL tab**
4. **Set SQL Mode (Optional):**
   ```sql
   SET SQL_MODE = 'STRICT_TRANS_TABLES,NO_ZERO_DATE,NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO';
   ```

### Execution Tips:

1. **Run one file at a time** - Don't run multiple files simultaneously
2. **Check for errors** - Review output panel after each execution
3. **Use transactions** - Wrap large data insertions in transactions if needed:
   ```sql
   START TRANSACTION;
   -- Your SQL statements here
   COMMIT;
   ```

---

## 🔍 Verification Queries

After completing all phases, run these verification queries:

```sql
-- 1. Verify all tables exist
SHOW TABLES;

-- 2. Check record counts
SELECT 'DEPARTMENTS' AS table_name, COUNT(*) AS records FROM DEPARTMENTS
UNION ALL
SELECT 'EMPLOYEES', COUNT(*) FROM EMPLOYEES
UNION ALL
SELECT 'PROJECTS', COUNT(*) FROM PROJECTS
UNION ALL
SELECT 'EMPLOYEE_PROJECTS', COUNT(*) FROM EMPLOYEE_PROJECTS
UNION ALL
SELECT 'SALARY_HISTORY', COUNT(*) FROM SALARY_HISTORY
UNION ALL
SELECT 'ATTENDANCE', COUNT(*) FROM ATTENDANCE;

-- 3. Test a complex join
SELECT 
    e.first_name,
    e.last_name,
    d.dept_name,
    e.job_title,
    e.salary
FROM EMPLOYEES e
INNER JOIN DEPARTMENTS d ON e.dept_id = d.dept_id
ORDER BY d.dept_name, e.salary DESC
LIMIT 10;

-- 4. Verify foreign key constraints
SELECT 
    TABLE_NAME,
    CONSTRAINT_NAME,
    CONSTRAINT_TYPE,
    REFERENCED_TABLE_NAME
FROM information_schema.TABLE_CONSTRAINTS 
WHERE TABLE_SCHEMA = 'employee_org'
AND CONSTRAINT_TYPE = 'FOREIGN KEY'
ORDER BY TABLE_NAME;
```

---

## 📊 Expected Results

After successful execution, you should have:

- **Database:** `employee_org` with proper character encoding
- **Tables:** 6 tables with proper relationships
- **Data:** 
  - 8 departments
  - 23 employees
  - 14 projects
  - Multiple project assignments
  - Sample salary history records
- **Constraints:** All foreign key relationships properly established
- **Learning Files:** 15+ query examples for SQL learning

---

## 🛠️ Troubleshooting

### Common Issues:

1. **Foreign Key Constraint Errors:**
   - Ensure Phase 1 and 2 are completed before Phase 3
   - Check that referenced data exists

2. **Duplicate Key Errors:**
   - Drop and recreate database if rerunning scripts
   - Or use the comprehensive test script for clean execution

3. **Syntax Errors:**
   - Ensure you're using MySQL Workbench (not SQL Server)
   - All scripts are MySQL-compatible

### Reset Database:
```sql
DROP DATABASE IF EXISTS employee_org;
-- Then restart from Phase 1
```

---

## 🎯 Learning Objectives

This database system teaches:

- **DDL:** Table creation, constraints, relationships
- **DML:** Data insertion, updates, complex queries
- **Functions:** Aggregate functions, date functions
- **Joins:** INNER JOIN, LEFT JOIN
- **Advanced:** Subqueries, grouping, filtering
- **Best Practices:** Database design, normalization

---

**Status:** ✅ All files tested and verified for MySQL Workbench compatibility
**Last Updated:** Current session
**Total Files:** 20+ SQL files for comprehensive learning
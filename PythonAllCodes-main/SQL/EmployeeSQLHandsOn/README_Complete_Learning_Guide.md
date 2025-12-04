# 🏢 Employee Organization SQL Learning Project

## 📋 Complete MySQL Workbench Compatible Training System

### 🎯 **Project Overview**
This comprehensive SQL training project uses a realistic **Employee Organization Database** to teach complete SQL concepts from beginner to advanced level. All examples work perfectly in **MySQL Workbench**.

---

## 🗄️ **Database Schema**

### **Tables Structure:**
1. **DEPARTMENTS** - Company departments (HR, IT, Finance, etc.)
2. **EMPLOYEES** - Employee information with hierarchy
3. **PROJECTS** - Company projects by department
4. **EMPLOYEE_PROJECTS** - Many-to-many relationship (employees ↔ projects)
5. **SALARY_HISTORY** - Track salary changes over time
6. **ATTENDANCE** - Daily attendance tracking

### **Key Relationships:**
- Employees belong to Departments
- Employees report to Managers (self-reference)
- Projects belong to Departments  
- Employees can work on multiple Projects
- Salary changes are tracked historically

---

## 📚 **Complete Learning Path**

### **🔧 Phase 1: Database Setup (DDL)**
| File | Topic | Description |
|------|-------|-------------|
| `01_Create_Database.sql` | Database Creation | Create employee_org database |
| `02_Create_Departments_Table.sql` | DDL Basics | Create DEPARTMENTS table |
| `03_Create_Employees_Table.sql` | Advanced DDL | Create EMPLOYEES with constraints |
| `04_Create_Projects_Table.sql` | DDL Constraints | Create PROJECTS table |
| `05_Create_Employee_Projects_Table.sql` | Many-to-Many | Junction table creation |
| `06_Create_Salary_History_Table.sql` | DDL Complete | Historical data table |
| `07_Create_Attendance_Table.sql` | DDL Advanced | Attendance tracking |
| `08_Add_Foreign_Key_Constraints.sql` | Relationships | Foreign key management |

### **📊 Phase 2: Basic Data Operations (DML)**
| File | Topic | Description |
|------|-------|-------------|
| `01_Insert_Departments_Data.sql` | INSERT Basics | Add department data |
| `02_Insert_Employees_Data.sql` | INSERT Advanced | Add employee records |
| `03_Update_Manager_Relationships.sql` | UPDATE Operations | Set manager hierarchy |
| `04_Insert_Projects_Data.sql` | INSERT Complex | Project data entry |
| `05_Insert_Employee_Projects_Data.sql` | Many-to-Many Data | Project assignments |
| `06_Insert_Salary_History_Data.sql` | Historical Data | Salary change tracking |

### **🔍 Phase 3: Basic Queries**
| File | Topic | Description |
|------|-------|-------------|
| `07_Basic_SELECT_Queries.sql` | SELECT Fundamentals | Basic data retrieval |
| `08_WHERE_Clause_Filtering.sql` | Data Filtering | WHERE conditions |
| `09_Logical_Operators_AND_OR_NOT.sql` | Logic Operations | Complex filtering |
| `10_ORDER_BY_Sorting.sql` | Data Sorting | Result ordering |

### **📈 Phase 4: Aggregate Functions**
| File | Topic | Description |
|------|-------|-------------|
| `11_Aggregate_Functions.sql` | COUNT, SUM, AVG, MIN, MAX | Statistical operations |
| `12_GROUP_BY_Clause.sql` | Data Grouping | Group-based analysis |
| `13_HAVING_Clause.sql` | Group Filtering | Filter grouped results |

### **🔗 Phase 5: Table Relationships (JOINs)**
| File | Topic | Description |
|------|-------|-------------|
| `14_INNER_JOIN.sql` | INNER JOIN | Matching records only |
| `15_LEFT_JOIN.sql` | LEFT JOIN | All left table records |
| `16_RIGHT_JOIN.sql` | RIGHT JOIN | All right table records |
| `17_FULL_OUTER_JOIN.sql` | FULL OUTER JOIN | All records from both tables |
| `18_SELF_JOIN.sql` | SELF JOIN | Table joined with itself |
| `19_CROSS_JOIN.sql` | CROSS JOIN | Cartesian product |

### **🎯 Phase 6: Advanced Queries**
| File | Topic | Description |
|------|-------|-------------|
| `20_Scalar_Subqueries.sql` | Subqueries | Single value subqueries |
| `21_Column_Subqueries.sql` | IN/EXISTS | Multiple value subqueries |
| `22_Table_Subqueries.sql` | FROM Subqueries | Subqueries as tables |
| `23_Correlated_Subqueries.sql` | Correlated | Dependent subqueries |

### **⚡ Phase 7: Functions & Optimization**
| File | Topic | Description |
|------|-------|-------------|
| `24_String_Functions.sql` | Text Processing | CONCAT, LENGTH, SUBSTRING |
| `25_Date_Functions.sql` | Date Operations | DATE_ADD, DATEDIFF, FORMAT |
| `26_Numeric_Functions.sql` | Math Operations | ROUND, CEILING, POWER |
| `27_Conditional_Functions.sql` | Logic Functions | CASE, IF, COALESCE |
| `28_Views_Management.sql` | Database Views | CREATE, ALTER, DROP |
| `29_Index_Optimization.sql` | Performance | CREATE INDEX, optimization |

---

## 🎓 **Learning Objectives by Phase**

### **Beginner Level (Files 1-10)**
- ✅ Create and manage database structure
- ✅ Insert, update, and delete data
- ✅ Write basic SELECT queries
- ✅ Filter data with WHERE clause
- ✅ Sort results with ORDER BY

### **Intermediate Level (Files 11-19)**
- ✅ Use aggregate functions for analysis
- ✅ Group data for business insights
- ✅ Join multiple tables effectively
- ✅ Understand different JOIN types
- ✅ Analyze related data across tables

### **Advanced Level (Files 20-29)**
- ✅ Write complex subqueries
- ✅ Use advanced SQL functions
- ✅ Create and manage views
- ✅ Optimize query performance
- ✅ Handle real-world business scenarios

---

## 💼 **Real-World Business Scenarios**

### **HR Analytics:**
- Employee count by department
- Salary analysis and comparisons
- Manager-subordinate relationships
- Hiring trends over time

### **Project Management:**
- Project resource allocation
- Team workload analysis
- Budget vs actual spending
- Project status tracking

### **Financial Analysis:**
- Salary cost by department
- Budget utilization reports
- Salary history and trends
- Commission calculations

### **Performance Metrics:**
- Employee productivity analysis
- Department efficiency metrics
- Project success rates
- Resource optimization

---

## 🚀 **Getting Started**

### **Prerequisites:**
- MySQL Workbench installed
- Basic understanding of databases
- Willingness to learn!

### **Setup Instructions:**
1. **Open MySQL Workbench**
2. **Run DDL files (01-08)** to create database structure
3. **Run DML files (01-06)** to insert sample data
4. **Practice with query files (07-29)** in order
5. **Experiment with your own variations**

### **Sample Business Questions to Practice:**
1. Which department has the highest average salary?
2. How many employees are working on each project?
3. Who are the employees that haven't received any salary increase?
4. What's the total budget allocation across all departments?
5. Which projects are over-allocated with resources?

---

## 📊 **Sample Data Overview**

- **8 Departments** across different functions
- **23 Employees** with realistic job titles and salaries
- **14 Projects** in various stages
- **25+ Project assignments** showing resource allocation
- **20+ Salary changes** showing career progression
- **Manager hierarchy** showing organizational structure

---

## 🎯 **Learning Outcomes**

After completing this project, you will:
- ✅ Master all SQL fundamentals and advanced concepts
- ✅ Understand real-world database design principles
- ✅ Write efficient queries for business analysis
- ✅ Handle complex data relationships
- ✅ Optimize database performance
- ✅ Be ready for professional SQL work!

---

## 🏆 **Next Steps**

1. Complete all exercises in order
2. Try modifying queries to answer new questions
3. Add your own data and scenarios
4. Practice with larger datasets
5. Learn about database administration
6. Explore advanced MySQL features

**Happy Learning! 🎉**
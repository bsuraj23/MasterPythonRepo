# University MySQL Project

This project is designed to manage a university database schema using MySQL. It includes SQL scripts for creating tables, defining the schema, and inserting data related to students, courses, and enrollments.

## Project Structure

- **DLD**: Contains Data Definition Language (DDL) scripts.
  - `create_tables.sql`: SQL statements to create the necessary tables for the university schema.
  - `schema.sql`: SQL commands to define the schema of the database, including constraints, indexes, and relationships between tables.

- **DML**: Contains Data Manipulation Language (DML) scripts.
  - `insert_students.sql`: SQL insert statements to add student records into the Students table.
  - `insert_courses.sql`: SQL insert statements to add course records into the Courses table.
  - `insert_enrollments.sql`: SQL insert statements to add enrollment records into the Enrollments table.

## Setup Instructions

1. **Create the Database**: 
   - Use the following command to create a new database:
     ```sql
     CREATE DATABASE university;
     ```

2. **Run DDL Scripts**:
   - Execute the `create_tables.sql` script to create the necessary tables:
     ```sql
     SOURCE path/to/DLD/create_tables.sql;
     ```
   - Execute the `schema.sql` script to define the schema:
     ```sql
     SOURCE path/to/DLD/schema.sql;
     ```

3. **Insert Data**:
   - Populate the Students table by running:
     ```sql
     SOURCE path/to/DML/insert_students.sql;
     ```
   - Populate the Courses table by running:
     ```sql
     SOURCE path/to/DML/insert_courses.sql;
     ```
   - Populate the Enrollments table by running:
     ```sql
     SOURCE path/to/DML/insert_enrollments.sql;
     ```

## Additional Information

- Ensure you have MySQL installed and running on your machine.
- Modify the paths in the `SOURCE` commands as necessary to match your directory structure.
- This project can be expanded with additional features such as querying capabilities, reporting, and more.
-- Notable keywords to remember
SELECT column_name -- Indicates which fields to be selected
FROM table_name -- which table to select the columns from

-- Sample query code
SELECT name, student_number -- replace columns with * to select all immediately
FROM graduation_data; -- make sure to end the query with a semicolon

-- Aliasing
SELECT name AS first_name, year_graduated
FROM graduation_data;

-- Selecting values with no repeat values
SELECT DISTINCT year_graduated
FROM graduation_data;

-- Creating views (simular to subsets in python)
CREATE VIEW graduation_student_data AS
SELECT student_id, name, year_graduated
FROM graduation_data;

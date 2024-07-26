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

-- counting number of records (similar to value_counts in Python)
SELECT COUNT(graduation_date) AS count_graduation_date
FROM graduation_data;
SELECT COUNT(*) AS total_records
from graduation_data;

-- counting unique values in a database
SELECT COUNT(DISTINCT graduation_date) AS distinct_graduation
FROM graduation_data;

-- Filtering
SELECT student_name
FROM graduation_data WHERE graduation_date => 2010;

-- Filtering with multiple criterias
SELECT * FROM graduaton_data
WHERE school = 'TIP_QC' OR school = 'TIP_MNL';
WHERE school = 'TIP_QC' AND graduation_date = 2010;
WHERE graduation_date BETWEEN 2010 AND 2015

-- multiple filtering conditions (selects students who graduation in 2010 and 2015 with the specific course)
WHERE (graduation_date = 2010 OR graduation_date = 2015)
AND (student_course = 'CpE' OR student_course = 'CE');

-- multiple filtering conditions (specified range)
WHERE graduation_date BETWEEN 2010 AND 2015

-- multiple filtering conditions 
WHERE graduation_data BETWEEN 2010 AND 2015 AND student_course = 'CpE';

-- Filtering text (Will select names starting with Ch)
SELECT name FROM graduation_data
WHERE name LIKE 'Ch%'; 

-- Filtering text (will only match three letter names starting from Ev)
WHERE name LIKE 'Ev_' ;

-- Filtering text (will not select names starting with A)
WHERE name NOT LIKE 'A%';

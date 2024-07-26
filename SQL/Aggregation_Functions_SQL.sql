-- Summarizing data Different functions include SUM(), MIN(), MAX(), and COUNT()
SELECT AVG(student_grade)
FROM graduation_data

-- Summarizing data with the WHERE and ROUND parameter, the number denotes the decimal places
SELECT ROUND(AVG(student_grade), 2) AS average_student_grade
FROM graduation_data 
WHERE graduation_date >= 2015;

-- Arithmetic aggregation
SELECT (gross - budget) AS total_profit
FROM business_data;

SELECT MAX(budget), MAX(gross)
FROM business_data;

-- Sample query application (arithmetic)
SELECT COUNT(graduation_date) * 1000.0 / COUNT(*)
AS percentage_graduated FROM graduation_data;

-- Sorting queries
SELECT name, average_grade FROM graduation_data
ORDER BY average_grade ASC;

-- Sample query application (sorting)
SELECT name, average_grade, graduation_date FROM graduation_data
WHERE average_grade IS NOT NULL 
ORDER BY average_grade DESC, graduation_date DESC;

-- Grouping data
SELECT student_course, COUNT(graduation_date) AS count_course_graduated
FROM graduation_data GROUP BY student_course;

-- Sample query application (grouped data)
SELECT student_course COUNT(graduation_date) AS count_course_graduation
FROM graduation_data GROUP BY student_course
ORDER BY count_course_graduated DESC;

-- Filtering grouped data
SELECT graduation_date, COUNT(student_course) AS graduated_per_course
FROM graduation_data GROUP BY graduation_date
HAVING COUNT(name) > 500 -- shows the year where there are more than 500 graduates

-- Sample query application (prints only the values where the average grade is more than 90% from different courses)
SELECT name, ROUND(AVG(student_grade), 2) AS average_student_grade 
FROM graduation_data GROUP BY student_course 
HAVING AVG(student_grade) > 90 ORDER BY average_student_grade DESC;

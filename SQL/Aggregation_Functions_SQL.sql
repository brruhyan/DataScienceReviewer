-- Summarizing data Different functions include SUM(), MIN(), MAX(), and COUNT()
SELECT AVG(student_grade)
FROM graduation_data

-- Summarizing data with the WHERE and ROUND parameter, the number denotes the decimal places
SELECT ROUND(AVG(student_grade), 2) AS average_student_grade
FROM graduation_data 
WHERE graduation_date >= 2015;

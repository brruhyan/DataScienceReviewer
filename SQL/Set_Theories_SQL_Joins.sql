-- Union joining
SELECT * FROM left_table
UNION SELECT * FROM right_table;

-- Union aLL joining
SELECT * FROM left_table
UNION ALL SELECT * FROM right_table;

-- sample union join query
SELECT monarch AS leader, country
FROM monarchs
UNION SELECT prime_minister, country
FROM prime_ministers 
ORDER BY country, leader LIMIT 10;

-- intersect joining
SELECT id, val 
FROM left_table
  INTERSECT
SELECT id,val 
FROM right_table;

-- Except joining (only returns records from the left table that are not present in the right table)
SELECT monarch, country
FROM monarchs
  EXCEPT
SELECT prime_minister, country 
FROM prime_ministers;

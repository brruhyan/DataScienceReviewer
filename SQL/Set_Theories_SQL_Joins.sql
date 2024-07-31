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

-- Additive joins
-- Semi joining (chooses records in the first table where a condition is met in the second table)
SELECT country FROM states
WHERE indep_year < 1800;

-- sample query (semi join)
SELECT president, country, continent FROM presidents
WHERE country IN
    (SELECT country FROM states 
      WHERE indep_year < 1800);

--sample query 2 (semi join, basically what it does it merges two subtables into one)
SELECT DISTINCT name FROM languages -- selecting only distinct names in the languages table
  WHERE code IN -- selecting only the code where the country is equal to middle east
    (SELECT code FROM countries 
      WHERE region = 'Middle East');

-- anti joins
SELECT country, president FROM presidents
WHERE continent LIKE '%America'  
  AND country NOT IN
    (SELECT country FROM states
     WHERE indep_year < 1800);


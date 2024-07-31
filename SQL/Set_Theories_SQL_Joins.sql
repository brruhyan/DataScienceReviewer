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
-- same as semi join but it includes records that are not equal to the condition
SELECT country, president FROM presidents
WHERE continent LIKE '%America'  
  AND country NOT IN
    (SELECT country FROM states
     WHERE indep_year < 1800);

-- subquery within the WHERE clause
WHERE DISTINCT continent, -- makes sure that no repeat continents are included
  (SELECT COUNT(*) FROM monarchs  -- will count the number of monarchs within each continent
      WHERE states.continent = monarch.continent) AS monarch_count --merges both into one column and outputs if there is a monarch.
FROM states;

-- sample query (subquery within WHERE)
SELECT * FROM populations -- selects all values in the table
  WHERE life_expectancy > 1.15 * -- gets the records where life_expectancy is times 1.15 than the average
    (SELECT AVG(life_expectancy) FROM populations
      WHERE year = 2015) AND year = 2015;

-- sample query 2 
SELECT name, country_code, urbanarea_pop FROM cities
  WHERE name IN 
    (SELECT capital FROM countries) 
ORDER BY urbanarea_pop DESC;

-- Subqueries within FROM
SELECT DISTINCT monarchs.continent, sub.most_recent
FROM monarchs,
  (SELECT continent, MAX(indep_year) AS most_recent
    FROM states GROUP BY continent) AS sub
WHERE monarchs.continent = sub.continent

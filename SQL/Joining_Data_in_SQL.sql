-- Inner join query (looks for records in both tables which have common values in the given field and compiles them in one table)
-- records that dont have a match will be discarded/omitted

SELECT prime_ministers.country, prime_ministers.continent, prime_minister, president -- select the fields you want included in the final table
FROM prime_ministers AS left_table-- left table
INNER JOIN presidents AS right_table -- right table (table to join the values to the left)
ON left_table.country = right_table.country; -- values in each table to match (make sure they have common values)

-- sample query application (inner join)
SELECT cities.name AS city, countries.name AS country, region
FROM cities
INNER JOIN countries ON cities.country_code = countries.code; 

-- sample query (inner join 2)
SELECT c.code AS country_code, name, year, inflation_rate
FROM countries AS c
INNER JOIN economies as e ON c.code = e.code;

-- In normal cases put select first 
SELECT c.name AS country, l.name AS language, official -- select which to show in the merged table
FROM countries AS c -- select the left table
INNER JOIN languages AS l -- select the right table
USING(name); -- select which common column to merge with

-- Multiple joins
-- Joins on joins
SELECT * -- selecting all columns
FROM left_table -- selecting the main table
INNER JOIN right_table ON left_table.id = right_table.id -- selecting the right table and performing join on id
INNER JOIN another_table ON left_table.id = another_table.id; -- joining another table to the results of the initial join

-- sample query (multiple join)
-- put select first
SELECT p1.country, p1.continent, p2.president, p1.prime_minister
FROM prime_minister AS p1
INNER JOIN presidents AS p2 USING(country)
INNER JOIN prime_minister_terms AS p3 USING(prime_minister);

-- sample query 2 (multiple join)
SELECT *
FROM left_table 
INNER JOIN right_table ON left_table.id = right_table.id AND left_table.date = right_table.date;

-- left join 
-- all values are merged but those without matching will be specified as NULL;
SELECT p1.country, p1.prime_minister, p2.president 
FROM prime_minister AS p1
LEFT JOIN presidents AS p2 USING(country); -- to convert this to right join change LEFT to right and opposite p1 and p2

-- sample query (left join)
SELECT c1.name AS city, c2.code, c2.name AS country, c2.region, c1.city_proper
FROM cities AS c1
LEFT JOIN countries AS c2 ON c1.country_code = c2.code
ORDER BY c2.code DESC;

-- sample left query 
SELECT c.name AS country, region, life_expectancy AS life_exp
FROM countries as c LEFT JOIN population as p
ON c.code = p.country_code WHERE year = 2010
ORDER BY life_exp LIMIT 5;

-- full join
-- all data will be joined regardless of repetition 
SELECT p1.country AS country, p1.prime_minister, p2.president
FROM prime_ministers AS p1
FULL JOIN presidents AS p2 ON p1.country = p2.country
LIMIT 10;

-- sample query (full join)
SELECT name AS country, code, region, basic_unit
FROM countries 
FULL JOIN currencies USING (code)
WHERE region = 'North America' OR name IS NULL
ORDER BY region;

-- cross joins
-- all possible combinations of both tables will be the output
SELECT p1.prime_minister, p2.president
FROM prime_ministers AS p1
CROSS JOIN presidents AS p2
WHERE p1.continent IN ('Asia')
  AND p2.continent IN ('South America');

-- self joins
SELECT 
    p1.country AS country_1
    p2.country AS country_2
    p1.continent 
FROM prime_ministers as p1
INNER JOIN prime_ministers AS p2
ON p1.continent = p2.continent   
  AND p1.country <> p2.country;

-- sample self join 
SELECT 
    p1.country_code
    p1.size AS size2010
    p2.size AS size2015
FROM populations AS p1
INNER JOIN population AS p2
USING(country_code) WHERE p1.year = 2010
  AND p1.year = p2.year - 5;

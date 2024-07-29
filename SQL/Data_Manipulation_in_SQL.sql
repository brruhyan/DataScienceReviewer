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

-- sample query (step by step)
FROM countries AS c -- select the left table
INNER JOIN languages AS l -- select the right table
SELECT c.name AS country, l.name AS language, official -- select which to show in the merged table
USING(name); -- select which common column to merge with

-- Multiple joins
-- Joins on joins
FROM left_table -- selecting the main table
INNER JOIN right_table -- selecting the right table
SELECT * ON left_table.id = right_table.id -- selecting all columns and then performing join on id
INNER JOIN another_table -- creating another table 
ON left_table_id = another_table.id -- joining another table to the results of the initial join

-- sample query (multiple join)
FROM prime_minister AS p1
INNER JOIN presidents as p2
SELECT p1.country, p1.continent, president, prime_minister
USING(country)
INNER JOIN prime_mister_terms AS p3
USING(prime_minister);

-- sample query 2 (multiple join)
FROM left_table INNER join right_table
SELECT * ON left_table.id = right_table.id
AND left_table.date = right_table.date; 

-- left join 
-- all values are merged but those without matching will be specified as NULL;
FROM prime_minister AS p1
LEFT JOIN presidents as p2
SELECT p1.country, prime_minister, president 
USING(country);

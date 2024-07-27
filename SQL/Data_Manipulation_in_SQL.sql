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

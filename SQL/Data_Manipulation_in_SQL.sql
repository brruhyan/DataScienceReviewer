-- Inner join query (looks for records in both tables which have common values in the given field and compiles them in one table)
-- records that dont have a match will be discarded/omitted

SELECT prime_ministers.country, prime_ministers.continent, prime_minister, president -- select the fields you want included in the final table
FROM prime_ministers -- left table
INNER JOIN presidents -- right table (table to join the values to the left)
ON prime_ministers.country = president.country; -- values in each table to match (make sure they have common values)


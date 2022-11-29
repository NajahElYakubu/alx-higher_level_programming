-- lists all records with a score>= 10 from the table second_table
-- diplay both the score then name
-- records should be oredered by name
SELECT `score`, `name`
FROM second_table
WHERE `score` >= 10
ORDER BY `score` DESC;

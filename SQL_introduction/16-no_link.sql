-- lists all records of the table second_table of the database hbtn_0c_0
-- don't list rows without a name value
-- results should display score and name (in this order)
-- records should be listed by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name <> '' ORDER BY score DESC;

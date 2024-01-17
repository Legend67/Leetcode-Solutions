# Write your MySQL query statement below
DELETE e 
FROM person e
INNER JOIN person e2 ON e.email = e2.email
WHERE e.id > e2.id;
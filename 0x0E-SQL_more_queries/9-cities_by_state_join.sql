-- join tables
SELECT C.id, C.name, S.name
FROM cities C INNER JOIN states S ON C.state_id = S.id
order by C.id

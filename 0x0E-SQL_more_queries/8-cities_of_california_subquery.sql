-- cities of calefornaia
SELECT id, name 
FROM cities AS C
WHERE C.state_id = (
	SELECT id
	FROM states AS S
	WHERE S.name = 'California')
ORDER BY C.id

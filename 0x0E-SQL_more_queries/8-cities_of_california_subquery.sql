-- cities of calefornaia
SELECT id, name 
FROM cities C
WHERE C.state_id = (
	SELECT id
	FROM states S
	WHERE S.name = 'Calefornia')
ORDER BY C.id

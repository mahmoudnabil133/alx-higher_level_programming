-- top 3 at temp
SELECT city, AVG(value) AS avg_temp
FROM hbtn_0c_0
WHERE month = 'July' or month = 'August'
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

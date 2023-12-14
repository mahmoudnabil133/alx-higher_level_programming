-- count genres
SELECT GN.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS GN INNER JOIN tv_show_genres AS SHG ON GN.id = SHG.genre_id
GROUP BY(genre)
ORDER BY number_of_shows DESC;

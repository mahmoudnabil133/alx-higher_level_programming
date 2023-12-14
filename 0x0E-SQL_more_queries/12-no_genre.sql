-- left join without intersection
SELECT SH.title, SHG.genre_id
FROM tv_shows AS SH LEFT JOIN tv_show_genres AS SHG ON SH.id = SHG.show_id
WHERE SHG.genre_id IS NULL;
ORDER BY SH.title, SHG.genre_id

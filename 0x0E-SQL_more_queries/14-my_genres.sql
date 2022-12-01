-- Uses a database to list a "value"
SELECT g.name
FROM tv_genres AS g
	INNER JOIN tv_show_genres AS t
	ON g.id = t.genre_id


	INNER JOIN tv_shows as s
	ON s.id = t.show_id
	WHERE s.title = 'Dexter'
ORDER BY g.name;

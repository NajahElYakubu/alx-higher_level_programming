-- Uses a database to list a "value"
SELECT g.name
FROM tv_genres AS g
	INNER JOIN tv_show_genres AS s
	ON g.id = s.genre_id


	INNER JOIN tv_shows as t
	ON t.id = s.show_id
	WHERE s.title = 'Dexter'
ORDER BY g.name;

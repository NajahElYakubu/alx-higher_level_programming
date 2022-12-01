-- lists values with a common link 
SELECT s.title, g.name
FROM tv_shows AS s
	LEFT JOIN tv_show_genres AS t
	ON s.id = t.show_id

	LEFT JOIN tv_genres AS g
	on g.id = t.genre_id
ORDER BY s.title, g.name;

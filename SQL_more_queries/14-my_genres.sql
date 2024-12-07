-- List all genres of the show Dexter.
SELECT tv_genres.name FROM tv_show_genres
	JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
	JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_shows.title = "Dexter"
	ORDER BY name;
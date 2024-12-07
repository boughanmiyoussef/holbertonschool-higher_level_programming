-- List all genres and display the number of shows linked to each.
SELECT tv_genres.name AS genre, COUNT(tv_genres.name) AS number_of_shows
	FROM tv_show_genres
	JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
	JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
	GROUP BY genre
	ORDER BY number_of_shows DESC;
-- SQL task 14
SELECT 
  tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
  ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
  ON tv_shows.id = tv_show_genres.show_id
WHERE 
  EXISTS (
    SELECT 1 
    FROM tv_shows 
    WHERE tv_shows.title = 'DEXTER' AND tv_shows.id = tv_show_genres.show_id
  )
ORDER BY tv_genres.name ASC;

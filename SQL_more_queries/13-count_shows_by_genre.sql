-- SQL task 13
SELECT 
  tv_genres.name AS genre, 
  (SELECT COUNT(*) 
   FROM tv_show_genres 
   WHERE tv_show_genres.genre_id = tv_genres.id) AS number_of_shows
FROM tv_genres
ORDER BY number_of_shows DESC;

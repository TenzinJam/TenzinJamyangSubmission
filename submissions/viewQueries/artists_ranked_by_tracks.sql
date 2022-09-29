-- SQLite

CREATE VIEW artists_ranked_by_tracks 
AS
SELECT ar.artist_id, ar.artist_name, COUNT(t.track_id) number_of_tracks
FROM artist ar
INNER JOIN album al
ON ar.artist_id = al.artist_id
INNER JOIN track t
ON t.album_id = al.album_id
GROUP BY 1
ORDER BY 3 DESC;
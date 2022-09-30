-- SQLite
-- DROP VIEW artists_ranked_by_tracks;

CREATE VIEW artists_ranked_by_tracks 
AS
SELECT ar.artist_id, ar.artist_name, SUM(al.total_tracks) number_of_tracks
FROM artist ar
INNER JOIN album al
ON ar.artist_id = al.artist_id
GROUP BY 1
ORDER BY 3 DESC;
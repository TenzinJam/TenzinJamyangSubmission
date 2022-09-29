-- SQLite
CREATE VIEW artists_ranked_by_albums
AS
SELECT ar.artist_id, ar.artist_name, COUNT(*)
FROM artist ar
JOIN album al 
ON ar.artist_id = al.artist_id
GROUP BY 1
ORDER BY 3 DESC


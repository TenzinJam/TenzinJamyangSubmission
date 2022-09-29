-- SQLite

-- DROP VIEW nonexplicit_songs_by_artists;

CREATE VIEW nonexplicit_songs_by_artists
AS
SELECT ar.artist_id, ar.artist_name, COUNT(t.explicit) non_explicit_count
     FROM artist ar 
     JOIN album al 
     ON ar.artist_id = al.artist_id
     JOIN track t 
     ON al.album_id = t.album_id
     WHERE t.explicit = 0
     GROUP BY 1
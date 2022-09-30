-- SQLite

-- DROP VIEW explicit_nonexplicit;

CREATE VIEW explicit_nonexplicit
AS
SELECT ar.artist_id, ar.artist_name, COUNT(IIF(t.explicit = 1, 1, NULL)) explicit_count, COUNT(IIF(t.explicit = 0, 1, NULL)) non_explicit_count
     FROM artist ar 
     JOIN album al 
     ON ar.artist_id = al.artist_id
     JOIN track t 
     ON al.album_id = t.album_id
     GROUP BY 1
     ORDER BY 2
     
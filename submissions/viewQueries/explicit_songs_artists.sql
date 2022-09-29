-- SQLite

-- DROP VIEW explicit;

-- CREATE VIEW explicit_songs
-- AS
-- SELECT artist_id, artist_name, explicit_count, non_explicit_count
-- FROM (
--     SELECT *
--     FROM 
--     (SELECT ar.artist_id, ar.artist_name, COUNT(t.explicit) explicit_count
--      FROM artist ar 
--      LEFT JOIN album al 
--      ON ar.artist_id = al.artist_id
--      JOIN track t 
--      ON al.album_id = t.album_id
--      WHERE t.explicit = 1
--      GROUP BY 1
--     ) AS table1
--     JOIN
--     (SELECT ar.artist_id, ar.artist_name, COUNT(t.explicit) non_explicit_count
--      FROM artist ar 
--      LEFT JOIN album al 
--      ON ar.artist_id = al.artist_id
--      JOIN track t 
--      ON al.album_id = t.album_id
--      WHERE t.explicit = 0
--      GROUP BY 1
--     ) AS table2
--     ON table1.artist_id = table2.artist_id
-- )

CREATE VIEW explicit_songs_by_artists
AS
SELECT ar.artist_id, ar.artist_name, COUNT(t.explicit) explicit_count
     FROM artist ar 
     JOIN album al 
     ON ar.artist_id = al.artist_id
     JOIN track t 
     ON al.album_id = t.album_id
     WHERE t.explicit = 1
     GROUP BY 1
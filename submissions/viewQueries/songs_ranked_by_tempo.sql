-- SQLite


CREATE VIEW tempo_ranked_by_artists
AS
    SELECT artist_id, artist_name, track_id, song_name, tempo
    FROM (
        SELECT artist_id, artist_name, track_id, song_name, tempo, 
                ROW_NUMBER() OVER (
                PARTITION BY artist_id
                ORDER BY tempo DESC
                ) AS rn
        FROM (
            SELECT ar.artist_id, ar.artist_name, t.track_id, song_name, tempo
            FROM artist ar
            JOIN album al
            ON ar.artist_id = al.artist_id
            JOIN track t
            ON t.album_id = al.album_id
            JOIN trackFeature tr
            ON t.track_id = tr.track_id
            -- ORDER BY 1, 4 DESC
            )
    )
    WHERE rn <= 10;
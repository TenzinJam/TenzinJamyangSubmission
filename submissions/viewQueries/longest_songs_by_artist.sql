-- SQLite

-- DROP VIEW longest_songs_by_artist;

CREATE VIEW longest_songs_by_artist
AS
    SELECT artist_id, artist_name, track_id, song_name, duration_ms 
    FROM (
        SELECT artist_id, artist_name, track_id, song_name, duration_ms, 
                ROW_NUMBER() OVER (
                PARTITION BY artist_name
                ORDER BY duration_ms DESC
                ) AS rn
        FROM (
            SELECT ar.artist_id, ar.artist_name, t.track_id, song_name, duration_ms
            FROM artist ar
            INNER JOIN album al
            ON ar.artist_id = al.artist_id
            INNER JOIN track t
            ON t.album_id = al.album_id
            ORDER BY 2
            )
    )
    WHERE rn <= 10;
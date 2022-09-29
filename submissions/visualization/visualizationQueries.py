queries = [
    """SELECT artist_name, popularity 
        FROM artist
        ORDER BY 2 DESC
    """, 

    """SELECT artist_name, AVG(energy) average_energy
        FROM artist ar
        JOIN album al
        ON ar.artist_id = al.artist_id
        JOIN track t
        ON t.album_id = al.album_id
        JOIN track_feature tr
        ON t.track_id = tr.track_id
        GROUP BY 1
        ORDER BY 2 DESC
    """,

    """SELECT release_date, AVG(danceability) average_danceability, artist_name
        FROM (SELECT ar.artist_name, al.release_date, tr.danceability
                FROM artist ar
                JOIN album al
                ON ar.artist_id = al.artist_id
                JOIN track t
                ON al.album_id = t.album_id
                JOIN track_feature tr
                ON t.track_id = tr.track_id
                WHERE ar.artist_name = 'Drake')
        GROUP BY 1
        ORDER BY 1
        """, 

    """SELECT popularity, AVG(valence) average_valence, artist_name
        FROM( SELECT ar.artist_name, ar.popularity, tr.valence
                FROM artist ar
                JOIN album al
                ON ar.artist_id = al.artist_id
                JOIN track t
                ON al.album_id = t.album_id
                JOIN track_feature tr
                ON t.track_id = tr.track_id)
        GROUP BY 3
    """
]

# Creating a singleton that stores dictionaries that correspond spotify column names to that of schema. 

class SchemaColumns(object):
    
    artistColumns = {
        "id": "artist_id", 
        "name": "artist_name",
        "uri": "artist_uri",
        "popularity": "popularity",
        "followers": "followers", 
        "genres": "genre",
        "images": "image_url",
        "type": "type",
        "external_urls": "external_url",
    }


    albumColumns = {
        "id": "album_id", 
        "name": "album_name",
        "uri": "album_uri",
        "album_type": "type",
        "total_tracks": "total_tracks",
        "images": "image_url",
        "release_date": "release_date",
        "external_urls": "external_url",
        "artist_id": "artist_id"
    }

    trackColumns = {
        "id": "track_id", 
        "name": "song_name",
        "uri": "song_uri",
        "duration_ms": "duration_ms",
        "explicit": "explicit",
        "disc_number": "disc_number",
        "external_urls": "external_url",
        "album_id": "album_id", 
        "type": "type"
    }

    featuresColumns = {
        "id":"track_id", 
        "uri": "song_uri",
        "danceability":"danceability" , 
        "energy": "energy", 
        "instrumentalness": "instrumentalness", 
        "liveness": "liveness", 
        "loudness": "loudness",  
        "speechiness": "speechiness", 
        "tempo": "tempo", 
        "type": "type", 
        "valence":"valence"
    }
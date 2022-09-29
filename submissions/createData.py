import sqlite3
import pandas as pd
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# be sure to change this "scope" depending on what kind of spotify personal account data you want to grant your app access to. Getting this wrong can get you a 403 error 
scope = "user-top-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

#        ________________________________________ INGESTION________________________________________________

# getting my top 20 artists from my spotify listening history. "topk" parameter's default value is set to 20 if you do not give it an argument
def getTopArtists(topk=20):
    topArtists = sp.current_user_top_artists(topk)['items']
    pprint(topArtists[0])
    transformValues(topArtists)
    return topArtists


# data transformation already starts with some values being changes from a list or a dictionary to a simple string. Such as with "genres" (a list) and with "external_urls" (a dictionary)
def transformValues(array):
    for elem in array:
        if 'genres' in elem: 
            elem['genres'] = elem['genres'][0] if len(elem['genres']) > 0 else 'genre not specified'
        if 'external_urls' in elem:
            elem['external_urls'] = elem['external_urls']['spotify']
        if 'followers' in elem:
            elem['followers'] = elem['followers']['total']
        if 'images' in elem:
            elem['images'] = elem['images'][0]['url']


# getting the albums of my top artists
# keep in mind that some of the data transforming starts here. We are removing the duplicated albums here
# maximum allowed limit is 50 and it looks good enough to get all the albums from the top artists. 
def getAlbums(artists):
    finalAlbums = []
    for artist in artists:
        albumSet = set()
        albums = sp.artist_albums(artist[0], album_type='album', limit=50)['items']
        
        for album in albums: 
            # this is to deduplicate the double albums we retrieve from the api.  
            if album['name'] not in albumSet:
                album['artist_id'] = artist[0].split(":")[2]
                finalAlbums.append(album)
                albumSet.add(album['name'])

    #before we return the final list of albums, we want to tranform some of the values, just the way we did with the artists
    transformValues(finalAlbums)
    return finalAlbums


    # time to get the tracks based on the collected album uris and their audio features based on track_uri
def getTracksAndFeatures(uris):
    tracks = []
    trackFeatures = []
    for uri in uris:
        albumTracks = sp.album_tracks(uri, limit=50, offset=0, market=None)['items']
        # this is where we are parsing the album id out of the album uri so it can be added as a property in the track's object
        albumId = uri.split(":")[2]

        # this is an important step because we are trying to add the album_id to each of the songs of the album. This information is not provided by data returned by "album_tracks" method, but we 
        # already have the album_id. 
        for eachTrack in albumTracks:
            eachTrack['album_id'] = albumId
        tracks.extend(albumTracks)

        #getting the track features at the end of getting all the tracks from an album
        trackuris = [eachTrack['uri'] for eachTrack in albumTracks]
        features = sp.audio_features(trackuris)
        trackFeatures.extend(features)
    
    # tranforming some of the values here again. 
    transformValues(tracks)
    return (tracks, trackFeatures)


# _________________________________________________TRANSFORMATION___________________________________________________

# some date transformation was already performed when we were cleaning duplicate albums in getAlbums 
# In this phase, It is wise to bring in pandas functionalities and create dataframes to examine if there are any null or blank values and drop any columns not required by the delineated schema 

def prepareSeeding(printTable=False, nullCheck=False):
    #collecting all the data frames so that we can perform multiple transformation on them in a loop
    dataFrames = {}

    # Artist dataframe columns we need: artist_id, artist_name, external_url, genre, image_url, followers, popularity, type, artist_uri
    # columns to drop before seeding: href
    # columns to rename: images to imgurl, genres to genre, external_urls to external_url
    artistsdf = pd.DataFrame(topArtists)
    artistsdf.drop("href", axis = 1, inplace=True)
    artistsdf.rename(columns={"external_urls": "external_url", "genres": "genre", "id": "artist_id", "images": "img_url", "name": "artist_name", "uri": "artist_uri"}, inplace=True)
    dataFrames['artist'] = artistsdf
    # Album dataframe columns we need: album_id, album_name, external_url, image_url, release_date, total_tracks, type, album_uri, artist_id
    # columns to drop before seeding: album_group, href, release_date_precision, available_markets, type
    # columns to rename: images into imgurl, genres to genre, external_urls to external_url

    albumsdf = pd.DataFrame(artistAlbums)
    albumsdf.drop(["href", "album_group", "release_date_precision", "available_markets", "type", "artists"], axis = 1, inplace=True)
    albumsdf.rename(columns={"external_urls": "external_url", "id": "album_id", "images": "img_url", "name": "album_name", "uri": "album_uri", "album_type": "type", "artists": "artist_id"}, inplace=True)
    dataFrames['album'] = albumsdf 
    # print(albumsdf.columns)
    # pprint(albums[0])



    # columns needed: track_id, song_name, external_url, durtaion_ms, explicit, disc_number, type, song_uri, album_id
    # drop columns: artists, available_markets, href, is_local, preview_url, track_number
    # remember that album_id is not a property of a track object. So this album_id addition is done when the tracks are retrieved in getTracks methods. Check above for a detailed implementation
    tracksdf = pd.DataFrame(albumTracks)
    tracksdf.drop(["href", "artists", "is_local", "available_markets", "preview_url", "track_number"], axis = 1, inplace=True)
    tracksdf.rename(columns={"external_urls": "external_url", "id": "track_id", "name": "song_name", "uri": "song_uri"}, inplace=True)
    dataFrames['track'] = tracksdf

    # columns needed: track_id, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, type, valence, song_uri
    # columns to drop: acousticness, analysis_url, duration_ms, mode, time_signature, track_href, key
    trackFeaturesdf = pd.DataFrame(albumTrackFeatures)
    trackFeaturesdf.drop(["track_href", "acousticness", "duration_ms", "mode", "key", "time_signature", "analysis_url"], axis = 1, inplace=True)
    trackFeaturesdf.rename(columns={"id": "track_id", "uri": "song_uri"}, inplace=True)
    dataFrames['trackFeature'] = trackFeaturesdf

    # this is just for developers to check the dataframe to see if the data set matches their expectations. It can be invoked if you passed a True value for the "printTable" parameter
    if printTable: 
        for key in dataFrames:
            pprint(dataFrames[key].head(10))
    
    
    # this step also checks for and cleans all the null values. This is also a switch which can be turned on by passing True for "nullCheck" parameter
    if nullCheck: 
        for key in dataFrames:
            checkAndCleanNull(key, dataFrames[key])


    return (artistsdf, albumsdf, tracksdf, trackFeaturesdf)


def checkAndCleanNull(title, df):

    #checking for null value before and after cleaning the rows with null value. 
    print("_________________________")
    print(f"{title} data frame before cleaning")
    print("_________________________")
    print(df.isnull().sum())

    df.dropna(inplace=True)

    print("_________________________")
    print(f"{title} data frame after cleaning")
    print("_________________________")
    print(df.isnull().sum())


topArtists = getTopArtists()
# collecting all the artist uri's from the previous data in order to retrieve artists' respestive albums. We are also getting the artist name for debugging purposes so that we can associate a uri to an artist's
# name. 
artisturis = [(x['uri'], x['name']) for x in topArtists]
artistAlbums = getAlbums(artisturis)
## collecting all the album uris using list comprehension. Keep in mind that this is the uri and not the album id, so we will do something down the line when we need the album_id for the tracks table/data. 
albumUris = [x['uri'] for x in artistAlbums]

tracksInfo = getTracksAndFeatures(albumUris)
albumTracks = tracksInfo[0]
albumTrackFeatures = tracksInfo[1]

# Passing in a True or False flag for the "printTable" argument to test the data frames by printing them out. It is defaulted at False value (refer to "prepareSeeding" method definition above)
# Same mechanism for "checkNull" parameter. Passing in a True Value will print out the dataframe states regarding null values before and after cleaning. 
(artists, albums, tracks, trackFeatures) = prepareSeeding(True, True)

#_____________________________________________STORAGE_______________________________________________

def seed(dbName):
    conn = connectToDb(dbName)
    artists.to_sql("artist", con=conn, if_exists="replace", index=False)
    albums.to_sql("album", con=conn, if_exists="replace", index=False)
    tracks.to_sql("track", con=conn, if_exists="replace", index=False)
    trackFeatures.to_sql("trackFeature", con=conn, if_exists="replace", index=False)
    conn.commit()


def connectToDb(dbName):
    return sqlite3.connect(dbName)

seed('spotify.db')
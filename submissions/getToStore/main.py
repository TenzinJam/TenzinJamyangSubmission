from schemaColumns import SchemaColumns
from DatabaseClass import Database
from FetchClass import FetchData
from TransformClass import Transform
from pprint import pprint

spotifyDb = Database('spotify1.db')
conn = spotifyDb.conn

spConn = FetchData.connectToSpotify()

tables = {}

def createArtistData():
    artists = FetchData.getTopArtists(spConn)
    artistUris = FetchData.getUris(artists)
    Transform.transformValues(artists)
    artistsdf = Transform.getDataFrame(artists)
    Transform.dropColumns(artistsdf, SchemaColumns.artistColumns)
    Transform.renameColumns(artistsdf, SchemaColumns.artistColumns)
    Transform.checkAndCleanNull("artist", artistsdf)
    tables['artist'] = artistsdf
    return (artistsdf, artistUris)

(artistsdf, artistUris) = createArtistData()

def createAlbumData(uris):
    albums = FetchData.getAlbums(spConn, uris)
    albumUris = FetchData.getUris(albums)
    Transform.transformValues(albums)
    albumsdf = Transform.getDataFrame(albums)
    Transform.dropColumns(albumsdf, SchemaColumns.albumColumns)
    Transform.renameColumns(albumsdf, SchemaColumns.albumColumns)
    Transform.checkAndCleanNull("album", albumsdf)
    tables['album'] = albumsdf
    return (albumsdf, albumUris)

(albumsdf, albumUris) = createAlbumData(artistUris)

def createTrackData(uris):
    tracks = FetchData.getTracks(spConn, uris)
    trackUris = FetchData.getUris(tracks)
    Transform.transformValues(tracks)
    tracksdf = Transform.getDataFrame(tracks)
    Transform.dropColumns(tracksdf, SchemaColumns.trackColumns)
    Transform.renameColumns(tracksdf, SchemaColumns.trackColumns)
    Transform.checkAndCleanNull("track", tracksdf)
    tables['tracks'] = tracksdf
    return (tracksdf, trackUris)

(tracksdf, trackUris) = createTrackData(albumUris)

def createFeatureData(uris):
    length = 100
    uriChunks = [uris[i * length:(i + 1) * length] for i in range((len(uris) + length - 1) // length )]
    features = []
    for chunk in uriChunks:
        featureChunk = FetchData.getTrackFeatures(spConn, chunk)
        features.extend(featureChunk)
    
    Transform.transformValues(features)
    featuresdf = Transform.getDataFrame(features)
    Transform.dropColumns(featuresdf, SchemaColumns.trackColumns)
    Transform.renameColumns(featuresdf, SchemaColumns.trackColumns)
    Transform.checkAndCleanNull("track feature", featuresdf)
    tables['track_feature'] = trackFeaturesdf
    return featuresdf

trackFeaturesdf = createFeatureData(trackUris)

def seed(dictValue):
    for key in dictValue:
        spotifyDb.createTableAndInsert(key, dictValue[key])

seed(tables)
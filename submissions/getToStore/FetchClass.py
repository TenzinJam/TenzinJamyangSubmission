from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class FetchData:

    @staticmethod
    def connectToSpotify():
        scope = "user-top-read"
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        return sp

    @staticmethod
    def getTopArtists(sp, topk=20):
        topArtists = sp.current_user_top_artists(topk)['items']
        pprint(topArtists[0])
        return topArtists
    
    @staticmethod
    def getAlbums(sp, artistUris: list):
        finalAlbums = []
        for uri in artistUris:
            albumSet = set()
            albums = sp.artist_albums(uri, album_type='album', limit=50)['items']
            
            for album in albums: 
                # this is to deduplicate the double albums we retrieve from the api.  
                if album['name'] not in albumSet:
                    album['artist_id'] = uri.split(":")[2]
                    finalAlbums.append(album)
                    albumSet.add(album['name'])

    #before we return the final list of albums, we want to tranform some of the values, just the way we did with the artists
        return finalAlbums

    
    @staticmethod
    def getTracks(sp, albumUris: list):
        tracks = []
        for uri in albumUris:
            albumTracks = sp.album_tracks(uri, limit=50, offset=0, market=None)['items']
            # this is where we are parsing the album id out of the album uri so it can be added as a property in the track's object
            albumId = uri.split(":")[2]

            # this is an important step because we are trying to add the album_id to each of the songs of the album. This information is not provided by data returned by "album_tracks" method, but we 
            # already have the album_id. 
            for eachTrack in albumTracks:
                eachTrack['album_id'] = albumId
            tracks.extend(albumTracks)

            #getting the track features at the end of getting all the tracks from an album
        
        return tracks


    @staticmethod
    def getTrackFeatures(sp, trackUris: list):        
        features = sp.audio_features(trackUris)
        return features

    @staticmethod
    def getUris(listValue):
        uris = [x['uri'] for x in listValue]
        return uris
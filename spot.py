from secrets__ import client_id, client_secret, target_playlist_id, user_id
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

uri = "http://localhost/"

class SpotifyPlaylistFetcher:
    def __init__(self, client_id = client_id, client_secret=client_secret):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                            client_secret=client_secret,
                                                            redirect_uri=uri,
                                                            scope="user-top-read"))

    def get_playlist_tracks(self, playlist_id):
        """Fetch tracks from a specific playlist and return them as a list of strings."""
        results = self.sp.playlist_tracks(playlist_id)
        tracks = []
        while results:
            for item in results['items']:
                track = item['track']
                track_name = track['name']
                track_artists = ', '.join([artist['name'] for artist in track['artists']])
                tracks.append(f"{track_name} by {track_artists}")
            if results['next']:
                results = self.sp.next(results)
            else:
                results = None
        print(tracks)
        #return tracks
    
    def get_user_top_tracks(self, limit=20, time_range='medium_term',offset=5):
        """Fetch the user's top tracks and return them as a list of strings.
        
        Parameters:
        - limit: The number of items to return (maximum 50).
        - time_range: Over what time frame the affinities are computed. 
                      Valid values: 'short_term', 'medium_term', 'long_term'.
        """
        results = self.sp.current_user_top_tracks(limit=limit, offset=0, time_range=time_range)
        tracks = []
        for item in results['items']:
            track_artists = item['name']
            tracks.append(f"{track_artists}")
        print(tracks)
        return tracks
    
a = SpotifyPlaylistFetcher()
a.get_user_top_tracks()


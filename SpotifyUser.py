import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyUser:

    def authorize(self):
        '''
        Authorize the account using Environment Variables needed for Spotipy API
        '''
        scope = "streaming,user-read-currently-playing,user-read-playback-state,user-read-recently-played,user-top-read"
        self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        return self.spotify

    def get_top_tracks(self,num_songs = 20,term = "medium_term"):
        self.top_tracks = self.spotify.current_user_top_tracks(limit=num_songs, time_range=term)
        return self.top_tracks

    def get_top_artists(self,num_artists = 20, term = "medium_term"):
        self.top_artists = self.spotify.current_user_top_artists(limit = num_artists, time_range = term)
        return self.top_artists

    def num_top_tracks(self):
        return len(self.top_tracks["items"])

    def num_top_artists(self):
        return len(self.top_artists["items"])

    def display_top_tracks(self):
        track_counter = 1    
        print("--- Top Songs ---")
        for track in self.top_tracks["items"]:
            print(str(track_counter) + ". "+ track["name"], "-", track["artists"][0]["name"])
            track_counter +=1

    def display_top_artists(self):
        print()
        print("--- Top Artists ---")
        artist_counter = 1
        for artist in self.top_artists["items"]:
            print(str(artist_counter) + ". "+  artist["name"])
            artist_counter +=1
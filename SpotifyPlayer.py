import time
from logging import debug
from random import seed
from random import randint

class SpotifyPlayer:

    def __init__(self,spotify):
        self.spotify = spotify

    def play_song(self, song_number, top_tracks):
        '''
        If a spotify device is active, play the song_number(th) track in the top_tracks list
        '''
        if song_number  >= 1  and top_tracks != None and self.__is_playing_device_active():
            song =[]
            song.append(top_tracks["items"][song_number - 1]["uri"]) 
            self.spotify.start_playback(uris=song)
            self.__now_playing()

    def play_artist(self, artist_number, top_artists):
        '''
        If a spotify device is active, play the artist_number(th) artist in the top_artists list
        '''
        if artist_number >= 1  and top_artists != None and self.__is_playing_device_active():
            artist = top_artists["items"][artist_number - 1]["uri"] 
            self.spotify.start_playback(context_uri=artist)
            self.__now_playing()

    def play_random_top_song(self,top_tracks):
        if top_tracks != None and self.__is_playing_device_active():
            seed()
            num_songs = len(top_tracks["items"])
            random_track_number =  randint(1, num_songs)
            song = []
            song.append(top_tracks["items"][random_track_number - 1]["uri"]) 
            self.spotify.start_playback(uris=song)
            self.__now_playing()  

    def __now_playing(self):
        '''
        Continuously query Spotify for the currently playing song. Once returned, print out the track title and the artist
        '''
        time.sleep(1)
        do_not_have_playing_song = True 
        while do_not_have_playing_song:
            try:
                currently_playing_song = self.spotify.current_playback()
                print("--- Playing "+'"'+currently_playing_song["item"]["name"]+'"',"by", currently_playing_song["item"]["artists"][0]["name"],"---")
                print()
                do_not_have_playing_song = False
            except(TypeError):
                debug(TypeError)

    def __is_playing_device_active(self):
        '''
        Query Spotify for if a device is active. This will allow the playback of tracks/artists
        '''
        device_is_active = False
        devices = self.spotify.devices()["devices"]

        for device in devices:
            if device["is_active"]:
                device_is_active = True

        if not device_is_active:
            print ("Spotify device not active")

        return device_is_active

#TODO Add comments for important functions
#Spotify
from SpotifyUser import SpotifyUser
from SpotifyPlayer import SpotifyPlayer
import HelperFunctions

#Main
user = SpotifyUser()
spotify_access = user.authorize()
spotify_player = SpotifyPlayer(spotify_access)

user_top_tracks = user.get_top_tracks(num_songs = 20, term = "short_term")
user_top_artists = user.get_top_artists(num_artists = 10, term = "short_term")
user.display_top_tracks()
user.display_top_artists()

choices= [
    "1.Play a top song",
    "2.Play a top artist",
    "3.Play a random top song",
    "4.Exit"
]
print("\n\nSelect A Choice:")
for option in choices:
    print(option) 
print()

choice = HelperFunctions.get_choice()

if choice >= 1 and choice <= len(choices) - 1:
    if choice == 1:
        print("Which song would you like to play (1 - " + str(user.num_top_tracks()) + ")? ")
        choice = HelperFunctions.get_choice()
        if choice >= 1 and choice <= user.num_top_tracks():
            spotify_player.play_song(choice,user_top_tracks)
        else:
            HelperFunctions.exit_program()
    elif choice == 2:
        print("Which artist would you like to play (1 - " + str(user.num_top_artists()) + ")? ")
        choice = HelperFunctions.get_choice()
        if choice >= 1 and choice <= user.num_top_artists():
            spotify_player.play_artist(choice,user_top_artists)
            print()
        else:
            HelperFunctions.exit_program()
    elif choice == 3:
        spotify_player.play_random_top_song(user_top_tracks)
else:
    HelperFunctions.exit_program()
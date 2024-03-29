import spotipy
import pickle
from spotipy.oauth2 import SpotifyOAuth
import cred
from playCall import playlistCall


def playlistSongs():
    song_id = []
    id = playlistCall()
    

    scope = "playlist-modify-private"
    sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = cred.client_ID, client_secret = cred.client_SECRET, redirect_uri = cred.redirect_url, scope = scope))

    items = sp.playlist_items(id)
    print(items)
    songs = items['items']
    
    for i in range(len(songs)):
        id = songs[i]['track']['id']
        song_id.append(id)
    
    print(song_id, len(song_id))

    file = open("song_ids.txt", "w+")
    for i in song_id:
        file.write(i + "\n")

playlistSongs()
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
    songs = items['items']
    print(songs)
    
    for i in range(len(songs)):
        id = songs[i]['track']['id']
        song_id.append(id)
    

    pickle.dump(song_id, open("song_ids", "wb"))

playlistSongs()
import spotipy
import pickle
from spotipy.oauth2 import SpotifyOAuth
import cred
from playCall import playlistCall


def playlistSongs():
    id = playlistCall()

    scope = "playlist-modify-private"
    sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = cred.client_ID, client_secret = cred.client_SECRET, redirect_uri = cred.redirect_url, scope = scope))

    items = sp.playlist_items(id)
    
    print(items['items'][0]['added_by']['id'])
    return items

if __name__ == "__main__":
    playlistSongs()
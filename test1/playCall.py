import spotipy
import pickle
from spotipy.oauth2 import SpotifyOAuth
import cred


def playlistCall():
    scope = "playlist-modify-private"
    sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = cred.client_ID, client_secret = cred.client_SECRET, redirect_uri = cred.redirect_url, scope = scope))

    playlists = sp.current_user_playlists()
    print(playlists)
    return (playlists['items'][0]['id'])

if __name__ == "__main__":
    playlistCall()


import pickle
import tkinter
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred
import recSpot

file = open("song_ids", "rb")
ids = pickle.load(file)


scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = cred.client_ID, client_secret = cred.client_SECRET, redirect_uri = cred.redirect_url, scope = scope))

if len(ids) == 0:
    recSpot.spotRecom()
    file = open("song_ids", "rb")
    ids = pickle.load(file)

details = sp.track(ids.pop(0))
print(details)
print(ids)

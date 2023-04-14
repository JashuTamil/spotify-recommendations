import spotipy
import pickle
from spotipy.oauth2 import SpotifyOAuth
import cred

file = open("song_ids", "rb")
song_id = pickle.load(file)
print(song_id)


scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = cred.client_ID, client_secret = cred.client_SECRET, redirect_uri = cred.redirect_url, scope = scope))
recom = sp.recommendations(limit = 1, seed_tracks = song_id[0:5])

print(recom)
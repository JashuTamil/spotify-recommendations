import spotipy
import pickle
from spotipy.oauth2 import SpotifyOAuth
import cred

file = open("song_ids", "rb")
song_id = pickle.load(file)

scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = cred.client_ID, client_secret = cred.client_SECRET, redirect_uri = cred.redirect_url, scope = scope))
recom = sp.recommendations(limit = 5, seed_artists = ["6rniTPs9zN26kYnkPdFl1U"], seed_genres = ["r&b", "pop", "hip-hop"], seed_tracks = [song_id[0]])

print(recom)
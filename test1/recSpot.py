import spotipy
import pickle
from spotipy.oauth2 import SpotifyOAuth
import cred

file = open("song_ids", "rb")
song_id = pickle.load(file)
print(song_id)


scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = cred.client_ID, client_secret = cred.client_SECRET, redirect_uri = cred.redirect_url, scope = scope))
recom = sp.recommendations(limit = 1, seed_artists = ["6rniTPs9zN26kYnkPdFl1U"], seed_genres = ["rock"], seed_tracks = ['0VjIjW4GlUZAMYd2vXMi3b', '0MNNKSUU9OOQ8DSGWduw79', '3xKsf9qdS1CyvXSMEid6g8'])

print(recom)
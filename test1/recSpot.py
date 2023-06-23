import spotipy
import pickle
from spotipy.oauth2 import SpotifyOAuth
import cred

def spotRecom():
    file = open("song_recom", "rb")
    song_id = pickle.load(file)
    ids = []

    songs = []
    scope = "playlist-modify-private"
    sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = cred.client_ID, client_secret = cred.client_SECRET, redirect_uri = cred.redirect_url, scope = scope))
    recom = sp.recommendations(limit = 5, seed_tracks = song_id[0:5])

    for i in recom["tracks"]:
        ids.append(i["id"])

    print(ids)
    pickle.dump(ids, open("song_ids", "wb"))

if __name__ == "__main__":
    spotRecom()

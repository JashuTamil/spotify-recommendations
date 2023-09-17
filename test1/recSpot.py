import spotipy
import pickle
from spotipy.oauth2 import SpotifyOAuth
import cred

def spotRecom():
    song_id = []

    file = open("song_ids.txt", "r")
    ids = file.readlines()
    for line in ids:
        line = line.rstrip("\n")
        song_id.append(line)
    file.close()

    ids = []

    scope = "playlist-modify-private"
    sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = cred.client_ID, client_secret = cred.client_SECRET, redirect_uri = cred.redirect_url, scope = scope))
    recom = sp.recommendations(limit = 5, seed_tracks = song_id[0:5])

    for i in recom["tracks"]:
        ids.append(i["id"])

    print(ids)
    file = open("song_recom", "wb")
    pickle.dump(ids, open("song_ids", "wb"))

if __name__ == "__main__":
    spotRecom()

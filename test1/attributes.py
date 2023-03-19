import spotipy
import pickle
from spotipy.oauth2 import SpotifyOAuth
import cred

scope = "user-top-read"
audioReading = []
danceability = []
energy = []
key = []
loudness = []
speechiness = []
acousticness = []
instrumentalness = []
liveness = []
valence = []
tempo = []
duration = []
time_signature = []
ranking = []
remove = ["mode", "type", "id", "uri", "track_href", "analysis_url"]
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = cred.client_ID, client_secret = cred.client_SECRET, redirect_uri = cred.redirect_url, scope = scope))

results = sp.current_user_top_tracks(limit = 50, time_range = "long_term")


for idx, item in enumerate(results["items"]):
    artists = ""
    tracks = item["id"]
    audioReading.append(tracks)
    trackInfo = sp.track(tracks)

    for x in range(len(trackInfo["artists"])):
        if x != len(trackInfo["artists"]) - 1:
            artists += trackInfo["artists"][x]["name"] + ", "
        else:
            if len(artists) == 0:
                artists += trackInfo["artists"][x]["name"]
            else:
                artists += "and " + trackInfo["artists"][x]["name"]
                

audioFeatures = sp.audio_features(audioReading)
for i in range(len(audioFeatures)):
    for k in remove:
        audioFeatures[i].pop(k, None)
    audioFeatures[i].update({"ranking": i + 1})
    danceability.append(audioFeatures[i]["danceability"])
    """ fill out the rest here """

pickle.dump((danceability, """ fill in the rest here"""), open("audio.pkl", "wb"))



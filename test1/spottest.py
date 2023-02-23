import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred 

scope = "user-top-read"
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = cred.client_ID, client_secret = cred.client_SECRET, redirect_uri = cred.redirect_url, scope = scope))

results = sp.current_user_top_tracks()

print(results)

for idx, item in enumerate(results["items"]):
    tracks = item["track"]
    trackInfo = sp.track(tracks)
    print(trackInfo)

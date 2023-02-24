import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credBryna 
"""
scope = "user-top-read"
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = credBryna.client_ID, client_secret = credBryna.client_SECRET, redirect_uri = credBryna.redirect_url, scope = scope))

results = sp.current_user_top_tracks()


for idx, item in enumerate(results["items"]):
    artists = ""
    tracks = item["id"]
    trackInfo = sp.track(tracks)

    for x in range(len(trackInfo["artists"])):
        if x != len(trackInfo["artists"]) - 1:
            artists += trackInfo["artists"][x]["name"] + ", "
        else:
            if len(artists) == 0:
                artists += trackInfo["artists"][x]["name"]
            else:
                artists += "and " + trackInfo["artists"][x]["name"]
                
    print(idx + 1, trackInfo["name"], "from", trackInfo["album"]["name"], "by", artists)

"""


scope = "user-read-recently-played"

sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = credBryna.client_ID, client_secret = credBryna.client_SECRET, redirect_uri = credBryna.redirect_url, scope = scope))

result = sp.current_user_recently_played()
print(result)








"""
    Sway by Michael Buble, Intertwined by dodie, Reflecting Light by Sam Phillips, Like Real people do by Hozier
    j's lullaby by Delaney Bailey, Haley's Comet by billie eilish, No big deal by dodie, Doomsday by lizzie
    raining in june by olive, rises the moon by flores, romeo & juliet by peter mcpoland
"""

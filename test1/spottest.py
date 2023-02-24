import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

scope = "user-top-read"
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = cred.client_ID, client_secret = cred.client_SECRET, redirect_uri = cred.redirect_url, scope = scope))

results = sp.current_user_top_tracks(limit = 20, time_range = "long_term")


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
    Sway by Michael Buble, Intertwined by dodie, Reflecting Light by Sam Phillips, Like Real people do by Hozier
    j's lullaby by Delaney Bailey, Haley's Comet by billie eilish, No big deal by dodie, Doomsday by lizzie
    raining in june by olive, rises the moon by flores, romeo & juliet by peter mcpoland
    """

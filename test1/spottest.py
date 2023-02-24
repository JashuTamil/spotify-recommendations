import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

scope = "user-read-recently-played"
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = cred.client_ID, client_secret = cred.client_SECRET, redirect_uri = cred.redirect_url, scope = scope))

results = sp.current_user_recently_played(limit = 20)


results = sp.current_user_recently_played()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " - ", track['name'])


    """
    Sway by Michael Buble, Intertwined by dodie, Reflecting Light by Sam Phillips, Like Real people do by Hozier
    j's lullaby by Delaney Bailey, Haley's Comet by billie eilish, No big deal by dodie, Doomsday by lizzie
    raining in june by olive, rises the moon by flores, romeo & juliet by peter mcpoland
    """

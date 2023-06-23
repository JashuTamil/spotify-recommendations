import pickle
from tkinter import *
from PIL import Image, ImageTk
import webbrowser
import spotipy
import urllib.request
from spotipy.oauth2 import SpotifyOAuth
import cred
import recSpot

file = open("song_ids", "rb")
ids = pickle.load(file)


scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = cred.client_ID, client_secret = cred.client_SECRET, redirect_uri = cred.redirect_url, scope = scope))

# Failsafe: If there are no songs, the program will call spotRecom to give the IDs of recommended songs
if len(ids) == 0:
    recSpot.spotRecom()
    file = open("song_ids", "rb")
    ids = pickle.load(file)


# This is all of the details we need to create the window
details = sp.track(ids.pop(0))
songLink = details["external_urls"]["spotify"]
songName = details["name"]
artistName = details["album"]["artists"][0]["name"]
albumArt = details["album"]["images"][0]["url"]
albumArt = urllib.request.urlretrieve(albumArt, "albumArt.png")


# This is where the window execution starts. It will use the above variables to output the song
window = Tk()
window.title("Your Song Recommendation")
window.geometry("760x590")

def open():
    webbrowser.open(songLink)

def destroy():
    window.quit()

albumArt = Image.open("albumArt.png")
albumArt = albumArt.resize((500, 500))
albumArt = ImageTk.PhotoImage(albumArt)

songArtist = Label(window, text = artistName)
songArtist.grid(row = 2, column = 1)

songTitle = Label(window, text = songName)
songTitle.grid(row = 1, column = 1)

artist = Label(window, text = "Artist: ")
artist.grid(row = 2, column = 0)

song = Label(window, text = "Song: ")
song.grid(row = 1, column = 0)

song2 = Label(window, text = "   ")
song2.grid(row = 3, column = 3)

labelImg = Label(window, image = albumArt)
labelImg.image = albumArt
labelImg.grid(row = 3, column = 4)


link = Button(window, text = "Go to Song!", command = lambda: [open(), destroy()], padx = 50)
link.grid(row = 4, column = 4)



window.mainloop()




from tkinter import *
from PIL import Image
import webbrowser

window = Tk()
window.title("Your Song Recommendation")
window.geometry("500x300")


name = "Cherry Wine"
artist = "grentperez"
artwork = Image.open("ab67616d0000b273136ef277a0791089f46628bb.jpg")
songLink = "https://open.spotify.com/track/5o5WaO9pzPhXSGIrTIYVce?si=e4ccf1b68a064f79"

def open():
    webbrowser.open(songLink)

songArtist = Label(window, text = artist)
songArtist.grid(row = 2, column = 1)

songTitle = Label(window, text = name)
songTitle.grid(row = 1, column = 1)

artist = Label(window, text = "Artist: ")
artist.grid(row = 2, column = 0)

song = Label(window, text = "Song: ")
song.grid(row = 1, column = 0)


link = Button(window, text = "Go to Song!", command = open, padx = 50)
link.place(relx = .5, rely = .5, anchor = S)



window.mainloop()
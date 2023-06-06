from tkinter import *
from PIL import Image, ImageTk
import webbrowser
import sys

window = Tk()
window.title("Your Song Recommendation")
window.geometry("760x590")




name = "Cherry Wine"
artist = "grentperez"
artwork = Image.open("ab67616d0000b273136ef277a0791089f46628bb.jpg")
artwork = artwork.resize((500, 500))
artwork = ImageTk.PhotoImage(artwork)
songLink = "https://open.spotify.com/track/5o5WaO9pzPhXSGIrTIYVce?si=e4ccf1b68a064f79"

def open():
    webbrowser.open(songLink)

def destroy():
    window.quit()


songArtist = Label(window, text = artist)
songArtist.grid(row = 2, column = 1)

songTitle = Label(window, text = name)
songTitle.grid(row = 1, column = 1)

artist = Label(window, text = "Artist: ")
artist.grid(row = 2, column = 0)

song = Label(window, text = "Song: ")
song.grid(row = 1, column = 0)

song2 = Label(window, text = "   ")
song2.grid(row = 3, column = 3)

labelImg = Label(window, image = artwork)
labelImg.image = artwork
labelImg.grid(row = 3, column = 4)


link = Button(window, text = "Go to Song!", command = lambda: [open(), destroy()], padx = 50)
link.grid(row = 4, column = 4)



window.mainloop()

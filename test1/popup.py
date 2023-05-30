import pickle
import tkinter

file = open("song_ids", "rb")
ids = pickle.load(file)
print(ids)

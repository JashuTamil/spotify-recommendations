import tensorflow
import pickle
import sklearn
from sklearn.neighbors import KNeighborsClassifier


audioPickle = open("audio.pkl", "rb")
danceability, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration, time_signature, ranking = pickle.load(audioPickle)
print(danceability)

x = list(zip(danceability, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration, time_signature))
y = ranking

print(x)
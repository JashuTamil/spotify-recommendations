import tensorflow
import pickle
import sklearn
from sklearn.neighbors import KNeighborsClassifier

arrtibutes = ["danceability", "energy", "key", "loudness", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo", "duration", "time_signature", "ranking"]
audioPickle = open("audio.pkl", "rb")
danceability, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration, time_signature, ranking = pickle.load(audioPickle)

x = list(zip(danceability, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration, time_signature))
y = ranking

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = .1)

model = KNeighborsClassifier(n_neighbors = 12)

model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print(acc)

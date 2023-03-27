import tensorflow
import pickle
import sklearn
from sklearn.neighbors import KNeighborsClassifier

arrtibutes = ["danceability", "energy", "key", "loudness", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo", "duration", "time_signature", "ranking"]
audioPickle = open("normalAudio.pkl", "rb")
danceability, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration, time_signature, ranking = pickle.load(audioPickle)

x = list(zip(danceability, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration, time_signature))
y = ranking

print(x)


x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = .1)

model = KNeighborsClassifier(n_neighbors = 2)

model.fit(x_train, y_train)
y_pred = model.predict(x_test)
acc = model.accuracy_score(y_test, y_pred)
print(acc)

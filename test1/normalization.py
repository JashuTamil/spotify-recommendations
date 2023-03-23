import pickle

audioPickle = open("audio.pkl", "rb")
danceability, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration, time_signature, ranking = pickle.load(audioPickle)

print(danceability, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration, time_signature, ranking)
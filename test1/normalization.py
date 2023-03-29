import pickle
from sklearn import preprocessing

le = preprocessing.LabelEncoder()

"""def normalizeAtttibute(attribute):
    minimum = min(attribute)
    range = max(attribute) - min(attribute)
    normalized = []
    for i in attribute:
        num = i - minimum
        num /= range
        normalized.append(num)
    return normalized"""

def normalizeAtttibute(attribute):
    return le.fit_transform(attribute)


audioPickle = open("audio.pkl", "rb")
danceability, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration, time_signature, ranking = pickle.load(audioPickle)

print(danceability, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration, time_signature, ranking)

danceability = normalizeAtttibute(danceability)
energy = normalizeAtttibute(energy)
key = normalizeAtttibute(key)
loudness = normalizeAtttibute(loudness)
speechiness = normalizeAtttibute(speechiness)
acousticness = normalizeAtttibute(acousticness)
instrumentalness = normalizeAtttibute(instrumentalness)
liveness = normalizeAtttibute(liveness)
valence = normalizeAtttibute(valence)
tempo = normalizeAtttibute(tempo)
duration = normalizeAtttibute(duration)
time_signature = normalizeAtttibute(time_signature)
ranking = normalizeAtttibute(ranking)

print(danceability, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration, time_signature, ranking)

pickle.dump((danceability, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration, time_signature, ranking), open("normalAudio1.pkl", "wb"))


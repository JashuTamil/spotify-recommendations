import tensorflow
import pickle
import sklearn
from sklearn.neighbors import KNeighborsClassifier


audioPickle = open("audio.pkl", "rb")
audioFeatures = pickle.load(audioPickle)

predict = "ranking"

print(audioFeatures[0][predict])
""" after new pkl file is created, make sure each and every list is accounted for. Then, make sure they're zipped to x and y (which is the ranking) """
""" then move forward with the knn algorithm """
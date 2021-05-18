import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv('~\Documents\Machine Learning\Car DB - ICS UCI\car.data')
print(data.head())

lenc = preprocessing.LabelEncoder()

buying = lenc.fit_transform(list(data["buying"]))
# This code gets all the values from the 'buying' column, transforms them into a list and then label encodes them as integers
maint = lenc.fit_transform(list(data["maint"]))
door = lenc.fit_transform(list(data["door"]))
persons = lenc.fit_transform(list(data["persons"]))
lug_boot = lenc.fit_transform(list(data["lug_boot"]))
safety = lenc.fit_transform(list(data["safety"]))
cls = lenc.fit_transform(list(data["class"])) #can't name it class

predict = 'class'

X = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(cls)

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2, random_state=42)

model = KNeighborsClassifier(n_neighbors=7)

model.fit(X_train, y_train)
acc = model.score(X_test, y_test)
print(acc)

predicted = model.predict(X_test)
names = ['unacc','acc','good','vgood'] # target names

for x in range(len(X_test)):
    print("Predicted: ", names[predicted[x]], "Data: ", X_test[x], "Actual: ", names[y_test[x]])
    n = model.kneighbors([X_test[x]], 7, True) # shows you the distance to it's k nearest neighbours
    print("N: ", n)

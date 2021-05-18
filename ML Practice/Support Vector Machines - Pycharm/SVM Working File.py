import pandas as pd
import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

# loading sklearn datasets below:
cancer = datasets.load_breast_cancer()

#print(cancer.feature_names)
#print(cancer.target_names)

X = cancer.data
y = cancer.target

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2, random_state=42)

print(len(X_train), len(X_test))

classes = ['malignant', 'benign'] # use these classes to cobvert our actual output from 0s and 1s, to target names

classifier = svm.SVC(kernel= 'linear', C=3) # can choose other paramaters too, like 'poly, see SVC bookmark guide

#classifier = KNeighborsClassifier(n_neighbors= 15) # testing knn also
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

acc = metrics.accuracy_score(y_test, y_pred)

print(acc)


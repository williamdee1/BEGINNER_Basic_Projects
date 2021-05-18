import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as plt
import pickle
from matplotlib import style

data = pd.read_csv('~\Documents\Machine Learning\Student DB - ICS UCI\student-mat.csv', sep = ';')

print(data.head())

data = data[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']]

predict = 'G3'

X = np.array(data.drop([predict], 1)) # Dropping all data from the predict column (G3), on column so 1
y = np.array(data[predict]) # trying to predict G3

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1, random_state=3)
# Takes all of our attributes, and splits them into 4 different arrays, test size is 10% (0.1 above)
# Does this so it's not training the model based on data in the test set, so it doesn't already 'know' the values

"""linear = linear_model.LinearRegression()

linear.fit(X_train, y_train)
# This is using the LinearRegression model to get a line of best fit for our training data
# It will then store that line within 'linear'

acc = linear.score(X_test, y_test)
print(acc)

with open('lrmodel.pickle', 'wb') as f:
    pickle.dump(linear, f)"""
# f stands for file, essentially this is saving a file in our directory using pickle that we can call later
# Have commented it out above as it's now automated below
# This is being saved in the base directory which is PycharmProjects\tensorEnv

# Below we are loading in the pickle we've saved, to apply the LR model to the data
pickle_in = open('lrmodel.pickle', 'rb')
# we can now load this pickle in our linear model
linear = pickle.load(pickle_in)

print("Coefficients: ", linear.coef_)
print("Intercept: ", linear.intercept_)

# Now using this to predict one students grades:
predictions = linear.predict(X_test)

for x in range(len(predictions)):
    print(predictions[x], X_test[x], y_test[x])
# Shows actual predictions vs the predictors and the target we used in the model

p = 'absences'
style.use('ggplot')
plt.scatter(data[p], data['G3'])
plt.xlabel(p)
plt.ylabel("Final Grade")
plt.show()
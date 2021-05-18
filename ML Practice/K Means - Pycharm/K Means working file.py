import numpy as np
import sklearn
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn import metrics

digits = load_digits()
data = scale(digits.data) #scaling down the large numbers in this dataset to save computational time

y = digits.target

k = len(np.unique(y))  # uses the amount of diff classes
samples, features = data.shape


# Function from sklearn for different scorings - https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html
def bench_k_means(estimator, name, data):
    estimator.fit(data)
    print('%-9s\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
          % (name, estimator.inertia_,
             metrics.homogeneity_score(y, estimator.labels_),
             metrics.completeness_score(y, estimator.labels_),
             metrics.v_measure_score(y, estimator.labels_),
             metrics.adjusted_rand_score(y, estimator.labels_),
             metrics.adjusted_mutual_info_score(y,  estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_,
                                      metric='euclidean')))

#euclidean is the absolute distance between two objects

classifier = KMeans(n_clusters=k, init='random', n_init=10)
# init means where each centroid will start, n_init, is how many times to randomly generate the centroids before beginning the classification

bench_k_means(classifier, "1", data)